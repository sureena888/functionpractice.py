question=input("What would you like to convert-distance, volume, or weight?")
while question == "distance" or "volume" or "weight":


    def distance(feet):
        return feet*12
    def volume(liter):
        return liter*1000
    def weight(gram):
        return gram/1000

    if question != "distance" or "volume" or "weight":
        question=input("What would you like to convert-distance, volume, or weight?")
    if question == "distance":
        user_input = input("How many feet do you have?")
        print(distance(int(user_input)))
    elif question == "volume":
        user_input = input("how many liters do you have?")
        print(volume(int(user_input)))
    elif question == "weight":
        user_input = input("how many grams do you have?")
        print(weight(int(user_input)))
