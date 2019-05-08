import portfolio
import position

class order_manager:
    def __init__(self):
        ORDER_OK = False

def long_order(self,portfolio, position):
    if portfolio.cash > (position.price + position.commission):
        return True