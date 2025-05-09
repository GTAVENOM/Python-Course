# duplicateList=[1, 5, 3, 5, 7, 10, 7, 7, 52]
# uniqueList=[]
# duplicateList.sort()

# My brute force approach
# i=0
# j=0
# for i in range(len(duplicateList) - 1):
#     if duplicateList[i]==duplicateList[i + 1]:
#         i+=1
#     else:
#         uniqueList.append(duplicateList[i])
#         j+=1
# uniqueList.append(duplicateList.pop())
# print(uniqueList)

#Simpler code

# for i in duplicateList:
#     if i not in uniqueList:
#         uniqueList.append(i)
# print(uniqueList)