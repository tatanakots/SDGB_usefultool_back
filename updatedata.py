from flask import Flask, request, jsonify
from sdgb import sdgb_api, qr_api
import json, time
from function import *
from dbmodels import *

def getuseritem(userId: int, nextIndex: int, maxCount: int) -> dict:
    for i in range(10):
        try:
            data = json.dumps({
                "userId": int(userId),
                "nextIndex": int(nextIndex),
                "maxCount": int(maxCount),
            })
            useritem_result = sdgb_api(data, "GetUserItemApi", userId)
            return json.loads(useritem_result)
        except ValueError as e:
            print(e)
            time.Sleep(1)
    return None

def getusermap(userId: int, nextIndex: int, maxCount: int) -> dict:
    for i in range(10):
        try:
            data = json.dumps({
                "userId": int(userId),
                "nextIndex": int(nextIndex),
                "maxCount": int(maxCount),
            })
            usermap_result = sdgb_api(data, "GetUserMapApi", userId)
            return json.loads(usermap_result)
        except ValueError as e:
            print(e)
            time.Sleep(1)
    return None

def getuserloginbonus(userId: int, nextIndex: int, maxCount: int) -> dict:
    for i in range(10):
        try:
            data = json.dumps({
                "userId": int(userId),
                "nextIndex": int(nextIndex),
                "maxCount": int(maxCount),
            })
            userloginbonus_result = sdgb_api(data, "GetUserLoginBonusApi", userId)
            return json.loads(userloginbonus_result)
        except ValueError as e:
            print(e)
            time.Sleep(1)
    return None

def getusermusic(userId: int, nextIndex: int, maxCount: int) -> dict:
    for i in range(10):
        try:
            data = json.dumps({
                "userId": int(userId),
                "nextIndex": int(nextIndex),
                "maxCount": int(maxCount),
            })
            usermusic_result = sdgb_api(data, "GetUserMusicApi", userId)
            return json.loads(usermusic_result)
        except ValueError as e:
            print(e)
            time.Sleep(1)
    return None

def getusercourse(userId: int, nextIndex: int) -> dict:
    for i in range(10):
        try:
            data = json.dumps({
                "userId": int(userId),
                "nextIndex": int(nextIndex),
            })
            usercourse_result = sdgb_api(data, "GetUserCourseApi", userId)
            return json.loads(usercourse_result)
        except ValueError as e:
            print(e)
            time.Sleep(1)
    return None

