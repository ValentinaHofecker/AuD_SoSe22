# exercise 1
def count_integer(numbers, integer):
    occurrence = 0
    for i in numbers:
        if i == integer:
            occurrence = occurrence + 1
    if occurrence > 0:
        return occurrence
    else:
        return 42


TestList = [1, 2, 3, 4, 5, 5, 5]

print count_integer(TestList, 1)



# exercise 2
def list_func(numbers, integer):
    temp_list = list(numbers)
    found = False
    for index, value in enumerate(temp_list):
        if value == integer:
            temp_list[index] = 6
            found = True

    if found == True:
        temp_list.reverse()
        print temp_list
        temp_list.reverse()
        return temp_list
    else:
        return []


print list_func(TestList, 9)



# exercise 3
def compare_lists(list1, list2):
    common_elements = []
    for i in list1:
        for j in list2:
            if (i == j) and i not in common_elements:
                common_elements.append(i)
    return common_elements

list1 = TestList
list2 = [9, 5, 1, 2, 3, 20, 25]

print compare_lists(list1, list2)



# exercise 4
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

list3 = ["apple", "banana", "orange", "apple"]
list4 = [1, 2, 3, 4, 4, 4]

print remove_duplicates(list4)



# exercise 5
def dict_func(dictionary):
    if ("Type" in dictionary):
        typ = dictionary["Type"]
    else:
        typ = "unknown type"
    if ("Brand" in dictionary):
        brand = dictionary["Brand"]
    else:
        brand = "unknown brand"
    if ("Price" in dictionary):
        price = dictionary["Price"]
    else:
        price = "unknown price"
    print"You have a", typ, "from", brand, "that costs", price,"."
    dictionary["OS"] = "Linux"
    print(dictionary)


my_dict = {"Type": "Notebook", "Brand": "Dell", "Price": 2000}
dict_func(my_dict)

my_dict1 = {"Type": "Notebook", "Price": 2000}
dict_func(my_dict1)