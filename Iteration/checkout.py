def checkout():
    '''Program prompts user for price of item. It keeps running total of prices entered, 
    and displays it each time a new price is entered. If the price is 0, the program
    stops prompting the user for prices, and displays the total price, quantity and
    average price'''
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price > 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        elif price < 0:
            print("Error, please enter a positive integer. ")
        else:
            moreItems = False
    if count == 0:
        print("Error, can't perform computations without data.") #prevents divide by zero error
    else:
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)

checkout()
