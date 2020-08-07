# stock = 10

# num = int(input('Enter the Number candy you Want: '))

# i = 1
# while i<=num:
#     if i<=stock:
#         print('candy')
#     else:
#         break
#     i += 1

# print('bye')


# while conditon1: 
#     while conditon2:


# for i in somthing1:
#     for j in somthing2:

# while conditon:
#   for i in somthing:

#for i in something:
#   while condition:

# i = 1
# while i<4:
#     j = 1
#     while j<4:
#         print('i', i)
#         print('j', j)
#         j += 1
#     i += 1

amt = 50000
n = 5
while n>0:
    trans = int(input('Enter amount: '))
    if trans<=amt:
        amt -= trans
        print('Transantion Succesfull')
    else:
        print('Failed')
        break
    