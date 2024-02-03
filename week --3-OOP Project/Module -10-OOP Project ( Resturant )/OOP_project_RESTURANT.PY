from abc import ABC ,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
#..................................................     
class Customer(User):
    def __init__(self, name,phone,email,address,money) -> None:
        self.wallet=money
        self.__order=None
        self.due_amount=0
        super().__init__(name,phone,email,address)
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order
    
    def place_order(self,order):
        self.order=order
        self.due_amount += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')

    def eat_food(self,order):
        print(f'{self.name} eating food {order.items}')
    
    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self,stars):
        pass
# ................
class Order:
    def __init__(self,customer,items) -> None:
        self.customer=customer
        self.items=items
        total=0
        for item in items:
            total+=item.price
        self.bill=total

#...........................................................
class Employes(User):
    def __init__(self, name,phone,email,address,salary,starting_date,departmrnt) -> None:
        self.salary=salary
        self.due=salary
        self.starting_date=starting_date
        self.departmrnt=departmrnt
        super().__init__(name,phone,email,address)

    def recive_salary(self):
        self.due=0
#.......................................................
class Cheif(Employes):
    def __init__(self, name, phone, email, address, salary, starting_date, departmrnt,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, departmrnt)
        self.cooking_item=cooking_item
#........................................................
class Server(Employes):
    def __init__(self, name, phone, email, address, salary, starting_date, departmrnt) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, departmrnt)
        self.tips_earning=0

    def take_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def serve_food(self,order):
        pass

    def recive_tips(self,amount):
        self.tips_earning+=amount
#.............................................................
class Manager(Employes):
    def __init__(self, name, phone, email, address, salary, starting_date, departmrnt) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, departmrnt)
#.....................................................
class Resturant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name=name
        self.orders=[]
        self.chief=None
        self.server=None
        self.manager=None
        self.rent=rent
        self.menu=menu
        self.expanse=0
        self.balance=0
        self.revenue=0
        self.profit=0
    def add_employee(self,employe_type,employe):
        if employe_type=='chief':
            self.chief=employe
        elif employe_type=='serverr':
            self.server==employe
        elif employe_type=='manager':
            self.manager=employe
    def add_order(self,order):
        self.orders.append(order)
    def receive_payment(self,order,amount,customer):
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount-order.bill
        else:
            print('not enough money')
    def pay_expanse(self,amount,description):
        if amount<self.balance:
            self.expanse+=amount
            self.balance-=amount
            print(f'this {amount} expanse for {description}')
        else:
            print(f'not enough money to pay {amount}')
    def pay_salary(self,employee):
        print(f'paying salary for {employee.name}salary: {employee.salary}')
        if employee.salary<self.balance:
            self.balance-=employee.salary
            self.expanse+=employee.salary
            employee.recive_salary()
            
    def show_employees(self):
        print(f'------------showing employees----------- ')
        if self.chief is not None:
            print(f'chef : {self.chief.name} with salary {self.chief.salary}')
        #server er output asteche nah
        if self.server is not None:
            print(f'server : {self.server.name} with salary {self.server.salary}')
#.........................................................
class Food:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        self.cooking_time=15
    
class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        self.meat=meat
        self.ingredients=ingredients
        super().__init__(name, price)

class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        self.size=size
        self.toppings=toppings
        super().__init__(name, price)

class Drinks(Food):
    def __init__(self, name, price,isCold=True) -> None:
        super().__init__(name, price)
        self.isCold=isCold
#........................................................
class Menu:
    def __init__(self) -> None:
        self.burgers=[]
        self.pizzas=[]
        self.drinks=[]

    def add_in_menu(self,item_type,item):
        if item_type== 'pizza':
            self.pizzas.append(item)
        elif item_type=='burger':
            self.burgers.append(item)
        elif item_type=='drink':
            self.drinks.append(item)
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price {pizza.price}')
        for burger in self.burgers:
            print(f'name :{burger.name} price :{burger.price}')
        for drink in self.drinks:
            print(f'name :{drink.name} price {drink.price}')

#..................................................................
menu=Menu()

pizza_1=Pizza('shutki pizza',6000,'larg',['shutki','onion'])
menu.add_in_menu('pizza',pizza_1)
pizza_2=Pizza('alu pizza',400,'large',['potato','onion','oil'])
menu.add_in_menu('pizza',pizza_2)
pizza_3=Pizza('dal pizza',500,'large',['dal','oil'])
menu.add_in_menu('pizza',pizza_3)

#add burger to the menu
burger_1=Burger('Naga Burger',1000,'chicken',['bread','chili'])
menu.add_in_menu('burger',burger_1)
burger_2=Burger('beef buregr',1200,'beef',['goru','haddi'])
menu.add_in_menu('burger',burger_2)

#add drinks
jiraphani=Drinks('jiraphni',50,True)
menu.add_in_menu('drink',jiraphani)
coffe=Drinks('coffee',80,False)
menu.add_in_menu('drink',coffe)
#show menu
menu.show_menu()

resturant=Resturant('sai Baba Resturant',2000,menu)
#add employes
manager=Manager('kala chan',5,'kalacahn@.com','kaliapur',1500,'january 1 2020','core')
resturant.add_employee('manager',manager)
chef=Cheif('rustom baburchi',6,'chuparustom@.com','rustomnagar',3500,'feb 1 2020','chef','everything')
resturant.add_employee('chief',chef)

server=Server('chotu server',7,'nai@jai.com','resturant',200,'march 1 2020','server')
resturant.add_employee('serverr',server)
#show employees 
resturant.show_employees()

#1 customer placing a order
customer_1=Customer('sakib khan',6,'king@khan','banani',100000)
order_1=Order(customer_1,[pizza_3,pizza_1,coffe])
customer_1.place_order(order_1)
resturant.add_order(order_1)

#customer_1 paying for order_1
resturant.receive_payment(order_1,15000,customer_1)

print(f'revenue is {resturant.revenue}, and  balance is {resturant.balance} after first customer')

#PAY RENT
resturant.pay_expanse(resturant.rent,'rent')
print(f'after rent revenue {resturant.revenue}, and  balance is {resturant.balance} and expanse {resturant.expanse}')

resturant.pay_salary(chef)
print(f'after salary revenue {resturant.revenue}, and  balance is {resturant.balance} and expanse {resturant.expanse}')