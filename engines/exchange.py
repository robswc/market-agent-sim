class Exchange(object):
    def __init__(self):
        self.bids = []
        self.asks = []



    def order(self, side, ord_type, qty):
        if ord_type == 'limit':
            if side == 'buy':
                self.bids.append(qty)
            if side == 'sell':
                self.asks.append(qty)
