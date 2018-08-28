# -*- coding: utf-8 -*-
# TODO:域名地址请获取文档的域名来配置
EXCHANGE_HOST = "http://192.168.20.13:9000"
KLINE_WS_HOST = "ws://192.168.20.13:28080"
KLINE_HTTP_HOST = KLINE_WS_HOST.replace("wss", "https").replace("ws", "http")

WEBSOCKET_PATH = "/websocket"

# TODO:API_ID和API_SECRET请自行设置
# 测试环境id
API_ID = "7eOiWtBG56e7eOiWtBG56f"
API_SECRET = "91ab5ef791cfe92fdb849869ab011cee"

# url获取用户信息
API_USER_INFO = "/exchange/user/controller/website/usercontroller/getuserinfo"

# url查询market
API_GET_MARKET_LIST = "/exchange/config/controller/website/marketcontroller/getByWebId"

# url获取资金列表
API_GET_CURRENCY_LIST = "/exchange/config/controller/website/currencycontroller/getCurrencyList"

# url新增委托
API_ADD_ENTRUST = "/exchange/entrust/controller/website/EntrustController/addEntrust"

# url取消委托
API_CANCEL_ENTRUST = "/exchange/entrust/controller/website/EntrustController/cancelEntrust"

# url 根据委托单ID查询委托单信息
API_USER_ENTRUST_BY_ID = "/exchange/entrust/controller/website/EntrustController/getEntrustById"

# url 分页获取用户的委托记录
API_GET_USER_ENTRUST_LIST = "/exchange/entrust/controller/website/EntrustController/getUserEntrustList"

# url从缓存中获取用户还未成交的委托记录
API_GET_USER_ENTRUST_FROM_CACHE = "/exchange/entrust/controller/website/EntrustController/getUserEntrustRecordFromCache"

# url获取充币地址
API_PAYIN_ADDRESS = "/exchange/fund/controller/website/fundcontroller/getPayinAddress"

# url查询充币记录
API_PAYIN_CION_RECORD = "/exchange/fund/controller/website/fundcontroller/getPayinCoinRecord"

# url查询提币记录
API_PAYOUT_CION_RECORD = "/exchange/fund/controller/website/fundwebsitecontroller/getpayoutcoinrecord"

# url获取用户所有资金信息
API_FUND_FIND_BY_PAGE = "/exchange/fund/controller/website/fundcontroller/findbypage"

# url查询提币地址
API_FUND_WITHDRAW_ADDRESS = "/exchange/fund/controller/website/fundwebsitecontroller/getwithdrawaddress"

# url查询所有市场行情
API_GET_TICKERS = "/api/data/v1/tickers"

# url查询单个市场行情
API_GET_TICKER = "/api/data/v1/ticker"

# url查询k线列表
API_GET_KILNES = "/api/data/v1/klines"

# url查询交易记录
API_GET_TRADES = "/api/data/v1/trades"

# url获取盘口（市场深度）
API_GET_ENTRUSTS = "/api/data/v1/entrusts"
