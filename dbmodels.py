# dbmodels.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # 先在这里创建 db 实例

class Card(db.Model):
    """ 
        缓存 FeliCa 卡片的 IDm 和 AccessCode 映射信息，仅需要 Aime 卡的服务器可用，
        原始数据记载于 AimeDB 
    """
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    IDm = db.Column(db.String(17), unique=True, nullable=False)
    PMm = db.Column(db.String(17), unique=False, nullable=False)
    accessCode = db.Column(db.String(21), nullable=True)
    updateTime = db.Column(db.BigInteger, nullable=True)

class User(db.Model):
    """ 用户基础信息表，完整内容记载于 GetUserDataApi 接口 """
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(9), nullable=True)
    accessCode = db.Column(db.String(21), nullable=True)
    friendCode = db.Column(db.String(16), nullable=True)
    isNetMember = db.Column(db.SmallInteger, nullable=True)
    playerRating = db.Column(db.Integer, nullable=True)
    playerOldRating = db.Column(db.Integer, nullable=True)
    playerNewRating = db.Column(db.Integer, nullable=True)
    highestRating = db.Column(db.Integer, nullable=True)
    gradeRating = db.Column(db.Integer, nullable=True)
    musicRating = db.Column(db.Integer, nullable=True)
    gradeRank = db.Column(db.Integer, nullable=True)
    courseRank = db.Column(db.Integer, nullable=True)
    classRank = db.Column(db.Integer, nullable=True)
    nameplateId = db.Column(db.Integer, nullable=True)
    frameId = db.Column(db.Integer, nullable=True)
    iconId = db.Column(db.Integer, nullable=True)
    trophyId = db.Column(db.Integer, nullable=True)
    plateId = db.Column(db.Integer, nullable=True)
    titleId = db.Column(db.Integer, nullable=True)
    partnerId = db.Column(db.Integer, nullable=True)
    charaSlot = db.Column(db.JSON, nullable=True)
    charaLockSlot = db.Column(db.JSON, nullable=True)
    contentBit = db.Column(db.Integer, nullable=True)
    selectMapId = db.Column(db.Integer, nullable=True)
    playCount = db.Column(db.Integer, nullable=True)
    currentPlayCount = db.Column(db.Integer, nullable=True)
    playVsCount = db.Column(db.Integer, nullable=True)
    playSyncCount = db.Column(db.Integer, nullable=True)
    winCount = db.Column(db.Integer, nullable=True)
    helpCount = db.Column(db.Integer, nullable=True)
    comboCount = db.Column(db.Integer, nullable=True)
    totalDeluxscore = db.Column(db.Integer, nullable=True)
    totalBasicDeluxscore = db.Column(db.Integer, nullable=True)
    totalAdvancedDeluxscore = db.Column(db.Integer, nullable=True)
    totalExpertDeluxscore = db.Column(db.Integer, nullable=True)
    totalMasterDeluxscore = db.Column(db.Integer, nullable=True)
    totalReMasterDeluxscore = db.Column(db.Integer, nullable=True)
    totalSync = db.Column(db.Integer, nullable=True)
    totalBasicSync = db.Column(db.Integer, nullable=True)
    totalAdvancedSync = db.Column(db.Integer, nullable=True)
    totalExpertSync = db.Column(db.Integer, nullable=True)
    totalMasterSync = db.Column(db.Integer, nullable=True)
    totalReMasterSync = db.Column(db.Integer, nullable=True)
    totalAchievement = db.Column(db.Integer, nullable=True)
    totalBasicAchievement = db.Column(db.Integer, nullable=True)
    totalAdvancedAchievement = db.Column(db.Integer, nullable=True)
    totalExpertAchievement = db.Column(db.Integer, nullable=True)
    totalMasterAchievement = db.Column(db.Integer, nullable=True)
    totalReMasterAchievement = db.Column(db.Integer, nullable=True)
    eventWatchedDate = db.Column(db.String(20), nullable=True)
    lastGameId = db.Column(db.String(10), nullable=True)
    lastRomVersion = db.Column(db.String(10), nullable=True)
    lastDataVersion = db.Column(db.String(10), nullable=True)
    lastLoginDate = db.Column(db.String(20), nullable=True)
    lastPlayDate = db.Column(db.String(20), nullable=True)
    lastPairLoginDate = db.Column(db.String(20), nullable=True)
    lastTrialPlayDate = db.Column(db.String(20), nullable=True)
    lastPlayCredit = db.Column(db.Integer, nullable=True)
    lastPlayMode = db.Column(db.Integer, nullable=True)
    lastPlaceId = db.Column(db.Integer, nullable=True)
    lastPlaceName = db.Column(db.String(100), nullable=True)
    lastAllNetId = db.Column(db.Integer, nullable=True)
    lastRegionId = db.Column(db.Integer, nullable=True)
    lastRegionName = db.Column(db.String(20), nullable=True)
    lastClientId = db.Column(db.String(20), nullable=True)
    lastCountryCode = db.Column(db.String(5), nullable=True)
    lastSelectEMoney = db.Column(db.Integer, nullable=True)
    lastSelectTicket = db.Column(db.Integer, nullable=True)
    lastSelectCourse = db.Column(db.Integer, nullable=True)
    lastCountCourse = db.Column(db.Integer, nullable=True)
    firstGameId = db.Column(db.String(10), nullable=True)
    firstRomVersion = db.Column(db.String(10), nullable=True)
    firstDataVersion = db.Column(db.String(10), nullable=True)
    firstPlayDate = db.Column(db.String(20), nullable=True)
    compatibleCmVersion = db.Column(db.String(10), nullable=True)
    totalAwake = db.Column(db.Integer, nullable=True)
    dailyBonusDate = db.Column(db.String(20), nullable=True)
    dailyCourseBonusDate = db.Column(db.String(20), nullable=True)
    mapStock = db.Column(db.Integer, nullable=True)
    renameCredit = db.Column(db.Integer, nullable=True)
    cmLastEmoneyCredit = db.Column(db.Integer, nullable=True)
    cmLastEmoneyBrand = db.Column(db.Integer, nullable=True)
    dateTime = db.Column(db.String(20), nullable=True)
    banState = db.Column(db.SmallInteger, nullable=True)
    updateTime = db.Column(db.BigInteger, nullable=True)

