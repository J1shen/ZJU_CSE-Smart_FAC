class Constants:
    # 注： 此处SELL与BUY均针对工作台而言
    OBJECT_SELL_PRICE = [3000, 4400, 5800, 15400, 17200, 19200, 76000]
    OBJECT_BUY_PRICE = [6000, 7600, 9200, 22500, 25000, 27500, 105000]
    # 工作台
    TABLE_1 = [('s', 1)]
    TABLE_2 = [('s', 2)]
    TABLE_3 = [('s', 3)]
    TABLE_4 = [('b', 1), ('b', 2), ('s', 4)]
    TABLE_5 = [('b', 1), ('b', 3), ('s', 5)]
    TABLE_6 = [('b', 2), ('b', 3), ('s', 6)]
    TABLE_7 = [('b', 4), ('b', 5), ('b', 6), ('s', 7)]
    TABLE_8 = [('b', 7)]
    TABLE_9 = [('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7)]
    TABLE_ALL = [TABLE_1, TABLE_2, TABLE_3, TABLE_4, TABLE_5, TABLE_6, TABLE_7, TABLE_8, TABLE_9]