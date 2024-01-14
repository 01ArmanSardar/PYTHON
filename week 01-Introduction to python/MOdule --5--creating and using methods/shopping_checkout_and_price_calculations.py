class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)
    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total+=item['price']*item['quantity']
        print('total price',total)
        if amount<total:
            print('your amount is not enough')
        elif amount>total:
            print(f'your give me{amount-total} money extra')
        else:
            print('OK')


arman=Shopping('arsa')
arman.add_to_cart('alu',50,6)
arman.add_to_cart('dim',12,24)
arman.add_to_cart('rice',50,5)
print(arman.cart)
arman.checkout(1000)