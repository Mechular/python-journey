# https://www.learnpython.org/en/Conditions

# associative dictionary
# for loop
# conditions

data = {"John": 23, "Rick": 33, "Mary": 63, "Ron": 23, "Joel": 51}

for key in data:
    if (key != "Rick" and data[key] >= 33) or key in ["John"]:
        print("Your name is " + key + ", and you are " + str(data[key]) + " years old.")