# 舞萌DX科技专页

本项目是舞萌DX科技专页的简易后端。

## 开发环境

本项目使用 [Flask](https://flask.palletsprojects.com/) 作为服务器框架，使用 [Python](https://python.org/) 作为基础语言。

请使用下面的命令运行项目：

```bash
python3 main.py
```

## 关于 `sdgb.py`

这个东西请自备，本仓库不提供， `sdgb.py` 中有两个我们会用到的函数， `sdgb_api` 和 `qr_api`。

`sdgb_api` 用于和官方服务器进行通讯，其调用方法如下：

```python
sdgb_api(data, useApi, userId)
"""
data表示要向服务器发送的数据本体，其格式是json字符串
useApi是string类型，代表api端点，无需添加服务器后缀（如MaiChn）
userId是int类型，传入用户ID

返回值是字符串类型，代表官方服务器返回的信息。
"""
```

`qr_api` 是与官方AimeDB通讯用于解析二维码到用户ID的的函数，其调用方法如下：

```python
qr_api(qr_code)
"""
qr_code是string类型，代表二维码的内容，一般为MAID或者SGWCMAID开头的字符串

返回值是json对象，代表官方服务器返回的信息经过json序列化后的结果。
"""
```

## 备注

项目仍在积极开发中，因此可能存在一些问题。