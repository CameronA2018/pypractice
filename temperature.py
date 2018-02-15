# Define Choices
print ('''In order for the system to work, you must input one of the three choices below in exactly the way it is shown:


Celcius

Fahrenheit

Abskel


''')

# Define Variable
measuresfrom = raw_input('Please supply the system of measure you are converting from: ')
measuresto = raw_input('Please supply the system of measure you are converting to: ')
convertmeasures = raw_input('Please supply the temperature in '+measuresfrom+' that you wish to convert to '+measuresto+': ')

CelFah = measuresfrom == "Celcius" and measuresto == "Fahrenheit"
FahCel = measuresfrom == "Fahrenheit" and measuresto == "Celcius"
CelAbskel = measuresfrom == "Celcius" and measuresto == "Abskel"

if(CelFah == True):
	CelFah = (int(convertmeasures)*1.8)+32
	print (CelFah)
elif(FahCel == True):
	FahCel = (int(convertmeasures)-32)*.5556
	print (FahCel)
elif(CelAbskel == True):
	CelAbskel = (int(convertmeasures)+273.15
	print (CelAbskel)
else:
	print ('This system of measure is unknown')
