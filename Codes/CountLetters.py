CapitalLetter = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"}
SmallLetter = { "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"}
Numeric = {"0","1","2","3","4","5","6","7","8","9"}


CountCapital = 0
CountSmall = 0
CountNumerics = 0
CountSpecial = 0


user = input("Enter Your Name: ")


for i in user:
    if (i in CapitalLetter) ==True:
        CountCapital += 1
    elif (i in SmallLetter) == True:
        CountSmall += 1
    elif (i in CountNumerics) == True:
        CountNumerics += 1
    else:
        CountSpecial += 1

print("Capital Letter: " + str(CountCapital))
print("Small Letter: " + str(CountSmall))
print("Numeric: " + str(CountNumerics))
print("Special Characters: " + str(CountSpecial))



