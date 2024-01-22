class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Regular_customer(Customer):
    def __init__(self, name, age,coupone:1):
        self.coupone=coupone
        super().__init__(name, age)
class ErRegular_Customer(Customer):
    def __init__(self, name, age,coupone:0):
        self.coupone=coupone
        super().__init__(name, age)

class Resturant:
    cart=[]
    def __init__(self,name):
        self.name=name
    
    def add_food(self,item,id,price):
        food_details={'item':item,'id':id,'price':price}
        self.cart.append(food_details)
    def buy_food(self,item,id,amount):
        for Food in self.cart:
            if Food['id']==id:
                if Food['price']<=amount:
                    print('congratulations you got food')
                    print(f'get your extar money : {amount-Food['price']}')
                    break
                elif Food['price']>amount:
                    print(f'need more : {Food['price']-amount} money')
            else:
                print('your recomended food not found')
                break


class employee:
    def __init__ (self,name,age,salary):
        self.name=name
        self.age=age
        
        self.salary=salary
    def incriment_salary(self,incriment_amount):
        self.salary+=incriment_amount
class manager(employee):
    def __init__(self, name, age, salary,special_tbl_no):
        self.special_sunglass=special_tbl_no
        super().__init__(name, age,salary)
    def incriment_salary(self, incriment_amount):
        return super().incriment_salary(incriment_amount)
    
class waiter(employee):
    def __init__(self, name, age, salary,serail_no):
        self.serial_no=serail_no
        super().__init__(name, age, salary)

    
class chief (employee):
    def __init__(self, name, age, salary,room_no):
        self.room_no=room_no
        super().__init__(name, age, salary)

manager_rohim=manager('rohim vai',25,14000,1)
manager_rohim.incriment_salary(5000)
print(manager_rohim.salary)
food=Resturant('madina resturant') 
food.add_food('vaht',12,18)
food.add_food('mach',15,28)

food.buy_food('vhat',12,30)
