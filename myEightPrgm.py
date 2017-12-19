temperature = [10, -20, -289, 100]
file = open("tempValues.txt",'w')
def tempConversion(celcius):
    if celcius > -273.15:
      Fahrenheit = celcius*(9/5)+32
      return Fahrenheit
for i in temperature:
    file.write(tempConversion(i)+"\n")
file.close()
