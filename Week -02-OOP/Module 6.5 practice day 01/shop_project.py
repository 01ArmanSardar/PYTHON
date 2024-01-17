""" 1 .Create a Product class and a Shop class.
2 .Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
3 .Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.
 """
class Product:
    def __init__(self,name,id,price,quantity):
        self.name=name
        self.id=id
        self.price=price
        self.quantity=quantity
class shop:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_product(self,name,id,price,quantity):
        product={'name':name,'id':id,'price':price,'quantity':quantity}
        self.cart.append(product)
    def buy_product(self,id,quantity,amount):
        for product in self.cart:
            if(product['id']==id):
                if(product['quantity']>=quantity):
                    if(product['price']*quantity<=amount):
                        print('congress you buy our product')
                        break
                    else:
                        print('need more money for buy product')
                        break
            else:
                print('not avilable')
                break

add=shop('bdshop')
add.add_product('alu',7,70,4)
add.add_product('apple',6,160,3)
add.add_product('komola',3,45,8)
add.buy_product(7,3,1)