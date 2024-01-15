# Doomsday fuel
# python 2.7
# using Absorbing Markov Chain
import numpy as np
from fractions import Fraction
from fractions import gcd
from functools import reduce

# this function takes a float, returns numerator and denominator
def dec_to_frac(n):
    fraction=Fraction(n).limit_denominator()
    numerator=fraction.numerator
    denominator=fraction.denominator
    return numerator,denominator

def lcm_of_array(numbers):
    return reduce(lambda x, y: abs(x * y) // gcd(x, y), numbers)
    
def solution(n):
    # corner case for 1x1: I literally spent 3 hours to find what was wrong in my code 
    if len(n)==1:
        if(len(n[0])==1 and n[0][0]==0):
            return [1, 1]
    
    other_mat = []
    order_of_zero = []
    order_of_other = []

    # step:1: find rows which have at least one non zero element
    # also store the order/index of each matrix
    for i in range(len(n)):
        z = 0
        for j in range(len(n[i])):
            if n[i][j] != 0:
                z = 1
                break

        if z == 0:
            order_of_zero.append(i)

        if z != 0:
            other_mat.append(n[i])
            order_of_other.append(i)

    order = order_of_zero + order_of_other

    for i in range(len(other_mat)):
        l = []
        for j in order:
            l.append(other_mat[i][j])
        other_mat[i] = l

    #step-3: finding probability of other mat values, also handling fractions
    
    for i in range(len(other_mat)):
        sum = int(0)
        for j in range(len(other_mat[i])):
            sum += other_mat[i][j]
        
    
        # modifying other mat with each_value/sum_of_each_row
        for j in range(len(other_mat[i])):
            other_mat[i][j] = float(float(other_mat[i][j]) / sum)

        
  

    #step-4: setup P,Q
    R = []
    Q = []
    for i in range(len(other_mat)):
        R.append(other_mat[i][:len(order_of_zero)])
        Q.append(other_mat[i][len(order_of_zero):])

    # print(R)

    ########################
    # Convert the matrix to a NumPy array
    numpy_matrix = np.array(Q)
   
    identity_matrix = np.identity(numpy_matrix.shape[0])
    result_matrix = identity_matrix - numpy_matrix

    # Step 5: F=(I-Q)^-1: inverse of result matrix
    F = np.linalg.inv(result_matrix)


    #step-6: FxR
    FR=np.dot(F,R)
 
    # print(R)
    # print('\n')
    # print(Q)

    # to list
    FR=FR.tolist()

    #step-7: take first row of FR
    FR=FR[0]

    # result numerator , denominator
    numerator=[]
    denominator=[]
    list_for_lcm = []
    for i in FR:
        numer,denomi=dec_to_frac(i)
        numerator.append(numer)
        denominator.append(denomi)

        # Take denominator list for non zero numerator
        if numer!=0:
            list_for_lcm.append(denomi)

    #step-8: finding lcm 
    lcm=lcm_of_array(list_for_lcm)

    # step-9: divide lcm by each denominator and multiply the result with numerator
    for i in range(len(numerator)):
        numerator[i]=int(numerator[i]*(lcm/denominator[i]))
    
    # step-10: add lcm at the end of the list
    if(len(other_mat))==1:
        #numerator.append(1)
        pass
    else:
        numerator.append(lcm)
    #print(numerator)
    # numerator contains the final result
    return numerator
    
    
    
    
# x=solution([[0]])
# print(x)
    
# x=solution([[0, 2, 1, 0, 0],
#           [0, 0, 0, 3, 4],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]])
# print(x)

# x=solution([[1, 1, 0, 0, 0, 1],
#           [4, 0, 0, 3, 2, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0]])
# print(x)


# x=solution([[0, 0, 0, 0, 0, 0],
#           [4, 0, 0, 3, 2, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0]])

# print(x)   
