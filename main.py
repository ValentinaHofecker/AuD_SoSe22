# Exercise 1
def power(a, b):
    # accept only integers >0
    if a <= 0 or b <= 0:
        return -1
    # base case
    if b == 1:
        return a
    # recursivily call function itself by decrementing b
    if b > 1:
        return a * power(a, b - 1)

print(power(0, 2)) # -1
print(power(1, 1)) # 1
print(power(2, 3)) # 8
print(power(2, 4)) # 16
print(power(3, 3)) # 27

# Exercise 2
# recursive binary search with arguments: numbers (list), num (number to find)
# optionally specify start and end of the list (also used for recursive search)
def binary_search(numbers, num, start = 0, end = None):
    # set end if not specified
    if end == None:
        end = len(numbers) - 1
    # recursively search for num
    if start <= end:
        # set current (mid) index
        mid = (start + end) // 2
        # num in list, return current index (mid)
        if numbers[mid] == num:
            return mid
        # num could be in left half -> split list by setting end = mid - 1 and recursively call function
        elif numbers[mid] > num:
            return binary_search(numbers, num, start, mid - 1)
        # num could be in right half -> split list by setting start = mid + 1 and recursively call function
        else:
            return binary_search(numbers, num, mid + 1, end)
    # start > end (num not in the list)
    else:
        return -1

numbers_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print(binary_search(numbers_list, 5, 0, len(numbers_list)-1)) # 4
print(binary_search(numbers_list, 5)) # 4
print(binary_search(numbers_list, 1)) # 0
print(binary_search(numbers_list, 2)) # 1
print(binary_search(numbers_list, 8)) # 7
print(binary_search(numbers_list, 10)) # 9
print(binary_search(numbers_list, 11)) # -1


# Exercise 3-7
class HashTable:
    def __init__(self, size):
        self.bucket_size = size
        self.size = 0 # stores actual size
        self.buckets = [[] for _ in range(size)] 
    
    # string representation of HashTable, used for printing
    def __str__(self):
        return repr(self.buckets)
    
    def __my_hash(self, element):
        if isinstance(element, int):
            return element % self.bucket_size
        elif isinstance(element, str):
            return len(element) % self.bucket_size
            
    def insert(self, element):
        # get bucket by using our hash function, append the element and increase the size
        key_hash = self.__my_hash(element)
        self.buckets[key_hash].append(element)
        self.size += 1

    def get_element(self, element):
        key_hash = self.__my_hash(element)
        bucket = self.buckets[key_hash]
        # if bucket contains element -> remove element, decrease size and return element
        if element in bucket:
            bucket.remove(element)
            self.size -= 1
            return element
        else:
            return False

    def get_size(self):
        return self.size


hash_table = HashTable(8)
hash_table.insert("abc")
hash_table.insert(5)
hash_table.insert(10)
hash_table.insert("hello")
hash_table.insert("hallo")
print(hash_table.get_size())
print(hash_table.get_element("test"))
print(hash_table.get_element("hallo"))
print(hash_table)

