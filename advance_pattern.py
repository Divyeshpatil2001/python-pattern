# 1.
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * * * * * * * 
# * * *     * * *
# * *         * *
# *             *
# n = 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     spaces = 2 * (n-i)
#     for j in range(1,spaces+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     spaces = 2 * (n-i)
#     for j in range(1,spaces+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    


# 2. 
#          * * * * * 
#       * * * * *
#     * * * * *
#   * * * * *
# * * * * *   
    
# n = 5
# for i in range(1,n+1):
#     spaces = n - i
#     for j in range(1,spaces+1):
#         print(" ",end=" ")
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()


# 3.
#         1   
#       2   2
#     3   3   3
#   4   4   4   4
# 5   5   5   5   5
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(i," ",end=" ")
#     print()



# 4.
#         1 
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     for j in range(2,i+1):
#         print(j,end=" ")
#     print()
    
    

# 5.
#      * 
#     * * *
#   * * * * *
# * * * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *
# n = 4
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i-1+1):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i-1+1):
#         print("*",end=" ")
#     print()