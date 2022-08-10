def cap(small_num, big_num):
    rem = big_num % small_num
    quotient = int((big_num - rem) / small_num)
    return(quotient)

def change(amount, currency_list):
    length = len(currency_list)
    max_list = []
    for i in range (0, length):
        currency = currency_list[i]
        x = cap(currency, amount)
        max_list.append(x)
    max_list = max_list.reverse()

    current_list = []
    for i in range (0, length):
        current_list.append(0)

    while current_list != 
        
    