def updatedata(userId, timestamp):
    login_data = login(userId, timestamp)
    if login_data["returnCode"] == 102:
        return jsonify({'stat': 102, 'msg': '用户登录失败，请检查是否拥有有效的二维码。', 'data': None, 'timestamp': timestamp}), 400
    if login_data["returnCode"] == 100:
        return jsonify({'stat': 100, 'msg': '用户登录失败，请检查用户是否正在登录中，若无法退出登录，请15分钟后再试一次。', 'data': None, 'timestamp': timestamp}), 400
    if login_data["returnCode"] != 1:
        return jsonify({'stat': login_data["returnCode"], 'msg': '用户登录失败，未知错误。', 'data': None, 'timestamp': timestamp}), 400
    data = json.dumps({
        "userId": int(userId)
    })
    user_data = json.loads(sdgb_api(data, "GetUserDataApi", userId))
    if user_data != None:
        db_userdata_table = User(
            userId                   = user_data["userId"],
            username                 = user_data["userData"]["userName"],
            accessCode               = user_data["userData"]["accessCode"],
            friendCode               = user_data["userData"]["friendCode"],
            isNetMember              = user_data["userData"]["isNetMember"],
            playerRating             = user_data["userData"]["playerRating"],
            playerOldRating          = user_data["userData"]["playerOldRating"],
            playerNewRating          = user_data["userData"]["playerNewRating"],
            highestRating            = user_data["userData"]["highestRating"],
            gradeRating              = user_data["userData"]["gradeRating"],
            musicRating              = user_data["userData"]["musicRating"],
            gradeRank                = user_data["userData"]["gradeRank"],
            courseRank               = user_data["userData"]["courseRank"],
            classRank                = user_data["userData"]["classRank"],
            nameplateId              = user_data["userData"]["nameplateId"],
            frameId                  = user_data["userData"]["frameId"],
            iconId                   = user_data["userData"]["iconId"],
            trophyId                 = user_data["userData"]["trophyId"],
            plateId                  = user_data["userData"]["plateId"],
            titleId                  = user_data["userData"]["titleId"],
            partnerId                = user_data["userData"]["partnerId"],
            charaSlot                = json.dumps(user_data["userData"]["charaSlot"]),
            charaLockSlot            = json.dumps(user_data["userData"]["charaLockSlot"]),
            contentBit               = user_data["userData"]["contentBit"],
            selectMapId              = user_data["userData"]["selectMapId"],
            playCount                = user_data["userData"]["playCount"],
            currentPlayCount         = user_data["userData"]["currentPlayCount"],
            playVsCount              = user_data["userData"]["playVsCount"],
            playSyncCount            = user_data["userData"]["playSyncCount"],
            winCount                 = user_data["userData"]["winCount"],
            helpCount                = user_data["userData"]["helpCount"],
            comboCount               = user_data["userData"]["comboCount"],
            totalDeluxscore          = user_data["userData"]["totalDeluxscore"],
            totalBasicDeluxscore     = user_data["userData"]["totalBasicDeluxscore"],
            totalAdvancedDeluxscore  = user_data["userData"]["totalAdvancedDeluxscore"],
            totalExpertDeluxscore    = user_data["userData"]["totalExpertDeluxscore"],
            totalMasterDeluxscore    = user_data["userData"]["totalMasterDeluxscore"],
            totalReMasterDeluxscore  = user_data["userData"]["totalReMasterDeluxscore"],
            totalSync                = user_data["userData"]["totalSync"],
            totalBasicSync           = user_data["userData"]["totalBasicSync"],
            totalAdvancedSync        = user_data["userData"]["totalAdvancedSync"],
            totalExpertSync          = user_data["userData"]["totalExpertSync"],
            totalMasterSync          = user_data["userData"]["totalMasterSync"],
            totalReMasterSync        = user_data["userData"]["totalReMasterSync"],
            totalAchievement         = user_data["userData"]["totalAchievement"],
            totalBasicAchievement    = user_data["userData"]["totalBasicAchievement"],
            totalAdvancedAchievement = user_data["userData"]["totalAdvancedAchievement"],
            totalExpertAchievement   = user_data["userData"]["totalExpertAchievement"],
            totalMasterAchievement   = user_data["userData"]["totalMasterAchievement"],
            totalReMasterAchievement = user_data["userData"]["totalReMasterAchievement"],
            eventWatchedDate         = user_data["userData"]["eventWatchedDate"],
            lastGameId               = user_data["userData"]["lastGameId"],
            lastRomVersion           = user_data["userData"]["lastRomVersion"],
            lastDataVersion          = user_data["userData"]["lastDataVersion"],
            lastLoginDate            = user_data["userData"]["lastLoginDate"],
            lastPlayDate             = user_data["userData"]["lastPlayDate"],
            lastPairLoginDate        = user_data["userData"]["lastPairLoginDate"],
            lastTrialPlayDate        = user_data["userData"]["lastTrialPlayDate"],
            lastPlayCredit           = user_data["userData"]["lastPlayCredit"],
            lastPlayMode             = user_data["userData"]["lastPlayMode"],
            lastPlaceId              = user_data["userData"]["lastPlaceId"],
            lastPlaceName            = user_data["userData"]["lastPlaceName"],
            lastAllNetId             = user_data["userData"]["lastAllNetId"],
            lastRegionId             = user_data["userData"]["lastRegionId"],
            lastRegionName           = user_data["userData"]["lastRegionName"],
            lastClientId             = user_data["userData"]["lastClientId"],
            lastCountryCode          = user_data["userData"]["lastCountryCode"],
            lastSelectEMoney         = user_data["userData"]["lastSelectEMoney"],
            lastSelectTicket         = user_data["userData"]["lastSelectTicket"],
            lastSelectCourse         = user_data["userData"]["lastSelectCourse"],
            lastCountCourse          = user_data["userData"]["lastCountCourse"],
            firstGameId              = user_data["userData"]["firstGameId"],
            firstRomVersion          = user_data["userData"]["firstRomVersion"],
            firstDataVersion         = user_data["userData"]["firstDataVersion"],
            firstPlayDate            = user_data["userData"]["firstPlayDate"],
            compatibleCmVersion      = user_data["userData"]["compatibleCmVersion"],
            totalAwake               = user_data["userData"]["totalAwake"],
            dailyBonusDate           = user_data["userData"]["dailyBonusDate"],
            dailyCourseBonusDate     = user_data["userData"]["dailyCourseBonusDate"],
            mapStock                 = user_data["userData"]["mapStock"],
            renameCredit             = user_data["userData"]["renameCredit"],
            cmLastEmoneyCredit       = user_data["userData"]["cmLastEmoneyCredit"],
            cmLastEmoneyBrand        = user_data["userData"]["cmLastEmoneyBrand"],
            dateTime                 = user_data["userData"]["dateTime"],
            banState                 = user_data["banState"],
            updateTime               = timestamp
        )
        db.session.merge(db_userdata_table)
        db.session.commit()
    data = json.dumps({
        "userId": int(userId)
    })
    user_character_data = json.loads(sdgb_api(data, "GetUserCharacterApi", userId))
    if user_character_data != None:
        db.session.query(UserCharacter).filter_by(userId=user_character_data["userId"]).delete()
        for entry in user_character_data["userCharacterList"]:
            uc = UserCharacter(
                userId           = user_character_data["userId"],
                characterId      = entry["characterId"],
                point            = entry["point"],
                useCount         = entry["useCount"],
                level            = entry["level"],
                nextAwake        = entry["nextAwake"],
                nextAwakePercent = entry["nextAwakePercent"],
                awakening        = entry["awakening"],
                updateTime       = timestamp
            )
            db.session.add(uc)
        db.session.commit()
    user_item_list = []
    nextIndex = 100000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 30000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 40000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 110000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 120000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 50000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 60000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 70000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    nextIndex = 80000000000
    maxCount = 100
    while True:
        user_item_data = getuseritem(userId, nextIndex, maxCount)
        # print(user_item_data)
        if user_item_data != None:
            nextIndex = user_item_data['nextIndex']
            if user_item_data['userItemList'] == None:
                break
            for userItem in user_item_data['userItemList']:
                user_item_list.append(userItem)
            if nextIndex == 0:
                break
        else:
            break
    db.session.query(UserItem).filter_by(userId=userId).delete()
    for entry in user_item_list:
        ui = UserItem(
            userId     = userId,
            itemKind   = entry["itemKind"],
            itemId     = entry["itemId"],
            stock      = entry["stock"],
            isValid    = entry["isValid"],
            updateTime = timestamp
        )
        db.session.add(ui)
    db.session.commit()
    user_course_list = []
    nextIndex = 0
    while True:
        user_course_data = getusercourse(userId, nextIndex)
        if user_course_data != None:
            nextIndex = user_course_data['nextIndex']
            if user_course_data['userCourseList'] == None:
                break
            for userCourse in user_course_data['userCourseList']:
                user_course_list.append(userCourse)
            if nextIndex == 0:
                break
        else:
            break
    db.session.query(UserCourse).filter_by(userId=userId).delete()
    for entry in user_course_list:
        uc = UserCourse(
            userId             = userId,
            courseId           = entry["courseId"],
            isLastClear        = entry["isLastClear"],
            totalRestlife      = entry["totalRestlife"],
            totalAchievement   = entry["totalAchievement"],
            totalDeluxscore    = entry["totalDeluxscore"],
            bestAchievement    = entry["bestAchievement"],
            bestDeluxscore     = entry["bestDeluxscore"],
            bestAchievementDate= entry["bestAchievementDate"],
            bestDeluxscoreDate = entry["bestDeluxscoreDate"],
            playCount          = entry["playCount"],
            clearDate          = entry["clearDate"],
            lastPlayDate       = entry["lastPlayDate"],
            extNum1            = entry["extNum1"],
            updateTime         = timestamp
        )
        db.session.add(uc)
    db.session.commit()
    user_map_list = []
    nextIndex = 0
    maxCount = 20
    while True:
        user_map_data = getusermap(userId, nextIndex, maxCount)
        if user_map_data != None:
            nextIndex = user_map_data['nextIndex']
            if user_map_data['userMapList'] == None:
                break
            for userMap in user_map_data['userMapList']:
                user_map_list.append(userMap)
            if nextIndex == 0:
                break
        else:
            break
    db.session.query(UserMap).filter_by(userId=userId).delete()
    for entry in user_map_list:
        um = UserMap(
            userId     = userId,
            mapId      = entry["mapId"],
            distance   = entry["distance"],
            isLock     = entry["isLock"],
            isClear    = entry["isClear"],
            isComplete = entry["isComplete"],
            unlockFlag = entry["unlockFlag"],
            updateTime = timestamp
        )
        db.session.add(um)
    db.session.commit()
    user_loginbonus_list = []
    nextIndex = 0
    maxCount = 20
    while True:
        user_loginbonus_data = getuserloginbonus(userId, nextIndex, maxCount)
        if user_loginbonus_data != None:
            nextIndex = user_loginbonus_data['nextIndex']
            # print(user_loginbonus_data)
            if user_loginbonus_data['userLoginBonusList'] == None:
                break
            for userLb in user_loginbonus_data['userLoginBonusList']:
                user_loginbonus_list.append(userLb)
            if nextIndex == 0:
                break
        else:
            break
    db.session.query(UserLoginBonus).filter_by(userId=userId).delete()
    for entry in user_loginbonus_list:
        ulb = UserLoginBonus(
            userId     = userId,
            bonusId    = entry["bonusId"],
            point      = entry["point"],
            isCurrent  = entry["isCurrent"],
            isComplete = entry["isComplete"],
            updateTime = timestamp
        )
        db.session.add(ulb)
    db.session.commit()
    data = json.dumps({
        "userId": int(userId)
    })
    useroption_data = json.loads(sdgb_api(data, "GetUserOptionApi", userId))
    if useroption_data != None:
        o = UserOption(
            userId               = useroption_data["userId"],
            optionKind           = useroption_data["userOption"]["optionKind"],
            noteSpeed            = useroption_data["userOption"]["noteSpeed"],
            slideSpeed           = useroption_data["userOption"]["slideSpeed"],
            touchSpeed           = useroption_data["userOption"]["touchSpeed"],
            noteSize             = useroption_data["userOption"]["noteSize"],
            slideSize            = useroption_data["userOption"]["slideSize"],
            touchSize            = useroption_data["userOption"]["touchSize"],
            tapDesign            = useroption_data["userOption"]["tapDesign"],
            holdDesign           = useroption_data["userOption"]["holdDesign"],
            slideDesign          = useroption_data["userOption"]["slideDesign"],
            starType             = useroption_data["userOption"]["starType"],
            starRotate           = useroption_data["userOption"]["starRotate"],
            adjustTiming         = useroption_data["userOption"]["adjustTiming"],
            judgeTiming          = useroption_data["userOption"]["judgeTiming"],
            mirrorMode           = useroption_data["userOption"]["mirrorMode"],
            ansVolume            = useroption_data["userOption"]["ansVolume"],
            tempoVolume          = useroption_data["userOption"]["tempoVolume"],
            tapHoldVolume        = useroption_data["userOption"]["tapHoldVolume"],
            touchHoldVolume      = useroption_data["userOption"]["touchHoldVolume"],
            breakVolume          = useroption_data["userOption"]["breakVolume"],
            exVolume             = useroption_data["userOption"]["exVolume"],
            slideVolume          = useroption_data["userOption"]["slideVolume"],
            breakSe              = useroption_data["userOption"]["breakSe"],
            slideSe              = useroption_data["userOption"]["slideSe"],
            exSe                 = useroption_data["userOption"]["exSe"],
            criticalSe           = useroption_data["userOption"]["criticalSe"],
            tapSe                = useroption_data["userOption"]["tapSe"],
            headPhoneVolume      = useroption_data["userOption"]["headPhoneVolume"],
            matching             = useroption_data["userOption"]["matching"],
            brightness           = useroption_data["userOption"]["brightness"],
            dispRate             = useroption_data["userOption"]["dispRate"],
            dispCenter           = useroption_data["userOption"]["dispCenter"],
            dispJudge            = useroption_data["userOption"]["dispJudge"],
            dispJudgePos         = useroption_data["userOption"]["dispJudgePos"],
            dispJudgeTouchPos    = useroption_data["userOption"]["dispJudgeTouchPos"],
            dispChain            = useroption_data["userOption"]["dispChain"],
            dispBar              = useroption_data["userOption"]["dispBar"],
            trackSkip            = useroption_data["userOption"]["trackSkip"],
            touchEffect          = useroption_data["userOption"]["touchEffect"],
            outlineDesign        = useroption_data["userOption"]["outlineDesign"],
            submonitorAnimation  = useroption_data["userOption"]["submonitorAnimation"],
            submonitorAppeal     = useroption_data["userOption"]["submonitorAppeal"],
            submonitorAchive     = useroption_data["userOption"]["submonitorAchive"],
            sortTab              = useroption_data["userOption"]["sortTab"],
            sortMusic            = useroption_data["userOption"]["sortMusic"],
            damageSeVolume       = useroption_data["userOption"]["damageSeVolume"],
            touchVolume          = useroption_data["userOption"]["touchVolume"],
            outFrameType         = useroption_data["userOption"]["outFrameType"],
            breakSlideVolume     = useroption_data["userOption"]["breakSlideVolume"],
            updateTime           = timestamp
        )
        db.session.merge(o)
        db.session.commit()
    user_music_list = []
    nextIndex = 0
    maxCount = 50
    while True:
        user_music_data = getusermusic(userId, nextIndex, maxCount)
        if user_music_data != None:
            nextIndex = user_music_data['nextIndex']
            if user_music_data['userMusicList'] == None:
                break
            for usermusicdetail in user_music_data['userMusicList']:
                for usermusic in usermusicdetail['userMusicDetailList']:
                    user_music_list.append(usermusic)
            if nextIndex == 0:
                break
        else:
            break
    db.session.query(UserMusic).filter_by(userId=userId).delete()
    for entry in user_music_list:
        um = UserMusic(
            userId        = userId,
            musicId       = entry["musicId"],
            level         = entry["level"],
            playCount     = entry["playCount"],
            achievement   = entry["achievement"],
            comboStatus   = entry["comboStatus"],
            syncStatus    = entry["syncStatus"],
            deluxscoreMax = entry["deluxscoreMax"],
            scoreRank     = entry["scoreRank"],
            extNum1       = entry["extNum1"],
            extNum2       = entry["extNum2"]
        )
        db.session.add(um)
    db.session.commit()
    for i in range(10):
        try:
            logout_data = logout(userId, timestamp)
            if logout_data["returnCode"] == 1:
                return jsonify({'stat': 1, 'msg': '更新用户数据完成。', 'data': logout_data, 'timestamp': timestamp})
        except:
            continue
    return jsonify({'stat': logout_data["returnCode"], 'msg': '登出失败，请手动逃离小黑屋。时间戳：'+str(timestamp), 'data': logout_data, 'timestamp': timestamp})
