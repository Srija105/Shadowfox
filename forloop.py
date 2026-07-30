import random

rolls = 20
count_6 = 0
count_1 = 0
two_sixes = 0
previous = 0

for i in range(rolls):
    current = random.randint(1, 6)
    print("Roll", i + 1, "=", current)

    if current == 6:
        count_6 += 1

    if current == 1:
        count_1 += 1

    if previous == 6 and current == 6:
        two_sixes += 1

    previous = current

print("\nNumber of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Number of times two 6s came in a row:", two_sixes)
total = 0

for i in range(10):
    total += 10
    print("\nYou completed", total, "jumping jacks.")

    if total == 100:
        print("Congratulations! You completed the workout.")
        break

    answer = input("Are you tired? (yes/no): ").lower()

    if answer == "yes" or answer == "y":
        print("You completed a total of", total, "jumping jacks.")
        break
    else:
        print(100 - total, "jumping jacks remaining.")