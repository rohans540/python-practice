#Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

#number of test cases
t = int(input("Enter number of test cases:"))


while t != 0:
    a = {"arr":[], "misnum": None}              #dict
    n = int(input("Enter size of array:"))      #size of list

    for i in range(n):                          #input array
        a['arr'].append(int(input()))
    m = n + 1                                   #because we assume one number is missing
    sum = m*(m+1)/2                             #sum of complete array
    restsum = 0
    for ele in a['arr']:                        #sum of our array(missing value)
        restsum = restsum + ele
    a['misnum'] = sum - restsum                 #calculating missing number
    print(a['arr'])
    print("missing number is: %d" %a['misnum'])
    t = t - 1                                   #updating number of test cases left

