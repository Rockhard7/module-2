n = input('введите первую вставку:')
result = ''
for i in range(1,int(n)):
    for j in range(1,int(n)):
        k = int(i)+int(j)
        if j < i:
            continue
        if int(n) % k == 0 and i != j:
            result = result + str(i) + str(j)
        else:
            continue
            k = 0
print(n, '-', result)