class priceData:
    def __init__(self, prices):
        self.__prices = prices
        self.__acceleration = 0.0
        self.__velocity = 0.0
        self.__accelerationMap = {}
        self.__veloctiyMap = {}
        self.__high = 0.0
        self.__low = 0.0
    
    def calcAcceleration(self, timestep):
        #self.__acceleration = self.__prices[timestep] ACCELERATION CALC MATH HERE
        #self.__insertAcceleration(timestep)
    
    def __insertAcceleration(self, timestep):
        #self.__accelerationMap[timestep] = self.acceleration
    
    def calcVelocity(self, timestep):
        #self.__velocity = self.__prices[timestep] VELOCITY CALC MATH HERE
        #self.__insertVelocity(timestep)
    
    def __insertVelocity(self,timestep):
        #self.__velocityMap[timestep] = self.velocity
    
    def setHigh(self,high):
        self.__high = high
    
    def setLow(self, low):
        self.__low = low
    