# class UserCard(db.Model):
#     # 应该是DX Pass的存储内容，对应api GetUserCardApiMaimaiChn 由于国服返回空值，现在先不写了
#     __tablename__ = 'userCard'
#     userId = db.Column(db.Integer, primary_key=True)

class UserCharacter(db.Model):
    """ 用户旅行伙伴信息表，完整内容记载于 GetUserCharacterApi 接口 """
    __tablename__ = 'userCharacter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    characterId = db.Column(db.Integer, nullable=False)
    point = db.Column(db.Integer, nullable=False)
    useCount = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    nextAwake = db.Column(db.Integer, nullable=False)
    nextAwakePercent = db.Column(db.Integer, nullable=False)
    awakening = db.Column(db.Integer, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

class UserItem(db.Model):
    """ 用户收藏品信息表，内容分段记载于 GetUserItemApi 接口 """
    __tablename__ = 'userItem'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    itemKind = db.Column(db.Integer, nullable=False)
    itemId = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    isValid = db.Column(db.Boolean, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

class UserCourse(db.Model):
    """ 用户段位认定信息表，完整内容记载于 GetUserCourseApi 接口 """
    __tablename__ = 'userCourse'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    courseId = db.Column(db.Integer, nullable=False)
    isLastClear = db.Column(db.Boolean, nullable=False)
    totalRestlife = db.Column(db.Integer, nullable=False)
    totalAchievement = db.Column(db.Integer, nullable=False)
    totalDeluxscore = db.Column(db.Integer, nullable=False)
    bestAchievement = db.Column(db.Integer, nullable=False)
    bestDeluxscore = db.Column(db.Integer, nullable=False)
    bestAchievementDate = db.Column(db.String(20), nullable=False)
    bestDeluxscoreDate = db.Column(db.String(20), nullable=False)
    playCount = db.Column(db.Integer, nullable=False)
    clearDate = db.Column(db.String(20), nullable=False)
    lastPlayDate = db.Column(db.String(20), nullable=False)
    extNum1 = db.Column(db.Integer, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

# class UserFavorite(db.Model):
#     """ 用户喜爱的收藏品信息表，内容分段记载于 GetUserFavoriteApi 接口 """
#     __tablename__ = 'userFavorite'
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, nullable=False)
#     # TODO: 待完善

# class UserGhost(db.Model):
#     """ 用户？？？信息表，完整内容记载于 GetUserGhostApi 接口 """
#     __tablename__ = 'userGhost'
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, nullable=False)
#     # TODO: 待完善

class UserMap(db.Model):
    """ 用户跑图区域信息表，内容分段记载于 GetUserMapApi 接口 """
    __tablename__ = 'userMap'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    mapId = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    isLock = db.Column(db.Boolean, nullable=False)
    isClear = db.Column(db.Boolean, nullable=False)
    isComplete = db.Column(db.Boolean, nullable=False)
    unlockFlag = db.Column(db.SmallInteger, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

class UserLoginBonus(db.Model):
    """ 用户登录奖励信息表，内容分段记载于 GetUserLoginBonusApi 接口 """
    __tablename__ = 'userLoginBonus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    bonusId = db.Column(db.Integer, nullable=False)
    point = db.Column(db.Integer, nullable=False)
    isCurrent = db.Column(db.Boolean, nullable=False)
    isComplete = db.Column(db.Boolean, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

class UserOption(db.Model):
    """ 用户设置信息表，完整内容记载于 GetUserOptionApi 接口 """
    __tablename__ = 'userOption'
    userId = db.Column(db.Integer, primary_key=True)
    optionKind = db.Column(db.SmallInteger, nullable=False)
    noteSpeed = db.Column(db.SmallInteger, nullable=False)
    slideSpeed = db.Column(db.SmallInteger, nullable=False)
    touchSpeed = db.Column(db.SmallInteger, nullable=False)
    noteSize = db.Column(db.SmallInteger, nullable=False)
    slideSize = db.Column(db.SmallInteger, nullable=False)
    touchSize = db.Column(db.SmallInteger, nullable=False)
    tapDesign = db.Column(db.SmallInteger, nullable=False)
    holdDesign = db.Column(db.SmallInteger, nullable=False)
    slideDesign = db.Column(db.SmallInteger, nullable=False)
    starType = db.Column(db.SmallInteger, nullable=False)
    starRotate = db.Column(db.SmallInteger, nullable=False)
    adjustTiming = db.Column(db.SmallInteger, nullable=False)
    judgeTiming = db.Column(db.SmallInteger, nullable=False)
    mirrorMode = db.Column(db.SmallInteger, nullable=False)
    ansVolume = db.Column(db.SmallInteger, nullable=False)
    tempoVolume = db.Column(db.SmallInteger, nullable=False)
    tapHoldVolume = db.Column(db.SmallInteger, nullable=False)
    touchHoldVolume = db.Column(db.SmallInteger, nullable=False)
    breakVolume = db.Column(db.SmallInteger, nullable=False)
    exVolume = db.Column(db.SmallInteger, nullable=False)
    slideVolume = db.Column(db.SmallInteger, nullable=False)
    breakSe = db.Column(db.SmallInteger, nullable=False)
    slideSe = db.Column(db.SmallInteger, nullable=False)
    exSe = db.Column(db.SmallInteger, nullable=False)
    criticalSe = db.Column(db.SmallInteger, nullable=False)
    tapSe = db.Column(db.SmallInteger, nullable=False)
    headPhoneVolume = db.Column(db.SmallInteger, nullable=False)
    matching = db.Column(db.SmallInteger, nullable=False)
    brightness = db.Column(db.SmallInteger, nullable=False)
    dispRate = db.Column(db.SmallInteger, nullable=False)
    dispCenter = db.Column(db.SmallInteger, nullable=False)
    dispJudge = db.Column(db.SmallInteger, nullable=False)
    dispJudgePos = db.Column(db.SmallInteger, nullable=False)
    dispJudgeTouchPos = db.Column(db.SmallInteger, nullable=False)
    dispChain = db.Column(db.SmallInteger, nullable=False)
    dispBar = db.Column(db.SmallInteger, nullable=False)
    trackSkip = db.Column(db.SmallInteger, nullable=False)
    touchEffect = db.Column(db.SmallInteger, nullable=False)
    outlineDesign = db.Column(db.SmallInteger, nullable=False)
    submonitorAnimation = db.Column(db.SmallInteger, nullable=False)
    submonitorAppeal = db.Column(db.SmallInteger, nullable=False)
    submonitorAchive = db.Column(db.SmallInteger, nullable=False)
    sortTab = db.Column(db.SmallInteger, nullable=False)
    sortMusic = db.Column(db.SmallInteger, nullable=False)
    damageSeVolume = db.Column(db.SmallInteger, nullable=False)
    touchVolume = db.Column(db.SmallInteger, nullable=False)
    outFrameType = db.Column(db.SmallInteger, nullable=False)
    breakSlideVolume = db.Column(db.SmallInteger, nullable=False)
    updateTime = db.Column(db.BigInteger, nullable=True)

class UserMusic(db.Model):
    """ 用户歌曲最佳成绩信息表，内容分段记载于 GetUserMusicApi 接口 """
    __tablename__ = 'userMusic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, nullable=False)
    musicId = db.Column(db.Integer, nullable=False)
    level = db.Column(db.SmallInteger, nullable=False)
    playCount = db.Column(db.Integer, nullable=False)
    achievement = db.Column(db.Integer, nullable=False)
    comboStatus = db.Column(db.SmallInteger, nullable=False)
    syncStatus = db.Column(db.SmallInteger, nullable=False)
    deluxscoreMax = db.Column(db.Integer, nullable=False)
    scoreRank = db.Column(db.Integer, nullable=False)
    extNum1 = db.Column(db.Integer, nullable=False)
    extNum2 = db.Column(db.Integer, nullable=False)