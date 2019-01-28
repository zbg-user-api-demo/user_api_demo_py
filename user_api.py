import config_params
from http_utils import *
from custom_error import CustomError

__market_list = {}
__currency_list = {}


# 根据市场的名字获取市场id
def get_market_id_by_name(market_name):
    if not __market_list or market_name not in __market_list:
        __init_market_cache()
    # print('__market_list=' + __market_list.__str__())
    if market_name in __market_list:
        market = __market_list[market_name]
        market_id = market['marketId']
        return market_id
    return None


# 初始化市场列表缓存
def __init_market_cache():
    # global __market_list
    status, result = get_market_list()
    # 根据返回结果解释出market列表
    if status:
        data = result['datas']
        for mk in data:
            name = mk['name'].upper()
            __market_list[name] = mk
    else:
        raise CustomError('初始化市场列表缓存失败，无法获取市场列表数据' + result)


# 根据市场的名字获取市场id
def get_currency_id_by_name(currency_name):
    if not __currency_list or currency_name not in __currency_list:
        __init_currency_cache()
    if currency_name in __currency_list:
        currency = __currency_list[currency_name]
        currency_id = currency['currencyId']
        return currency_id
    return None


# 初始化币种列表缓存
def __init_currency_cache():
    status, result = get_currency_list()
    # 根据返回结果解释出market列表
    if status:
        data = result['datas']
        for currency in data:
            name = currency['name'].upper()
            __currency_list[name] = currency
    else:
        raise CustomError('初始化币种列表缓存失败，无法获取市场列表数据' + result)


# 获取用户信息
def get_userinfo():
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_USER_INFO)
    return status, result


# 获取市场列表
def get_market_list():
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_GET_MARKET_LIST)
    return status, result


# 获取比币种列表
def get_currency_list():
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_GET_CURRENCY_LIST)
    return status, result


# 增加委托单，也就是下单接口
def add_entrust(market_name, amount, price, range_type, entrust_type):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id, 'amount': amount, 'price': price, 'rangeType': range_type, 'type': entrust_type}
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_ADD_ENTRUST, **params)
    return status, result


# 取消委托单接口
def cancle_entrust(market_name, entrust_id):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id, 'entrustId': entrust_id}
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_CANCEL_ENTRUST, **params)
    return status, result


# 根据id获取委托单信息
def get_entrust_by_id(market_name, entrust_id):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id, 'entrustId': entrust_id}
    status, result = signed_request_get(config_params.EXCHANGE_HOST + config_params.API_USER_ENTRUST_BY_ID, **params)
    return status, result


# 获取用户待撮合、委托记录
def get_user_entrust_from_cache_with_page(market_name, page_index, page_size):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id, 'pageIndex': page_index, 'pageSize': page_size}
    status, result = signed_request_get(config_params.EXCHANGE_HOST
                                        + config_params.API_GET_USER_ENTRUST_FROM_CACHE_WITH_PAGE, **params)
    return status, result


# 获取用户待撮合、委托记录
def get_user_entrust_from_cache(market_name):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id}
    status, result = signed_request_get(config_params.EXCHANGE_HOST
                                        + config_params.API_GET_USER_ENTRUST_FROM_CACHE, **params)
    return status, result


# 获取用户待撮合、已成交、部分成交、已取消、取消中的委托记录
def get_user_entrust_list(market_name, page_index, page_size, type_param, status_param, start_date_time, end_date_time):
    market_id = get_market_id_by_name(market_name)
    if not market_id:
        raise CustomError(market_name + '市场不存在')
    params = {'marketId': market_id, 'pageIndex': page_index, 'pageSize': page_size}
    if type_param is not None:
        params['type'] = type_param
    if status_param is not None:
        params['status'] = status_param
    if start_date_time is not None:
        params['startDateTime'] = start_date_time
    if end_date_time is not None:
        params['endDateTime'] = end_date_time
    status, result = signed_request_get(config_params.EXCHANGE_HOST + config_params.API_GET_USER_ENTRUST_LIST,
                                        **params)
    return status, result


