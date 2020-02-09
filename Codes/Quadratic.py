from math import*


class Quadratic:
    a = 0
    b = 0
    c = 0
    x = 0
    #discriminate = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = a
        self.c = c

    def getA(self, a):
        self.a = a

    def getB(self, b):
        self.b = b

    def getC(self, c):
        self.c = c

    def evaluate(a, b, c, x):
        result = ((a*x*x) + (b*x) + c)
        return result

    def discriminant(a, b, c):
        #     will return (b^2 - 4ac)
        discriminate = (b*b) - (4*a*c)
        return discriminate

    def isImaginaryRoots(discriminate):
        #     roots are imaginary if (b^2 - 4ac) < 0
        if(discriminate < 0):
            return True
        else:
            return False

    def isRealRoots(discriminate):
        #     roots are real if (b^2 - 4a >= 0
        if(discriminate >= 0):
            return True
        else:
            return False

    def firstRoot(a, b, c):
        firstRoot = ((-b) + sqrt((b*b) - (4*a*c))) / ((2*a))
        return firstRoot

    def secondRoot(a, b, c):
        #     -b - sqrt(b^2-4ac)/2a
        secondRoot = ((-b) + sqrt((b*b) - (4*a*c)))/((2*a))
        return secondRoot

    def isPerfectSquare(firstRoot, secondRoot):
        #     if first and second roots are equal
        if(firstRoot == secondRoot):
            print("The Roots are Equal: x1 = " +
                  str(firstRoot) + " x2 = " + str(secondRoot))
            print("it is a Perfect Square")
        else:
            print("The Roots are Equal: x1 = " +
            str(firstRoot) + " x2 = " + str(secondRoot))
            print("it is not a Perfect Square")


# main
    a = float(input("coefficient a: "))
    b = float(input("coefficient b: "))
    c = float(input("coefficient c: "))
    discriminate = discriminant(a, b, c)
    imaginary = isImaginaryRoots(discriminate)
    real = isRealRoots(discriminate)

    print("\nQuadratic expression: " + str(round(a)) +
          "x² + " + str(round(b)) + "x + " + str(round(c)))

    if(imaginary == True):
        print("Imaginary")
    else:
        firstRoot = firstRoot(a, b, c)
        secondRoot = secondRoot(a, b, c)
        PerfectSquare = isPerfectSquare(firstRoot, secondRoot)
        print("Evaluating the expression")
        x = float(input("Enter X: "))
        result = evaluate(a,b,c,x)
        print("Result : ",result)
