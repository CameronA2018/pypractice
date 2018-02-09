# Define Variables
measure_system = str(input('Please supply the system of measure that you wish to convert from: '))
convert_cel = int(input('Please give the temperature in Celcius that you wish to convert: '))
convertfah_to = str(input('Please supply the system of measure that you wish to convert to: '))
convert_fah_cel = int(input('Please give the temperature in Fahrenheit that you wish to convert to Celcius: '))
convert_fah_aok = int(input('Please give the temperature in Fahrenheit that you wish to convert to Absolute/Kelvin: '))
convert_aok = int(input('Please give the temperature in Absolute/Kelving that you wish to convert: '))

# Declare User Options
print ('''Your options for temperature conversions are as follows:

Celcius
Fahrenheit
AbsKel

You must type the options above exactly as they are shown, or the system will not work.''')

# Ask "the Question"
print (measure_system)

# Ask User for Temperature Measure Celcius
if(measure_system == "Celcius"):
	print (convert_cel)
	print (celcius_fah)

# Convert Celcius to Fahrenheit
celcius_fah = (convert_cel*1.8)+32

# Ask User for Temperature Measure Fahrenheit
if(measure_system == "Fahrenheit"):
	print (convertfeh_to)
if(convertfah_to == "Celcius"):
	print (convert_fah_cel)
	print (fahrenheit_cel)
if(convertfah_to == "AbsKel"):
	print (convert_fah_aok)
	print (fahrenheit_aok)

# Convert Fahrenheit to Celcius and Absolute/Kelvin
fahrenheit_cel = (convert_fah_cel-32)/1.8
fahrenheit_aok = (convert_fah_aok+459.67)*(5/9)

# Ask User for Temperature Measure Absolute/Kelvin
if(system_measure == "Absolute/Kelvin"):
	print (convert_aok)
	print (aok_fah)

# Convert Absolute/Kelvin to Fahrenheit
aok_fah = (convert_aok*(9/5))-459.67
