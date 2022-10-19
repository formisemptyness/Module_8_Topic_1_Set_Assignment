'''
Program: set_membership.py
Author: Joshua M McGinley
Last Date Modified: 10/19/2022

Create a project Module 8 and directories more_fun_with_collections.

    Create a file set_membership.py in more_fun_with_collections.
    In set_membership.py
        Write a function in_set() that
            Accepts a set and a value
            Return a boolean value stating if the element is in the set.
        Write a main()
            Initialize a set called test_set (aka make a variable called test_set that is a type/instance of set)
            Initialize a value called test_value (aka make a variable called test_value that is set to a value
            potentially in the set)
            Call in_set() with appropriate values
            Print messages as appropriate
                The value 'apple' is in the set {'banana', 'apple', 'cherry'}
                The value '5' is not in the set {'banana', 'apple', 'cherry'}

'''

def in_set(test_set, test_value):
    if test_value in test_set:
        test_answer = str('The value ' '\'' + str(test_value) + '\'' + ' is in the set ' + str(test_set))
    else:
        test_answer = str('The value ' '\'' + str(test_value) + '\'' + ' is not in the set ' + str(test_set))
    return test_answer

if __name__=='__main__':
    test_set = {1, 2, 3, 4, 5, 6, 22, 98}
    test_value = 23
    test_main = in_set(test_set, test_value)
    print(test_main)
