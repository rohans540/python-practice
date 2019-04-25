#Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s


#function count_Distinct_Strings():
#Input: n (Number of bits)
#Output: Number of possible binary strings without consecutive 1's
def count_Distinct_Strings(n):

    a = []
    b = []

    a.append(1)
    b.append(1)

    for i in range(1, n):
        a.append(a[i-1] + b[i-1])
        b.append(a[i-1])
    return a[n-1] + b[n-1]

if __name__ == "__main__":
    n = int(input("Enter n:"))
    print(count_Distinct_Strings(n))