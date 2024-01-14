class shop:
    cart=[] #this cart is class attribute,class attribute tah shobgulu instance er sateh share hoi
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item) #akhne amrah self. die cart[] jeh class attributes aceh setah keh acces korlam 

arman =shop('arsa')
arman.add_to_cart('shoes')
arman.add_to_cart('phone')
print(arman.cart)

iqbal=shop('iqbu')
iqbal.add_to_cart('book')
iqbal.add_to_cart('pen')
print(iqbal.cart)
        