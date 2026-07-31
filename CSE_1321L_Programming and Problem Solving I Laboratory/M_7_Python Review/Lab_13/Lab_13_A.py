#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 13A

temps_input = input("Enter temperatures for each day separated by space:\n")
temps = list(map(int, temps_input.split()))

cold_streak = 0
longest_cold_streak = 0
average_temp = sum(temps) / len(temps)

i = 0
while i < len(temps):
    if temps[i] > 30:
        count = 1
        i += 1
        while i < len(temps) and temps[i] > 30:
            count += 1
            i += 1
        if count >= 3:
            heatwave_count += 1
    else:
        i += 1

current_streak = 0
for temp in temps:
    if temp < 15:
        current_streak += 1
        if current_streak > longest_cold_streak:
            longest_cold_streak = current_streak
    else:
        current_streak = 0

print()
print(f"Number of heat waves: {heatwave_count}")
print(f"Longest cold streak: {longest_cold_streak} days")
print(f"Average temperature: {average_temp:.2f}°C")