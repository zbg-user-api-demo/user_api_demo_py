# -*- coding: utf-8 -*-

from ws4py.client.threadedclient import WebSocketClient


class WsCustomClient(WebSocketClient):
    def __init__(self, url, market_id_param, market_name_param):
        super(WsCustomClient, self).__init__(url)
        self.market_id = market_id_param
        self.market_name = market_name_param
        self.entrust_data = {'asks': [], 'bids': [], 'ts': 0}
        self.is_ws_connect = False

    def opened(self):
        self.is_ws_connect = True
        self.subscribe()

    def subscribe(self):
        # TODO:一般而言，API用户只需要用到entrust类型的数据，其他三类数据如果需要请自行取消代码注释
        # 订阅盘口数据，其他的数据请参考修改
        entrust_data_type = '{}_ENTRUST_ADD_{}'.format(self.market_id, self.market_name)
        self.send('{"dataType":%s,"dataSize":50,"action":"ADD"}' % entrust_data_type)
        # # 订阅k线数据，1小时线
        # kline_data_type = '{}_KLINE_{}_{}'.format(self.market_id, '1H', self.market_name)
        # self.send('{"dataType":%s,"dataSize":500,"action":"ADD"}' % kline_data_type)
        # # 订阅交易记录数据
        # trade_data_type = '{}_TRADE_{}'.format(self.market_id, self.market_name)
        # self.send('{"dataType":%s,"dataSize":20,"action":"ADD"}' % trade_data_type)
        # # 订阅单个市场的行情数据
        # self.send('{"dataType":"%s_TRADE_STATISTIC_24H","dataSize":1,"action":"ADD"}' % self.market_id)
        # # 订阅所有市场的行情数据
        # self.send('{"dataType":"ALL_TRADE_STATISTIC_24H","dataSize":1,"action":"ADD"}')

    def closed(self, code, reason=None):
        self.is_ws_connect = False
        print("Closed down", code, reason)

    def received_message(self, m):
        print('接收到websocket消息')
        print(m)
        data = eval(str(m).replace('“', '"').replace('”', '"'))
        try:
            if 'trade_statistic' in data:
                # 有需要可以自行加入 trade_statistic 类型数据的处理
                test_data = data['trade_statistic']
            elif data[0] != 'E' and data[0][0] == 'AE':
                self.entrust_data['asks'] = data[0][4]['asks']
                self.entrust_data['bids'] = data[0][5]['bids']
                self.entrust_data['ts'] = data[0][3]
                data = self.entrust_data
            elif data[0] == 'E':
                self.entrust_data['ts'] = data[2]
                self.update_data(data)
                data = self.entrust_data
            # print('更新后盘口数据...data:%s' % data)
        except Exception as err:
            print('数据准备中...data:%s' % data)
            print(err)
        # print('data:%s'%self.depth_data['asks'][-1][0])

    def update_data(self, data):
        side = data[4].lower() + 's'
        for i in range(len(self.entrust_data[side])):
            if self.entrust_data[side][i][0] == data[5]:
                if data[6] != '0':
                    self.entrust_data[side][i][1] = data[6]
                else:
                    # 数量为0的档位必须删除
                    self.entrust_data[side].pop(i)
                return
            elif float(data[5]) > float(self.entrust_data[side][i][0]) and data[6] != '0':
                self.entrust_data[side].insert(i, [data[5], data[6]])
                return
        if data[6] != '0':
            self.entrust_data[side].append([data[5], data[6]])
