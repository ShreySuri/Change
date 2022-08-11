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

    
    
        
            
            
amount = 1
list_1 = [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100]
print(change(amount, list_1))
    
            
    
