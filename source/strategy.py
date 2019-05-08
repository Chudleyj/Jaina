class strategy:
    def __init__(self, priceData):
        self.__symbols = []
        self.__capital = 0.0
        self.__active = False
        self.priceData = priceData
        
    def set_capital(self, capital):
        self.__capital = capital
    
    def set_symbols(self, symbols):
        self.__symbols = symbols

    def activate(self):
        self.__active = True