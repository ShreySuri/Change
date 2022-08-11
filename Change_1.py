def cap(small_num, big_num):
    rem = big_num % small_num
    quotient = int((big_num - rem) / small_num)
    return(quotient)

def sift_lower(x, y_list):
    length = len(y_list)
    counter = 0
    for i in range (0, length):
        if y_list[i] > x:
            y_list[i] = "placeholder"
            counter = counter + 1
        else:
            toggle = True

    if counter > 0:
        for i in range (0, counter):
            y_list.remove("placeholder")
    else:
        toggle = False
    
    return(y_list)


def change(amount, currency_list):
    currency_list = sift_lower(amount, currency_list)
    length = len(currency_list)
    max_list = []
    new_list = []
    for i in range(0, length):
        x = currency_list[i]
        y = cap(x, amount)
        max_list.append(y)
        new_list.append(0)

    
    counter = 0
    while new_list != max_list:
        new_list[0] = new_list[0] + 1
        for i in range (0, length - 1):
            if new_list[i] > max_list[i]:
                new_list[i] = 0
                new_list[i + 1] = new_list[i + 1] + 1
            else:
                toggle = True

        total = 0
        for j in range (0, length):
            total = total + currency_list[j] * new_list[j]

        if total == amount:
            counter = counter + 1
        else:
            toggle = False

    return(counter)

def validate_float(x):
    list_x = list(x)
    length = len(list_x)
    accepted_val = []
    for i in range (0, 10):
        i = str(i)
        accepted_val.append(i)
    accepted_val.append(".")
    period_count = 0

    counter = 0
    for j in range (0, length):
        for k in range (0, 11):
            if list_x[j] == accepted_val[k]:
                counter = counter + 1
                if k == 10:
                    period_count = period_count + 1
                else:
                    toggle = True
            else:
                toggle = False
    if counter == length and period_count < 2:
        return(True)
    else:
        return(False)

amount = "None"
while validate_float(amount) == False:
    print("")
    amount = input("What amount do you want change for? ")

amount = float(amount)

denominations = []
input_1 = "None"
while input_1 != "done":
    print("")
    input_1 = input("Enter a denomination. If you have entered all denominations, type 'done'. ")
    input_1 = input_1.lower()

    if validate_float(input_1) == True:
        input_1 = float(input_1)
        denominations.append(input_1)
    elif input_1 != "done":
        print("Please enter a float value or 'done'.")
    else:
        toggle = True
    
    
        
            
            
print(change(amount, denominations))
    
            
    
