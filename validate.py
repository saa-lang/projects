def cal():
    print('Welcome To Basic Cal')
    num = int(input("What Is Your Number: "))
    numo = int(input('Enter Your Second Number: '))

    add = num + numo
    add1 = num - numo
    add3 = num / numo

    print(add)
    print(add1)
    print(add3)

def value():
           print("Solve the following. Pay Attention To Grammar")
           a = input('Who is your favorite cousin? ')

           if a == 'Noorain':
                          print('ACCESS GRANTED')
                          cal()

           else:
               print('RECOVERY FAILED')


psk = input('ENTER YOUR PASSWORD: ')
if psk == 'Saafy' :
    cal()

else:
    print('ACCESS DENIED')
    value()









 



 