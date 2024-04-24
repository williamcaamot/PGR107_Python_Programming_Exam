
def read_from_user():
    positive_numbers = ()
    zero_numbers = ()
    negative_numbers = ()
    while True:
        latest_input = input("Enter an integer (blank to quit): ")
        if latest_input == "":
            break
        
        try:
            latest_input = int(latest_input)
            if latest_input > 0:
                positive_numbers.append(str(latest_input))
            elif latest_input == 0:
                zero_numbers.append(str(latest_input))
            elif latest_input < 0:
                negative_numbers.append(str(latest_input))
            else:
                inputing = False;
        except:
            print("Please enter valid input")


    print(" ".join(positive_numbers + zero_numbers + negative_numbers))


read_from_user()