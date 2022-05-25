

def restaurant():
    total = 0
    while True:

        if order in menu:
         total += price
         print(f'{order} cost {price}, total is {total}')

         if not order:
            break
        
        else: print(f'Your total is {total}') 

if __name__ == "__main__":

    menu = {'sandwich': 12, 'soup':8, 'steak':31, 'desert':6, 'coffee':4, 'tea':3}
    order = input("What would you like to get? ").strip()
    price = menu[order]
    