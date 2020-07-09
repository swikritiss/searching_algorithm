#linear_search
list1 = [34,5,6,78,35,47]
key = int(input("enter the value you want to search: \n"))


def linear_searching(list1,key):
    for i in range(0,len(list1)):
        if key == list1[i]:
            print(f'element is found and is in {i} position')
            break
    else:

        print("element not found")

linear_searching(list1,key) 

