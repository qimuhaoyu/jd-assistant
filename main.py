#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    sku_ids = '100012117649'  # 商品id
    area = '22_1930_50948_52157'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
