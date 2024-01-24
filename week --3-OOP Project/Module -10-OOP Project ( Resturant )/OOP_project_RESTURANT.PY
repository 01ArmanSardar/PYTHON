class User:
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
#..................................................     
class Customer(User):
    def __init__(self, name,money,phone,email,address) -> None:
        self.wallet=money
        self.__order=None
        super().__init__(name,phone,email,address)
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order
    
    def place_order(self,order):
        self.order=order
        print(f'{self.name} placed an order {order.items}')

    def eat_food(self,order):
        print(f'{self.name} eating food {order.items}')
    
    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self,stars):
        pass

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
class server(Employes):
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
    def __init__(self,name,menu=[]) -> None:
        self.name=name
        self.chief=None
        self.server=None
        self.manager=None
        self.menu=menu
        self.expanse=0
        self.balance=0
        self.revenue=0
        self.profit=0
    def add_employee(self,employe_type,employe):
        if employe_type=='chief':
            self.chief=employe
        elif employe_type=='server':
            self.server==employe
        elif employe_type=='manager':
            self.manager=employe
    def receive_payment(self,order,amount,customer):
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount-order.bill
    def pay_expanse(self,amount,description):
        if amount<self.balance:
            self.expanse+=amount
            self.balance-=amount
            print(f'this {amount} expanse for {description}')
        else:
            print(f'not enough money to pay {amount}')
    def pay_salary(self,employee):
        if employee.salary<self.balance:
            employee.recive_salary()
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
            self.burgers.append('burger')
        elif item_type=='drink':
            self.drinks.append('drink')
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price {pizza.price}')
        for burger in self.burgers:
            print(f'name :{burger.name} price :{burger.price}')
        for drink in self.drinks:
            print(f'name{drink.name} price {drink.price}')

#..................................................................
menu=Menu()

pizza_1=Pizza('shutki pizza',600,'larg',['shutki','onion'])
menu.add_in_menu('pizza',pizza_1)
pizza_2=Pizza('alu pizza',400,'large',['potato','onion','oil'])
menu.add_in_menu('pizza',pizza_2)
pizza_3=Pizza('dal pizza',500,'large',['dal','oil'])
menu.add_in_menu('pizza',pizza_3)
menu.show_menu
