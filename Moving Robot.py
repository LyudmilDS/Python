def moving_robot(n,m):
    table = making_matrix(n, m)
    print(table)


def making_matrix(n, m):
    table = []
    for i in range(n):
        a = []
        j = 0
        while( j < m ):
            a.append(input('enter number[' + str(i) + '][' + str(j) + ']='))
            if(not (a[j] == 'R' or a[j]=='D' or a[j]=='L' or a[j]=='U')):
                print("Wrong input. Enter only R/L/D/U!")
                del a[j]
                j -= 1
            j += 1
        table.append(a)
    return(table)


if __name__ == '__main__':
    moving_robot(2,3)
