import string
import random

# store characters in lists

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Request number of characters from user

user_input = input("Enter the number of characters you want in your password: ")

# Check input is number > 8
while True:

    try:

        characters_number = int(user_input)

        if characters_number < 8:
            print("Please enter a number greater than 8")
            user_input = input("Enter the number of characters you want in your password: ")
            
        else:
            
            break
    
    except:
        
        print("Please enter a number.")

        user_input = input("How many characters in password?")

# Calculate 30% and 20% of number characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

# Generate password (60% letters and 40% digits and punctuation)
result = []

for x in range(part1):
    result.append(s1[random.randint(0,len(s1)-1])
    result.append(s2[random.randint(0,len(s2)-1])

for x in range(part2):
    result.append(s3[random.randint(0,len(s3)-1])
    result.append(s4[random.randint(0,len(s4)-1])


# Shuffle the result
random.shuffle(result)

# Join result
password = "".join(result)
print("Strong password: ", password)

