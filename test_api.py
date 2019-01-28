# -*- coding: utf-8 -*-

import unittest
import user_api
import config_params
from custom_error import CustomError
from user_api import get_market_id_by_name
import time

from ws_custom_client import WsCustomClient


class TestApiFunc(unittest.TestCase):
    # TODO:实际使用时请注意自行设置市场名
    test_market_name = 'ETH_USDT'
    # TODO:实际使用时请注意自行设置市场id
    test_market_id = '80'
    # TODO:实际使用时请注意自行设置币种名
    test_currency_name = 'ETH'
    is_use_market_name = True

    def test_get_userinfo(self):
        status, result = user_api.get_userinfo()
        print('\n' + 'test_get_userinfo:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_market_list(self):
        status, result = user_api.get_market_list()
        print('\n' + 'test_get_market_list:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_currency_list(self):
        status, result = user_api.get_currency_list()
        print('\n' + 'test_get_currency_list:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_add_entrust(self):
        amount = '1.1'
        price = '10'
        entrust_type = 0
        # TODO:测试此接口时注意先调好价格和数量，避免失误下单  ，参数type买卖类型：0 卖出 1 购买
        # status, result = user_api.add_entrust(TestApiFunc.test_market_name, amount, price, 0, entrust_type)
        # print('\n' + 'test_add_entrust:')
        # print(result)
        # assert '1' == result['resMsg']['code']

    def test_cancle_entrust(self):
        # TODO:设置还没完成的订单id才能跑通
        entrust_id = 'E6440XXXXX'
        status, result = user_api.cancle_entrust(TestApiFunc.test_market_name, entrust_id)
        print('\n' + 'test_cancle_entrust:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_entrust_by_id(self):
        entrust_id = 'E6439XXX'
        status, result = user_api.get_entrust_by_id(TestApiFunc.test_market_name, entrust_id)
        print('\n' + 'test_get_entrust_by_id:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_user_entrust_from_cache_with_page(self):
        status, result = user_api.get_user_entrust_from_cache_with_page(TestApiFunc.test_market_name, 1, 5)
        print('\n' + 'test_get_user_entrust_from_cache_with_page:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_user_entrust_from_cache(self):
        status, result = user_api.get_user_entrust_from_cache(TestApiFunc.test_market_name)
        print('\n' + 'test_get_user_entrust_from_cache:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_user_entrust_list(self):
        type_param = None
        status_param = None
        start_date_time = None
        end_date_time = None

        # 可选参数自行选择
        # （可选）委托类型，0 卖出 1 购买  -1 取消
        # type_param = 0
        # （可选）状态 : -2资金解冻失败 -1用户资金不足 0起始 1取消 2交易成功 3交易一部
        # status_param = 1
        # （可选）委托下单的起始时间，13位时间戳
        # start_date_time = 1548225569699
        # （可选）委托下单的结束时间，13位时间戳
        # end_date_time = 1548225569699

        status, result = user_api.get_user_entrust_list(TestApiFunc.test_market_name, 1, 20, type_param, status_param,
                                                        start_date_time, end_date_time)
        print('\n' + 'test_get_user_entrust_list:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_payin_address(self):
        status, result = user_api.get_payin_address(TestApiFunc.test_currency_name)
        print('\n' + 'test_get_payin_address:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_payin_coin_record(self):
        status, result = user_api.get_payin_coin_record(TestApiFunc.test_currency_name, 1, 20)
        print('\n' + 'test_get_payin_coin_record:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_withdraw_address(self):
        status, result = user_api.get_withdraw_address(TestApiFunc.test_currency_name, 1, 10)
        print('\n' + 'test_get_withdraw_address:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_payout_coin_record(self):
        status, result = user_api.get_payin_coin_record(TestApiFunc.test_currency_name, 1, 20)
        print('\n' + 'test_get_payout_coin_record:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_fund_findbypage(self):
        status, result = user_api.fund_finbypage(1, 999)
        print('\n' + 'test_fund_findbypage:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_tickers(self):
        status, result = user_api.get_tickers(TestApiFunc.is_use_market_name)
        print('\n' + 'test_get_tickers:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_ticker(self):
        if TestApiFunc.is_use_market_name:
            status, result = user_api.get_ticker(None, TestApiFunc.test_market_name)
        else:
            status, result = user_api.get_ticker(TestApiFunc.test_market_id, None)
        print('\n' + 'test_get_ticker:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_klines(self):
        if TestApiFunc.is_use_market_name:
            status, result = user_api.get_klines(None, TestApiFunc.test_market_name, 2, '1M')
        else:
            status, result = user_api.get_klines(TestApiFunc.test_market_id, None, 2, '1M')
        print('\n' + 'test_get_klines:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_trades(self):
        if TestApiFunc.is_use_market_name:
            status, result = user_api.get_trades(None, TestApiFunc.test_market_name, 20)
        else:
            status, result = user_api.get_trades(TestApiFunc.test_market_id, None, 20)
        print('\n' + 'test_get_trades:')
        print(result)
        assert '1' == result['resMsg']['code']

    def test_get_entrusts(self):
        if TestApiFunc.is_use_market_name:
            status, result = user_api.get_entrusts(None, TestApiFunc.test_market_name, 20)
        else:
            status, result = user_api.get_entrusts(TestApiFunc.test_market_id, None, 20)
        print('\n' + 'test_get_entrusts:')
        print(result)
        assert '1' == result['resMsg']['code']

        # websocket接口的测试代码

    def test_websocket_data(self):
        print('\n' + 'test_websocket_data:')
        market_id = get_market_id_by_name(TestApiFunc.test_market_name)
        if not market_id:
            raise CustomError('市场不存在')
        ws = WsCustomClient(config_params.KLINE_WS_HOST + config_params.WEBSOCKET_PATH, market_id,
                            TestApiFunc.test_market_name)
        ws.connect()
        time.sleep(5)
        # 这里提供最简单的websocket保持连接实现，建议用户根据项目实际需要自行优化
        # while True:
        i = 1
        while i < 10:
            if not ws.is_ws_connect:
                print('连接已断开，重新连接')
                ws.connect()
            time.sleep(1)
            i = i + 1
        ws.close(reason='test')


if __name__ == '__main__':
    unittest.main()
