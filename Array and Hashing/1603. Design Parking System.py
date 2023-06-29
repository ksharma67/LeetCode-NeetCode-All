class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigTotal = big
        self.mediumTotal = medium
        self.smallTotal = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigTotal >= 1:
                self.bigTotal = self.bigTotal - 1
                return True
            else:
                return False
        
        elif carType == 2:
            if self.mediumTotal >= 1:
                self.mediumTotal = self.mediumTotal - 1
                return True
            else:
                return False
        elif carType == 3:
            if self.smallTotal >= 1:
                self.smallTotal = self.smallTotal - 1
                return True
            else:
                return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
