class portfolio:
    def __init__(self, inital_cash):
        self.cash = inital_cash
        self.current_capital = inital_cash
        self.positions = {} #Holds position objects
    
    def reset(self):
        self.positions.clear()
    
    def position_entered(self, position, order):
        self.positions.append(position)
        self.cash -= position.price + position.commission
    
    def postion_exited(self, price, commission):
        ##########
