from Constants import Constants


class Order:
    # 订单状态
    ORDER_HANGUP = 0            # 订单挂在市场，还未成交
    ORDER_RECEIVED = 1          # 订单已成交，还未完成
    ORDER_FIN = 2               # 订单已完成

    def __init__(self, order_id, owner: int, content, price: float):
        # 唯一标识号
        self.id = order_id
        # 订单所属工作台
        self.owner = owner
        # 订单执行人
        self.executor = -1
        # 订单内容: ('b', id) or ('s', id)
        self.content = content
        # 订单报价
        self.price = price
        # 订单状态
        self.status = Order.ORDER_HANGUP


class Market:
    def __init__(self):
        self.orders = []

    def create_order(self, owner, order_type, obj_id) -> Order:
        price = Constants.OBJECT_SELL_PRICE[obj_id - 1] if order_type == 's' else Constants.OBJECT_BUY_PRICE[obj_id - 1]
        new_order = Order(order_id=len(self.orders),
                          owner=owner,
                          content=(order_type, obj_id),
                          price=price)
        self.orders.append(new_order)
        return new_order

    def refresh(self, order_id: int):
        # 以原本的价格重新挂上订单
        order = self.orders[order_id]
        obj_id = order.content[1]
        order_type = order.content[0]
        price = Constants.OBJECT_SELL_PRICE[obj_id - 1] if order_type == 's' else Constants.OBJECT_BUY_PRICE[obj_id - 1]
        order.price = price
        order.status = Order.ORDER_HANGUP

