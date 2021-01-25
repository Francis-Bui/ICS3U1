
# Constants
vowelCount = 0
vowelPass = 0

# Variables
letter = "a"
string = str(input("What's the sentence?"))

# Run code block five times
while vowelPass < 5:

    for x in string:

        if vowelPass == 0:
            if (x == "a"):
                vowelCount += 1
                letter = "a"
        elif vowelPass == 1:
            if (x == "e"):
                vowelCount += 1
                letter = "e"
        elif vowelPass == 2:
            if (x == "i"):
                vowelCount += 1
                letter = "i"
        elif vowelPass == 3:
            if (x == "o"):
                vowelCount += 1
                letter = "o"
        elif vowelPass == 4:
            if (x == "u"):
                vowelCount += 1
                letter = "u"

    print(f"There are {vowelCount} {letter}'s")

    # Increment while loop value
    vowelPass +=1
    # Reset vowel count for next loop
    vowelCount = 0
