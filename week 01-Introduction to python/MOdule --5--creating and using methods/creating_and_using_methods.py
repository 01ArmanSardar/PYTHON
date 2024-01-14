class phone:
    name='samsung'
    color=1200
    owner='microsoft'
    features=['camera','speaker','hammer']

    def call():
        print('callin it-self')
myphone=phone
myphone.call()