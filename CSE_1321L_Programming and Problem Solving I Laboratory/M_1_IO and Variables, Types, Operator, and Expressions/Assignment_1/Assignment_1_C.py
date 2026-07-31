#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 1C

print("[Centimeters to Feet and Inches Converter]")
l = float(input("Enter the length in centimeters: "))

ft = l/30.48
modulus = ft % 1
inches = modulus * 12
a = round(inches, 2)

print()
print("The length is " + str(int(ft)) + " feet and " + str(a) + " inches")