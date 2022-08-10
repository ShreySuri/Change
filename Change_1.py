def cap(small_num, big_num):
    rem = big_num % small_num
    quotient = int((big_num - rem) / small_num)
    return(quotient)

def sift_lower(x, y_list):
    length = len(y_list)
    delete_list = []
    for i in range (0, length):
        if y_list[i] > x:
            delete_list.append(x)
        else:
            toggle = True

    delete_list = delete_list.reverse()
    length = len(delete_list)
    for j in range (0, length):
        bad_val = delete_list[j]
        y_list.pop(bad_val)

    return(y_list)

def change(amount, currency_list):
    currency_list = sift_lower(amount, currency_list)
    length = len(currency_list)

    current_list = []
    for i in range (0, length):
        current_list.append(0)

    counter = 0
    while current_list != max_list:
        current_list[length] = current_list[length] + 1
        for i in range (1, length):
            if current_list[i] > max_list[i]:
                current_list[i] = 0
                current_list[i + 1] = current_list[i + 1] + 1
            else:
                toggle = True

        total = 0
        for j in range (0, length):
            total = total + current_list[j] * currency_list[j]

        if total == amount:
            return(current_list)
            counter = counter + 1
        else:
            toggle = False

    print("")
    return(counter)

print(change(5, [1, 2, 5, 10, 20, 50, 100]))
    
            
    
