# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

#get user name 
name= input("What's your name?") # ask for their name
#this is input always a string
print(f"Hi, {name}! Let's do some math")
#is your output
# ask for your birthday
# ask for favorite food
# ask for 2 numbers

birthday= input("What is your birthday?")
food= input("What is your favorite food?")
number= input("What are 2 numbers")

print(f"My birthday is {birthday}. My favorite food is {food}. Two numbers are {number}")



# Get two numbers from the user and ask for their name to personalize the experience
















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings