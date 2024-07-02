# 1.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# for i in range(1,5):
#     for j in range(0,5):
#         print("*",end=" ")
#     print()    
        

# 2.
# * * * * *
# *       *
# *       *
# * * * * *
# for i in range(1,5):
#     for j in range(1,6):
#         if i==1 or i==4 or j==1 or j==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    

# 3.
# *
# * *
# * * *
# * * * *
# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
    
#  4.   
# * * * *
# * * * 
# * *
# *
# n = 4
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         print("*",end=" ")
#     print() 

#  2 option

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# 5.
#       *
#     * *
#   * * * 
# * * * *
# n = 4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()


# 6.
# 1 
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 


# 7.
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2
# 1      
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 2 option
# n = 6
# for i in range(1,6):
#     for j in range(1,n-i+1):
#         print(j,end=" ")
#     print()

# 8.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# num = 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num += 1
#     print()


# 9.
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         sum = i+j
#         if sum % 2 == 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()


# 10.
# n = 5

# for i in range(1, n + 1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# Set the height of the pyramid
# pyramid_height = int(input("Enter the height of the pyramid: "))

# Call the function to print the pyramid
# print_pyramid(pyramid_height)
n =5
for  i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,(2*i-1)+1):
        print("*",end=" ")
    print()



    
    
    
# n =5
# for  i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for k in range(1,(2*i-1)+1):
#         print("*",end=" ")
#     print()


