#list_A = [2, 3, 4]
##list_B = [2, 3, 4]

#print("The first given list is %s" % list_A)
#print('The second given list is %s' % list_B)

#result = [[] for inx in range(len(listA))]
    #for i in range(len(list_A)):
        #for j in range(len(list_B)):
            #result[i] += [list_B[i] * list_A[i][j]]
#print('Results of multiplication is: ', result)

list_A = [2, 3, 4]
list_B = [2, 3, 4]
print("The first given list is %s" % list_A)
print('The second given list is %s' % list_B)
result = [] 
for i in range(0, len(list_A)): 
    result.append(list_A[i] * list_B[i]) 
print('Results of multiplication is: ', result)