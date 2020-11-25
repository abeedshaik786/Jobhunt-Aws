# def modification(mylist):
#     count_data = []
#     count = 0
#     for i in range(len(mylist)):
#         for j in range(len(mylist)):
#             if mylist[j] == mylist[i]:
#                 print(list)
#                 count +=1
#                 count_data.append(count)
#     return count_data
mylist=[5,4,6,6,5,7,5,4,5,3,5,4,4,3]
from collections import Counter
dump = dict(Counter(mylist))
print('dumpdata',dump)
                
        