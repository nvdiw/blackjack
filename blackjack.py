import random
sumcart = random.randint(1, 11)
q = ''
lst_sumcart = [sumcart]

print('your carts is : ')
print(lst_sumcart)

while q != 'yes' and q != 'no' :
    q = input('do you need cart ? (yes) (no) : ')
    
    if q == 'yes' :
        sumcart = random.randint(1, 11)
        lst_sumcart.append(sumcart)
        print('your carts is : ')
        print(lst_sumcart)
        print('some of your carts is : ')
        print(sum(lst_sumcart))
        q = ''
        
    if sum(lst_sumcart) == 21 :
        print('you win :)')
        break
    elif sum(lst_sumcart) > 21 :
        break

some = sum(lst_sumcart)         
if q == 'no' :
    print(f'some of your carts : {some}')


sumcart_co = random.randint(14, 20)

if sum(lst_sumcart) < 21 :
    print(f'some of CO carts : {sumcart_co}')

if sum(lst_sumcart) > sumcart_co and sum(lst_sumcart) < 21 :
    print('you win :)')
else :
    print('you lose :(')