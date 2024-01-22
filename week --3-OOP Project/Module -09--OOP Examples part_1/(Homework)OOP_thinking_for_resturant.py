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
    

    