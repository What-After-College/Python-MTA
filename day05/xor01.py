# # a = [1,2,3,4,5,6]

# # # print(a)
# # # print(a[2:])
# # # print(a[2:4])

# # print(a[-3:0])

#            #    -6      -5         -4       -3      -2       -1                

#           #   0         1           2       3       4         5          
# sandwich = ['bread', 'chicken', 'mayo', 'tomato', 'pesto', 'bread']

# print(sandwich[-3:0])
# print(sandwich[4:0])


# true ^ true = false
# false ^ false = false
# true ^ false = true
# false ^ true = true

# 1  --->    01
# 2   --->   10
#  ^ ----->  11

#  4, 6
#  ----> 0100
# -----> 0110
#   -- ^ 0010


# print(4^6)


a = [4,4,5,5,7,7,1,5,1, 6, 9,9,6]
t = a[0]

for i in a:                          
    if a.count(i)%2 !=0:
        print(i)
        break

for i in range(1, len(a)):
    t = t^a[i]                                                      # t = 0
                                                                    # t = 5^6
# p*n

#   p*n*n --(n*n) 

# a === ''''''''
# a ==== ''''''''
# ^^ ==== 000000
# a^a ==0
# a^0 == a

# a === ''''''''
# 0 === 00000000
# ^ ==  '''''''