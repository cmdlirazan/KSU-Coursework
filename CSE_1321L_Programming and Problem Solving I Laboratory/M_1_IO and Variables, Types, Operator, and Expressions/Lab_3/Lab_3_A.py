#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 3A

amount_owed = float(input("Amount owed: $"))
APR = float(input("APR: "))

APR_percentage = APR/100
MPR_dec = APR_percentage/12
MPR_percentage = MPR_dec*100
MPR = round(MPR_percentage, 3)

MP = amount_owed*MPR_dec
MP_rounded = round(MP, 2)

print("Monthly percentage rate: " + str(MPR))
print("Minimum payment: $" + str(MP_rounded))