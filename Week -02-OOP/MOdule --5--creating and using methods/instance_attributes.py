class shop:
    shopping_mall='jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #this cart is instance attributes
    def add_to_cart(self,item):
        self.cart.append(item)
arman=shop('arsa')
arman.add_to_cart('mango')
arman.add_to_cart('apple')
print(arman.cart)

iqbal=shop('iqbu')
iqbal.add_to_cart('khejor')
iqbal.add_to_cart('kichu nah')
print(iqbal.cart)
