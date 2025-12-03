"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

with open('task5.csv') as file:
    amount = 0
    match = False

    stock = file.read().split('\n')

    query = input('Enter the stock symbol: ')
    query = query.upper()

    for i in stock:
        stocklist = i.split(',')
        symbol = stocklist[0]
        if query == symbol:
            print(stocklist[1], end='')
            match = True
            try:
                print(f',{stocklist[2]}') #some company names have commas in them so splitting by the commas splits the company names in half, this is just trying to see if there is another index after where the company should be and prints that if there is
            except:
                break
        elif query in symbol:
            amount += 1

    if amount > 0 and match == False:
        print(f'There are {amount} stocks with that symbol')
    elif amount == 0 and match == False:
        print('No matches')
