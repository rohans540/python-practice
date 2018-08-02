def bubblesort(mylist):
    for passnum in range(len(mylist)-1,0,-1):
        for i in range(passnum):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
a = [10, 20, 80, 40, 23, 15, 12, 9]
bubblesort(a)
print(a)
