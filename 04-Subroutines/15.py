import mymath

rand = mymath.generate_number()
guess = 0

while True:
    guess = mymath.read_number("Enter a number from 1 to 9: ")
    if guess != rand:
        print("incorrect")
        continue
    print("correct")
    break
