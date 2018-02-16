# Define Choices
print (''' 



In order for the system to work, you must input one of the three choices below in exactly the way it is shown:


Celcius

Fahrenheit

AbsKel


''')

# Define Variable
measuresfrom = raw_input('Please supply the system of measure you are converting from: ')
measuresto = raw_input('Please supply the system of measure you are converting to: ')
convertmeasures = raw_input('Please supply the temperature in '+measuresfrom+' that you wish to convert to '+measuresto+': ')

# System Measures Variable And Statements
CelFah = measuresfrom == "Celcius" and measuresto == "Fahrenheit"
FahCel = measuresfrom == "Fahrenheit" and measuresto == "Celcius"
CelAbsKel = measuresfrom == "Celcius" and measuresto == "AbsKel"
AbsKelCel = measuresfrom == "AbsKel" and measuresto == "Celcius"
FahAbsKel = measuresfrom == "Fahrenheit" and measuresto == "AbsKel"
AbsKelFah = measuresfrom == "AbsKel" and measuresto == "Fahrenheit"

# Formulaic Ifs for Conversion
if(CelFah == True):
	CelFah = (float(convertmeasures)*1.8)+32
	print (CelFah)
elif(FahCel == True):
	FahCel = (float(convertmeasures)-32)*.5556
	print (FahCel)
elif(CelAbsKel == True):
	CelAbsKel = (float(convertmeasures)+273.15)
	print (CelAbsKel)
elif(AbsKelCel == True):
	AbsKelCel = ((float(convertmeasures))+(float(-273.15)))
	print (AbsKelCel)
elif(FahAbsKel == True):
	FahAbsKel = ((float(convertmeasures)+459.67)*(5/9))
	print (FahAbsKel)
elif(AbsKelFah == Ture):
	AbsKelFah = ((float(convertmeasures)*(9/5))-459.67)
else:
	print ('This system of measure is unknown')
