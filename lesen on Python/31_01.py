def task2():
    arr = [[2, 0, 0], [3, 0, 9], [4, 7, 6], [5, 1, 3]]

    x = len(arr[0])
    y = len(arr)

    lst = []
    for i in range(y):
        for j in arr[i]:
            lst.append(j)
    set_lst=list(set(lst))
    diff=set_lst[-2]-set_lst[1]
    print(set_lst)
    print(diff)
task2()
