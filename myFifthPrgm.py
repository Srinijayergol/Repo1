def currency_conversion(rate, euros):
    dollars= rate * euros
    return dollars
r = input("Enter the rate: ")
e = input("Enter Euros: ")
print(currency_conversion(float(r), float(e)))
