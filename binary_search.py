#binary_search
list2 = [45,67,3,89,11,35,25]
list2.sort()
print(list2)
key2 = int(input("Enter the value you want to search: \n"))

def binary_searching(list2,key):
    low = 0
    high = len(list2)-1
    found = False
    while low <= high and not found:
        mid = (low+high)//2
        if key == list2[mid]:
            found = True
            break
        elif key < list2[mid]:
            high = mid-1
        else:
            low = mid+1
    if found:
        print("Element found")

    else:
        print(f'element not found')

binary_searching(list2,key2)