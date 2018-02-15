# Define Choices
print ('''In order for the system to work, you must input one of the three choices below in exactly the way it is shown:


Celcius

Fahrenheit

AbsKel


''')

# Define Variable
measuresfrom = raw_input('Please supply the system of measure you are converting from: ')
measuresto = raw_input('Please supply the system of measure you are converting to: ')
convertmeasures = raw_input('Please supply the temperature in '+measuresfrom+' that you wish to convert to '+measuresto+': ')

CelFah = measuresfrom == "Celcius" and measuresto == "Fahrenheit"
FahCel = measuresfrom == "Fahrenheit" and measuresto == "Celcius"
CelAbsKel = measuresfrom == "Celcius" and measuresto == "AbsKel"

if(CelFah == True):
	CelFah = (int(convertmeasures)*1.8)+32
	print (CelFah)
elif(FahCel == True):
	FahCel = (int(convertmeasures)-32)*.5556
	print (FahCel)
elif(CelAbsKel == True):
	CelAbsKel = (int(convertmeasures)+273.15
	print (CelAbsKel)
else:
	print ('This system of measure is unknown')
