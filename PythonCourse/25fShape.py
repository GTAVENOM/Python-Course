number=[1,1,1,1,5]
for i in number:
    print('x'*i)
print('')

number=[5,2,5,2,2]
for i in number:
    output=''
    for j in range(i):
        output+='x'
    print(output)