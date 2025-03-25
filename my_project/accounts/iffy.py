# Task 1: Inefficient Printing
myFavNum = 123456  # Replace with your favorite number between 0 and 999,999

for i in range(1000000):
    if i == myFavNum:
        print(i)

print("\n" + "="*30 + "\n")  # Separator for clarity

# Task 2: Nicely Aligned Numbers
for i in range(0, 126, 5):
    spaces = " " * (3 - len(str(i)))  # Adds leading spaces to align numbers
    print(spaces + str(i))

print("\n" + "="*30 + "\n")  # Separator for clarity

# Task 3: Paying Out a Prisoner’s Dilemma
cooperate1 = True  # Change these values to test different scenarios
cooperate2 = False

if cooperate1 and cooperate2:
    player1 = player2 = 100
elif not cooperate1 and not cooperate2:
    player1 = player2 = 25
elif cooperate1 and not cooperate2:
    player1, player2 = 1, 500
else:
    player1, player2 = 500, 1

print(f"Player1: ${player1}")
print(f"Player2: ${player2}")

print("\n" + "="*30 + "\n")  # Separator for clarity

# Task 4: 3s and 7s, Cheers and Jeers
for x in range(10):
    for y in range(10):
        if x + y == 7 and abs(x - y) == 3:
            print("Aw, rats")
        elif x + y == 7:
            print("Hooray!")
        elif abs(x - y) == 3:
            print("Swell")
