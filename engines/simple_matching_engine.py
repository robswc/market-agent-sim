class SimpleEngine(object):
    def __init__(self):
        self.price = 100

    def add_order(self, order):
        if order.get('side') == 'buy':
            self.market_buy(order['qty'])
        if order.get('side') == 'sell':
            self.market_sell(order['qty'])

    def market_buy(self, qty):
        self.price = self.price + qty

    def market_sell(self, qty):
        self.price = self.price - qty

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
