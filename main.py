from flask import Flask, request, jsonify
from sdgb import sdgb_api, qr_api
from function import *
from settings import *
from dbconfig import get_database_config
import json, time
from datetime import datetime, timedelta
from flask_cors import CORS  # 导入 flask-cors
from flask_sqlalchemy import SQLAlchemy
from dbmodels import *
from authlite import authlite
import httpx, re
from updatedata import updatedata

app = Flask(__name__)
CORS(app)  # 全局允许跨域请求
app.config.from_object(get_database_config())
db.init_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"stat": 404, "msg": "页面未找到。", "data": None, "timestamp": int(time.time())}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"stat": 405, "msg": "使用了未受支持的方式调用接口，请查看文档后重试。", "data": None, "timestamp": int(time.time())}), 405

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"stat": 400, "msg": "坏了，就是有些东西坏了。", "data": None, "timestamp": int(time.time())}), 400

@app.route('/', methods=['POST', 'GET'])
def handle_root():
    return jsonify({'stat': 1, 'msg':'Welcome to Maimai~'}), 200

@app.route('/api/v1/qrcode', methods=['POST'])
def handle_qrcode():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # 检查是否传入了"maid"参数
    if 'maid' not in data:
        return jsonify({'stat': -1, 'msg': '未传入MAID', 'userId': -1}), 400

    maid = data['maid']
    try:
        aime_data = qr_api(maid)
        if aime_data['errorID'] == 0:
            return jsonify({'stat': 1, 'msg': '成功获取userId', 'userId': aime_data['userID']})
        return jsonify({'stat': aime_data['errorID'], 'msg': 'userId获取失败', 'userId': aime_data['userID']}), 400
    except:
        return jsonify({'stat': -1, 'msg': '服务器发生内部错误', 'userId': -1}), 500

@app.route('/api/v1/player/preview', methods=['POST'])
def handle_preview():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    
    if 'userId' not in data:
        return jsonify({'stat': -1, 'msg': '未传入userId', 'data': None}), 400
    userId = data['userId']
    try:
        data = json.dumps({
            "userId": int(userId)
        })

        preview_result = sdgb_api(data, "GetUserPreviewApi", int(userId))
        preview_data = json.loads(preview_result)
        if preview_data['userId'] == None:
            return jsonify({'stat': -1, 'msg': '获取信息失败', 'data': preview_data}), 400
        return jsonify({'stat': 1, 'msg': '已获取信息', 'data': preview_data})
    except:
        return jsonify({'stat': -1, 'msg': '服务器发生内部错误', 'data': None}), 500

