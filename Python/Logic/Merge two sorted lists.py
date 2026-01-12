##Merge two sorted lists.

def twoListedMerge(list1,list2):
    i=j=0
    mergedList=[]
    while i<len(list1) and j<len(list2):
        print("-----------------------")
        print(list1[i],'First Element')
        print(list2[j],'Second Element')
        if list1[i]<= list2[j]:
            mergedList.append(list1[i])
            print(mergedList,'mergedList first Element')
            i+=1
            print(i,' I Element')
        else:
            mergedList.append(list2[j])
            print(mergedList,'mergedList Second Element')
            j+=1
            print(j,'J Element')


    ##exit()
    mergedList.extend(list1[i:])
    print(mergedList,'first mergedList Element')
    mergedList.extend(list2[j:])
    print(mergedList,'Second mergedList Element')

    return mergedList


print(twoListedMerge([1, 3, 5, 7,9,10,11], [2, 4, 10]))




