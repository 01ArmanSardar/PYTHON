""" def double_func():
    print('start function there')
    def innerfunc():
        print('inside the inner function')
        return 3000
    return innerfunc
print(double_func()())
 """

def do_somthing(work):
    print('playing')
    work()
    print('dancing')

def coding():
    print('code some speacial thing')

do_somthing(coding)