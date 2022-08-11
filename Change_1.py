def cap(small_num, big_num):
    rem = big_num % small_num
    quotient = int((big_num - rem) / small_num)
    return(quotient)

def higher_than(x, y_list):
    length = len(y_list)
    index_list = []
    for i in range (0, length):
        if y_list[i] > x:
            index_list.append(i)
        else:
            toggle = True

    return(index_list)

def change(amount, currency_list):


print(change(5, [1, 2, 5, 10, 20, 50, 100]))
    
            
    
