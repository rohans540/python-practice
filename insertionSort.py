
def insertionSort(a):

    for i in range(1, len(a)):
        key = a[i]

        j = i - 1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

if __name__ == "__main__":

    T = int(input("Enter number of test cases:"))

    while T != 0:
        N = int(input("Enter size of array:"))
        a = []

        for i in range(N):
            a.append(int(input()))

        insertionSort(a)
        print("Sorted list:")

        print(a)
        T -= 1

