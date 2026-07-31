#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 1B

print("[Ideal Gas Law Calculator]")
n = float(input("Enter the number of moles of the gas: "))
Celsius = float(input("Enter the temperature of the gas in Celsius: "))
V = float(input("Enter the volume of the gas in Liters: "))

R = 0.0821 #Ideal gas constant

Kelvin = Celsius + 273.15

P = n*R*Kelvin/V
answer = round(P, 2)

print()
print("The pressure of the gas is " + str(answer) +" atm")