@app.route('/api/v1/player/sendticket', methods=['POST'])
def handle_sendticket():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    timestamp = int(datetime.now(pytz.timezone('Asia/Shanghai')).timestamp())
    if 'userId' not in data:
        return jsonify({'stat': -1, 'msg': '未传入userId', 'data': None, 'timestamp': timestamp}), 400
    if 'ticketId' not in data:
        return jsonify({'stat': -1, 'msg': '未传入ticketId', 'data': None, 'timestamp': timestamp}), 400
    try:
        userId = int(data['userId'])
        # print(userId)
        ticketId = int(data['ticketId'])
        # print(ticketId)
        price = int(ticketId) - 1
        if price > 5:
            price = 0
        # print(price)
        data = json.dumps({
            "userId": userId,
            "userCharge": {
                "chargeId": ticketId,
                "stock": 1,
                "purchaseDate": (datetime.now(pytz.timezone('Asia/Shanghai'))).strftime("%Y-%m-%d %H:%M:%S.0"),
                "validDate": (datetime.now(pytz.timezone('Asia/Shanghai')) + timedelta(days=90)).replace(hour=4, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")
            },
            "userChargelog": {
                "chargeId": ticketId,
                "price": price,
                "purchaseDate": (datetime.now(pytz.timezone('Asia/Shanghai'))).strftime("%Y-%m-%d %H:%M:%S.0"),
                "placeId": placeId,
                "regionId": regionId,
                "clientId": clientId
            }
        })
        loginresult = login(userId, timestamp)
        # print(loginresult)
        if loginresult['returnCode'] != 1:
            return jsonify({'stat': loginresult['returnCode'], 'msg': '登录失败，请检查是否存在有效二维码。', 'data': None, 'timestamp': timestamp}), 400
        ticket_result = json.loads(sdgb_api(data, "UpsertUserChargelogApi", userId))
        # print(ticket_result)
        logoutresult = logout(userId, timestamp)
        # print(logoutresult)
        if ticket_result['returnCode'] != 1 and logoutresult['returnCode'] == 1:
            return jsonify({'stat': ticket_result['returnCode'], 'msg': '发券失败，但已经成功登出。', 'data': None, 'timestamp': timestamp}), 400
        if ticket_result['returnCode'] != 1 and logoutresult['returnCode'] != 1:
            return jsonify({'stat': logoutresult['returnCode'], 'msg': '发券失败，且登出失败！请根据时间戳'+str(timestamp)+'手动登出，否则可能进入小黑屋！', 'data': None, 'timestamp': timestamp}), 400
        if ticket_result['returnCode'] == 1 and logoutresult['returnCode'] != 1:
            return jsonify({'stat': logoutresult['returnCode'], 'msg': '发券成功，但登出失败！请根据时间戳'+str(timestamp)+'手动登出，否则可能进入小黑屋！', 'data': None, 'timestamp': timestamp}), 400
        return jsonify({'stat': 1, 'msg': '发券成功！', 'data': None, 'timestamp': timestamp})
    except:
        return jsonify({'stat': -1, 'msg': '服务器发生内部错误', 'data': None, 'timestamp': timestamp}), 500
    
@app.route('/api/v1/player/updatedata', methods=['POST'])
def handle_updatedata():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    
    if 'userId' not in data:
        return jsonify({'stat': -1, 'msg': '未传入userId', 'data': None}), 400
    userId = data['userId']
    timestamp = int(datetime.now(pytz.timezone('Asia/Shanghai')).timestamp())
    try:
        return updatedata(userId, timestamp)
    except Exception as e:
        logout(userId, timestamp)
        print(e)
        return jsonify({'stat': -1, 'msg': '服务器发生内部错误', 'data': None, 'timestamp': timestamp}), 500
    
# 测试数据库连接
@app.route('/api/v1/setdb', methods=['POST','GET'])
def handle_setdb():
    if not db_setdb_lock:
        try:
            # 测试数据库是否连接成功
            db.create_all()  # 创建所有数据库表（如果还没有）
            return jsonify({'stat': 1, 'msg': '数据库连接成功', 'data': None})
        except Exception as e:
            return jsonify({'stat': -1, 'msg': f"数据库连接失败: {e}", 'data': None}), 500
    else:
        return jsonify({'stat': -1, 'msg': '无权限操作', 'data': None}), 403
    
@app.route('/api/v1/serverstatus', methods=['POST','GET'])
def handle_serverstatus():
    aimedbstatus = False
    titleserverstatus = False
    updateserverstatus = False
    fakeqrcode = "SGWCMAID0000000000000000000000000000000000000000000000000000000000000000"
    try:
        aimedata = qr_api(fakeqrcode)
        if aimedata["errorID"] == 1 or aimedata["userID"] < 10:
            aimedbstatus = True
    except:
        aimedbstatus = False
    try:
        titledata = json.loads(sdgb_api("{}", "Ping", 0))
        if titledata["result"] == "Pong":
            titleserverstatus = True
    except:
        titleserverstatus = False
    try:
        updatedata = authlite()
        if updatedata["result"] == "1":
            updateserverstatus = True
    except:
        updateserverstatus = False
    return jsonify({'stat': 1, 'msg': '获取服务器状态成功', 'data': {'aimedb': aimedbstatus, 'titleserver': titleserverstatus, 'updateserver': updateserverstatus}})

@app.route('/api/v1/getopt', methods=['POST','GET'])
def handle_getopt():
    try:
        updatedata = authlite()
        if updatedata["result"] != "1":
            return jsonify({'stat': -1, 'msg': '获取opt失败', 'data': {"instruction": None, "opts": None}}), 400
        print(updatedata)
        r = httpx.get(
            updatedata["uri"],
            headers = {
                'User-Agent': 'SDGB;Windows/Lite',
                'host': 'maimai-haisin.wahlap.com'
            }
        )
        print(r.status_code)
        instruction_data = str(r.content)
        opt_links = re.findall(r"https?://[^\s;]+?\.opt", instruction_data)
        return jsonify({'stat': 1, 'msg': '获取opt成功', 'data': {"instruction": updatedata["uri"], "opts": opt_links}})
    except:
        return jsonify({'stat': -1, 'msg': '服务器发生内部错误', 'data': {"instruction": None, "opts": None}}), 500

if __name__ == '__main__':
    # 启动 Flask 应用程序
    app.run(host=app_host, port=app_port, debug=app_debug)