# 获取充值地址
def get_payin_address(currency_type_name):
    params = {'currencyTypeName': currency_type_name}
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_PAYIN_ADDRESS,
                                         **params)
    return status, result


# 获取充值记录
def get_payin_coin_record(currency_type_name, page_num, page_size):
    params = {'currencyTypeName': currency_type_name, 'paegNum': page_num, 'pageSize': page_size}
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_PAYIN_CION_RECORD,
                                         **params)
    return status, result


# 获取提现地址,currency_name 币种名称如ETH
def get_withdraw_address(currency_name, page_num, page_size):
    currency_id = get_currency_id_by_name(currency_name)
    if not currency_id:
        raise CustomError(currency_name + '币种不存在')
    params = {'currencyId': currency_id, 'paegNum': page_num, 'pageSize': page_size}
    status, result = signed_request_get(config_params.EXCHANGE_HOST + config_params.API_FUND_WITHDRAW_ADDRESS,
                                        **params)
    return status, result


# 获取提现记录,currency_name 币种名称如ETH,tal  all(所有), wait(已提交，未审核), success(审核通过), fail(审核失败), cancel(用户主动取消)
def get_payout_coin_record(currency_name, tal, page_num, page_size):
    currency_id = get_currency_id_by_name(currency_name)
    if not currency_id:
        raise CustomError(currency_name + '币种不存在')
    params = {'currencyId': currency_id, 'tal': tal, 'paegNum': page_num, 'pageSize': page_size}
    status, result = signed_request_get(config_params.EXCHANGE_HOST + config_params.API_PAYOUT_CION_RECORD,
                                        **params)
    return status, result


# 获取资金列表
def fund_finbypage(page_num, page_size):
    params = {'pageNum': page_num, 'pageSize': page_size}
    status, result = signed_request_post(config_params.EXCHANGE_HOST + config_params.API_FUND_FIND_BY_PAGE, **params)
    return status, result


# 获取所有市场的行情信息
def get_tickers(is_use_market_name):
    params = {'isUseMarketName': is_use_market_name}
    status, result = public_request_get(config_params.KLINE_HTTP_HOST + config_params.API_GET_TICKERS, **params)
    return status, result


# 获取单个市场的行情信息,市场id和名字传一个即可
def get_ticker(market_id, market_name):
    if market_id:
        params = {'marketId': market_id}
    else:
        params = {'marketName': market_name}
    status, result = public_request_get(config_params.KLINE_HTTP_HOST + config_params.API_GET_TICKER, **params)
    return status, result


# 获取k线列表,市场id和名字传一个即可
def get_klines(market_id, market_name, data_size, kline_type):
    if market_id:
        params = {'marketId': market_id, "dataSize": data_size, "type": kline_type}
    else:
        params = {'marketName': market_name, "dataSize": data_size, "type": kline_type}
    status, result = public_request_get(config_params.KLINE_HTTP_HOST + config_params.API_GET_KILNES, **params)
    return status, result


# 获取成交列表,市场id和名字传一个即可
def get_trades(market_id, market_name, data_size):
    if market_id:
        params = {'marketId': market_id, "dataSize": data_size}
    else:
        params = {'marketName': market_name, "dataSize": data_size}
    status, result = public_request_get(config_params.KLINE_HTTP_HOST + config_params.API_GET_TRADES, **params)
    return status, result


# 获取市场盘口列表,市场id和名字传一个即可
def get_entrusts(market_id, market_name, data_size):
    if market_id:
        params = {'marketId': market_id, "dataSize": data_size}
    else:
        params = {'marketName': market_name, "dataSize": data_size}
    status, result = public_request_get(config_params.KLINE_HTTP_HOST + config_params.API_GET_ENTRUSTS, **params)
    return status, result
