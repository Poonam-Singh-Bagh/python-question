'''Q 10. Write a Python program to print the even numbers from a given list.'''

def even_num():
    simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_list = []
    for i in simple_list:
        if i % 2 == 0:
          even_list.append(i)
    return even_list
    
    
print (even_num())

