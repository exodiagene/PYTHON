from math import*


class Addition:
    FirstNumber = 0
    SecondNumber = 0
    Result = 0

    def __init__(self, FirstNumber, SecondNumber):
        self.FirstNumber = FirstNumber
        self.SecondNumber = SecondNumber

    def getFirstNumber(self):
        return self.FirstNumber

    def getSecondNumber(self):
        return self.SecondNumber

    def setFirstNumber(self, FirstNumber):
        self.FirstNumber = FirstNumber

    def setSecondNumber(self, SecondNumber):
        self.SecondNumber = SecondNumber

    @classmethod
    def UserInput(self):
        try:
            FirstNumber = int(input("Enter FirstNumber: "))
            SecondNumber = int(input("Enter SecondNumber: "))
            return self(FirstNumber, SecondNumber)
        except:
            print("Invalit INPUT")

            
    def Calculate(self):
        self.Result = self.FirstNumber + self.SecondNumber

    def Display(self):
        print("Result: " + str(self.Result))



obj = Addition.UserInput()
obj.Calculate()
obj.Display()
print(obj.getFirstNumber())
print(obj.getSecondNumber())
obj.setFirstNumber(2)
print(obj.getFirstNumber())
obj.Calculate()
obj.Display()

