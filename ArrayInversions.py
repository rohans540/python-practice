#Given an array of positive integers find the inversion count of the array
#Inversion count - How far the array is from being sorted
#input: T (integer)- Number of test cases
#input: N (integer) - For every test case the size of the list
#input: [] (list) - List of N integers

#output: Inversion count of the array

def inverseCount(a, N):
    count = 0
    for i in range(N):
            for j in range(i+1, N):
                if a[i] > a[j]:
                    count +=1
    return count



if __name__ == "__main__":
    T = int(input("Enter number of test cases:"))

    while T != 0:
        a = []
        N = int(input("Enter size of array:"))
        for i in range(N):
            a.append(int(input()))
        
        print("\nThe inverse count is:")
        print(inverseCount(a, N))
        
