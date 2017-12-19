def tempConversion(celcius):
    if celcius > -273.15:
         Fahrenheit = celcius*(9/5) + 32
         return(Fahrenheit)
    else:
        print("The temperature cannot be lowest than -273.15 degree celcius")
print("Temparture conversion from degree to celciuss")
temperatures=[10,-20,-289,100]
for t in temperatures:
  print(tempConversion(t))
 
