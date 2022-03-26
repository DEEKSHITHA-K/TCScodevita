string = input()
count = 1
for i in range(1, len(string)-1):
    if string[i] == 'G':
        if (string[i-1] == 'G') and (string[i+1] == 'G'):
            count+=1
    elif string[i] == 'B':
        if (string[i-1] == 'B') and (string[i+1] == 'B'):
            count+=1 
if string[-1] == string[-2]:
    count+=1
print(count)
