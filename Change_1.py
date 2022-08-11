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
    for i in range(0, length):
        x = currency_list[i]
        y = cap(x, amount)
        max_list.append(y)

    for j in range 
        
            
            

list_1 = [1, 2, 5, 10, 20, 50, 100]
print(change(5, list_1))
    
            
    
