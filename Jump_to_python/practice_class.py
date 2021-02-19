class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second =  second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result =  self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(9,2)
print(a.first)
print(a.second)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(9,2)
print(b.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(4,0)
print(c.div())

class Family:
    lastname = "suh"
print(Family.lastname)
