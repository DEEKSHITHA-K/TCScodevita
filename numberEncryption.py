num = input()
commands = input()
key = 0
# for i in commands:
keyEle = num[0]
i = 0
while(i < len(commands)):
    # print(i)
    if commands[i] == 'R':
        keyEle = num[key+1]
        key+=1
        # print('[')
    elif commands[i] == 'L':
        keyEle = num[key-1]
        key-=1
    elif commands[i] == 'T' and int(keyEle) < 9:
        keyEle = int(keyEle)+1
        tempNum = num[key:key+1].replace(num[key], str(keyEle), 1)
        num = num[0:key]+tempNum+num[key+1:]
    elif commands[i] == 'D' and int(keyEle) > 0:
        # print('in D')
        # print(keyEle)
        keyEle = int(keyEle)-1
        tempNum = num[key:key+1].replace(num[key], str(keyEle),1)
        # if key == 0:
        #     num = tempNum + num[1:]
        # elif key == len(num):
        #     num = num[:-1]+tempNum
        # else:    
        num = num[0:key]+tempNum+num[key+1:]
        # print(num, '0')
    elif commands[i] == 'S':
        swapIdx = int(commands[i+1])-1
        # temp = num[key]
        # num[key] = num[swapKey]
        # num[swapKey] = temp
        if swapIdx > key: 
            num = num[:key]+num[swapIdx]+num[key+1:swapIdx]+num[key]+num[swapIdx+1:]
        else:
            num = num[:swapIdx]+num[key]+num[swapIdx+1:key]+num[swapIdx]+num[key+1:]
        i+=1
    # print(key, keyEle)
    # print(num)

    i+=1
print(num)
