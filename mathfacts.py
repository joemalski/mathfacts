'''
Simple Math Facts
-----------------

Date: March 7, 2022
By: Joel Malinao

'''

import random
from os import system, name
from time import sleep

# Addition Table
add_table_one = [
    {1: [1,0,1]},
    {2: [1,1,2]},
    {3: [1,2,3]},
    {4: [1,3,4]},
    {5: [1,4,5]},
    {6: [1,5,6]},
    {7: [1,6,7]},
    {8: [1,7,8]},
    {9: [1,8,9]},
    {10: [1,9,10]}
]

add_table_two = [
    {1: [2,0,2]},
    {2: [2,1,3]},
    {3: [2,2,4]},
    {4: [2,3,5]},
    {5: [2,4,6]},
    {6: [2,5,7]},
    {7: [2,6,8]},
    {8: [2,7,9]},
    {9: [2,8,10]},
    {10: [2,9,11]}
]

add_table_three = [
    {1: [3,0,3]},
    {2: [3,1,4]},
    {3: [3,2,5]},
    {4: [3,3,6]},
    {5: [3,4,7]},
    {6: [3,5,8]},
    {7: [3,6,9]},
    {8: [3,7,10]},
    {9: [3,8,11]},
    {10: [3,9,12]}
]

add_table_four = [
    {1: [4,0,4]},
    {2: [4,1,5]},
    {3: [4,2,6]},
    {4: [4,3,7]},
    {5: [4,4,8]},
    {6: [4,5,9]},
    {7: [4,6,10]},
    {8: [4,7,11]},
    {9: [4,8,12]},
    {10: [4,9,13]}
]

add_table_five = [
    {1: [5,0,5]},
    {2: [5,1,6]},
    {3: [5,2,7]},
    {4: [5,3,8]},
    {5: [5,4,9]},
    {6: [5,5,10]},
    {7: [5,6,11]},
    {8: [5,7,12]},
    {9: [5,8,13]},
    {10: [5,9,14]}
]

add_table_six = [
    {1: [6,0,6]},
    {2: [6,1,7]},
    {3: [6,2,8]},
    {4: [6,3,9]},
    {5: [6,4,10]},
    {6: [6,5,11]},
    {7: [6,6,12]},
    {8: [6,7,13]},
    {9: [6,8,14]},
    {10: [6,9,15]}
]

add_table_seven = [
    {1: [7,0,7]},
    {2: [7,1,8]},
    {3: [7,2,9]},
    {4: [7,3,10]},
    {5: [7,4,11]},
    {6: [7,5,12]},
    {7: [7,6,13]},
    {8: [7,7,14]},
    {9: [7,8,15]},
    {10: [7,9,16]}
]

add_table_eight = [
    {1: [8,0,8]},
    {2: [8,1,9]},
    {3: [8,2,10]},
    {4: [8,3,11]},
    {5: [8,4,12]},
    {6: [8,5,13]},
    {7: [8,6,14]},
    {8: [8,7,15]},
    {9: [8,8,16]},
    {10: [8,9,17]}
]

add_table_nine = [
    {1: [9,0,9]},
    {2: [9,1,10]},
    {3: [9,2,11]},
    {4: [9,3,12]},
    {5: [9,4,13]},
    {6: [9,5,14]},
    {7: [9,6,15]},
    {8: [9,7,16]},
    {9: [9,8,17]},
    {10: [9,9,18]}
]

# Multiplication Table
multiply_table_one = [
    {1: [1,1,1]},
    {2: [1,2,2]},
    {3: [1,3,3]},
    {4: [1,4,4]},
    {5: [1,5,5]},
    {6: [1,6,6]},
    {7: [1,7,7]},
    {8: [1,8,8]},
    {9: [1,9,9]},
    {10: [1,10,10]}
]

multiply_table_two = [
    {1: [2,1,2]},
    {2: [2,2,4]},
    {3: [2,3,6]},
    {4: [2,4,8]},
    {5: [2,5,10]},
    {6: [2,6,12]},
    {7: [2,7,14]},
    {8: [2,8,16]},
    {9: [2,9,18]},
    {10: [2,10,20]}
]

multiply_table_three = [
    {1: [3,1,3]},
    {2: [3,2,6]},
    {3: [3,3,9]},
    {4: [3,4,12]},
    {5: [3,5,15]},
    {6: [3,6,18]},
    {7: [3,7,21]},
    {8: [3,8,24]},
    {9: [3,9,27]},
    {10: [3,10,30]}
]

multiply_table_four = [
    {1: [4,1,4]},
    {2: [4,2,8]},
    {3: [4,3,12]},
    {4: [4,4,16]},
    {5: [4,5,20]},
    {6: [4,6,24]},
    {7: [4,7,28]},
    {8: [4,8,32]},
    {9: [4,9,36]},
    {10: [4,10,40]}
]

multiply_table_five = [
    {1: [5,1,5]},
    {2: [5,2,10]},
    {3: [5,3,15]},
    {4: [5,4,20]},
    {5: [5,5,25]},
    {6: [5,6,30]},
    {7: [5,7,35]},
    {8: [5,8,40]},
    {9: [5,9,45]},
    {10: [5,10,50]}
]

multiply_table_six = [
    {1: [6,1,6]},
    {2: [6,2,12]},
    {3: [6,3,18]},
    {4: [6,4,24]},
    {5: [6,5,30]},
    {6: [6,6,36]},
    {7: [6,7,42]},
    {8: [6,8,48]},
    {9: [6,9,54]},
    {10: [6,10,60]}
]

multiply_table_seven = [
    {1: [7,1,7]},
    {2: [7,2,14]},
    {3: [7,3,21]},
    {4: [7,4,28]},
    {5: [7,5,35]},
    {6: [7,6,42]},
    {7: [7,7,49]},
    {8: [7,8,56]},
    {9: [7,9,63]},
    {10: [7,10,70]}
]


multiply_table_eight = [
    {1: [8,1,8]},
    {2: [8,2,16]},
    {3: [8,3,24]},
    {4: [8,4,32]},
    {5: [8,5,40]},
    {6: [8,6,48]},
    {7: [8,7,56]},
    {8: [8,8,64]},
    {9: [8,9,72]},
    {10: [8,10,80]}
]

multiply_table_nine = [
    {1: [9,1,9]},
    {2: [9,2,18]},
    {3: [9,3,27]},
    {4: [9,4,36]},
    {5: [9,5,45]},
    {6: [9,6,54]},
    {7: [9,7,63]},
    {8: [9,8,72]},
    {9: [9,9,81]},
    {10: [9,10,90]}
]


# Subtraction Table
subtract_table_nine = [
    {1: [9,0,9]},
    {2: [9,1,8]},
    {3: [9,2,7]},
    {4: [9,3,6]},
    {5: [9,4,5]},
    {6: [9,5,4]},
    {7: [9,6,3]},
    {8: [9,7,2]},
    {9: [9,8,1]},
    {10: [9,9,0]},
]

subtract_table_eight = [
    {1: [8,0,8]},
    {2: [8,1,7]},
    {3: [8,2,6]},
    {4: [8,3,5]},
    {5: [8,4,4]},
    {6: [8,5,3]},
    {7: [8,6,2]},
    {8: [8,7,1]},
    {9: [8,8,0]}
]

subtract_table_seven = [
    {1: [7,0,7]},
    {2: [7,1,6]},
    {3: [7,2,5]},
    {4: [7,3,4]},
    {5: [7,4,3]},
    {6: [7,5,2]},
    {7: [7,6,1]},
    {8: [7,7,0]}
]

subtract_table_six = [
    {1: [6,0,6]},
    {2: [6,1,5]},
    {3: [6,2,4]},
    {4: [6,3,3]},
    {5: [6,4,2]},
    {6: [6,5,1]},
    {7: [6,6,0]}
]

subtract_table_five = [
    {1: [5,0,5]},
    {2: [5,1,4]},
    {3: [5,2,3]},
    {4: [5,3,2]},
    {5: [5,4,1]},
    {6: [5,5,0]}
]

subtract_table_four = [
    {1: [4,0,4]},
    {2: [4,1,3]},
    {3: [4,2,2]},
    {4: [4,3,1]},
    {5: [4,4,0]}
]

subtract_table_three = [
    {1: [3,0,3]},
    {2: [3,1,2]},
    {3: [3,2,1]},
    {4: [3,3,0]}
]

subtract_table_two = [
    {1: [2,0,2]},
    {2: [2,1,1]},
    {3: [2,2,0]}
]

subtract_table_one = [
    {1: [1,0,1]},
    {2: [1,1,0]}
]


# Division Table
division_table_one = [
    {1: [1,1,1]}
]

division_table_two = [
    {1: [2,1,2]},
    {2: [2,2,1]}
]

division_table_three = [
    {1: [3,1,3]},
    {2: [3,3,1]}
]

division_table_four = [
    {1: [4,1,4]},
    {2: [4,2,2]},
    {3: [4,4,1]}
]

division_table_five = [
    {1: [5,1,5]},
    {2: [5,5,1]}
]

division_table_six = [
    {1: [6,1,6]},
    {2: [6,2,3]},
    {3: [6,3,2]},
    {4: [6,6,1]}
]

division_table_seven = [
    {1: [7,1,7]},
    {2: [7,7,1]}
]

division_table_eight = [
    {1: [8,1,8]},
    {2: [8,2,4]},
    {3: [8,4,2]},
    {4: [8,8,1]}
]

division_table_nine = [
    {1: [9,1,9]},
    {2: [9,3,3]},
    {3: [9,9,1]}
]


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def show_problem(val, optr):
    values = []
    incorrect = 0
    for v in val.values():
        values = v

    print("{} {} {} = ".format(values[0], optr, values[1]), end='')

    i = True
    answer = input_filter()
    while i is True:
        if answer == values[2]:
            print("{} is CORRECT! Please wait...".format(answer))
            sleep(1)
            clear()
            i = False
        else: 
            print("{} is WRONG! Try again!\a\n".format(answer))
            print("{} {} {} = ".format(values[0], optr, values[1]), end='')
            answer = input_filter()
            incorrect = 1

    if incorrect == 1:
        return val


def run_table_of(table, title, optr, iterate):

    clear()
    random.shuffle(table)
    weak_spots = []
    result = None
    i = iterate
    while i >= 0:
        print("{}:".format(title))
        result = show_problem(table[i], optr)
        if result is not None:
            weak_spots.append(result)
        i -= 1
    

    if len(weak_spots) > 0:
        print("Weak Spots on {} \n".format(title))
        for weak in weak_spots:
            for v in weak.values():
                print("{} {} {} = {}".format(v[0], optr, v[1], v[2]))

        input('\nPress any Enter Key to continue...')
    else:
        print("Congrats! No weak spots on {} ".format(title))
        input('\nPress any Enter Key to continue...')
    

def addition_loop():

    i = True
    while i is True:
        clear()
        table = input_filter('Addition Facts: [1-9] Table [0] Exit -> ')
        if table == 1:
            run_table_of(add_table_one, 'Addition Table 1', '+', 9)
        elif table == 2:
            run_table_of(add_table_two, 'Addition Table 2', '+', 9)
        elif table == 3:
            run_table_of(add_table_three, 'Addition Table 3', '+', 9)
        elif table == 4:
            run_table_of(add_table_four, 'Addition Table 4', '+', 9)
        elif table == 5:
            run_table_of(add_table_five, 'Addition Table 5', '+', 9)
        elif table == 6:
            run_table_of(add_table_six, 'Addition Table 6', '+', 9)
        elif table == 7:
            run_table_of(add_table_seven, 'Addition Table 7','+', 9)
        elif table == 8:
            run_table_of(add_table_eight, 'Addition Table 8', '+', 9)
        elif table == 9:
            run_table_of(add_table_nine, 'Addition Table 9', '+', 9)
        elif table == 0:
            i = False
            print('Exiting...')
            sleep(1)
        else:
            print('Incorrect selection...')
            sleep(1)


def multiplication_loop():

    i = True
    while i is True:
        clear()
        table = input_filter('Multiplication Facts: [1-9] Table [0] Exit -> ')
        if table == 1:
            run_table_of(multiply_table_one, 'Multiplication Table 1', 'x', 9)
        elif table == 2:
            run_table_of(multiply_table_two, 'Multiplication Table 2', 'x', 9)
        elif table == 3:
            run_table_of(multiply_table_three, 'Multiplication Table 3', 'x', 9)
        elif table == 4:
            run_table_of(multiply_table_four, 'Multiplication Table 4', 'x', 9)
        elif table == 5:
            run_table_of(multiply_table_five, 'Multiplication Table 5', 'x', 9)
        elif table == 6:
            run_table_of(multiply_table_six, 'Multiplication Table 6', 'x', 9)
        elif table == 7:
            run_table_of(multiply_table_seven, 'Multiplication Table 7','x', 9)
        elif table == 8:
            run_table_of(multiply_table_eight, 'Multiplication Table 8', 'x', 9)
        elif table == 9:
            run_table_of(multiply_table_nine, 'Multiplication Table 9', 'x', 9)
        elif table == 0:
            i = False
            print('Exiting...')
            sleep(1)
        else:
            print('Incorrect selection...')
            sleep(1)


def subtraction_loop():

    i = True
    while i is True:
        clear()
        table = input_filter('Subtraction Facts: [1-9] Table [0] Exit -> ')
        if table == 1:
            run_table_of(subtract_table_one, 'Subtraction Table 1', '-', 1)
        elif table == 2:
            run_table_of(subtract_table_two, 'Subtraction Table 2', '-', 2)
        elif table == 3:
            run_table_of(subtract_table_three, 'Subtraction Table 3', '-', 3)
        elif table == 4:
            run_table_of(subtract_table_four, 'Subtraction Table 4', '-', 4)
        elif table == 5:
            run_table_of(subtract_table_five, 'Subtraction Table 5', '-', 5)
        elif table == 6:
            run_table_of(subtract_table_six, 'Subtraction Table 6', '-', 6)
        elif table == 7:
            run_table_of(subtract_table_seven, 'Subtraction Table 7','-', 7)
        elif table == 8:
            run_table_of(subtract_table_eight, 'Subtraction Table 8', '-', 8)
        elif table == 9:
            run_table_of(subtract_table_nine, 'Subtraction Table 9', '-', 9)
        elif table == 0:
            i = False
            print('Exiting...')
            sleep(1)
        else:
            print('Incorrect selection...')
            sleep(1)


def division_loop():

    i = True
    while i is True:
        clear()
        table = input_filter('Division Facts: [1-9] Table [0] Exit -> ')
        if table == 1:
            run_table_of(division_table_one, 'Division Table 1', '/', 0)
        elif table == 2:
            run_table_of(division_table_two, 'Division Table 2', '/', 1)
        elif table == 3:
            run_table_of(division_table_three, 'Division Table 3', '/', 1)
        elif table == 4:
            run_table_of(division_table_four, 'Division Table 4', '/', 2)
        elif table == 5:
            run_table_of(division_table_five, 'Division Table 5', '/', 1)
        elif table == 6:
            run_table_of(division_table_six, 'Division Table 6', '/', 3)
        elif table == 7:
            run_table_of(division_table_seven, 'Division Table 7','/', 1)
        elif table == 8:
            run_table_of(division_table_eight, 'Division Table 8', '/', 3)
        elif table == 9:
            run_table_of(division_table_nine, 'Division Table 9', '/', 2)
        elif table == 0:
            i = False
            print('Exiting...')
            sleep(1)
        else:
            print('Incorrect selection...')
            sleep(1)


def input_filter(msg=''):

    raw = input(msg)

    try:
        cleaned = int(raw)
    except ValueError as err:
        cleaned = '(Non-Integer)'
    
    return cleaned



def main():

    i = True
    while i is True:
        clear()
        print('--- M A T H  F A C T S  1.0 ---\n')
        operation = input_filter('Enter: [1] Add [2] Subtract [3] Multiply [4] Divide [0] Exit -> ')

        if operation == 1:
            addition_loop()
        elif operation == 2:
            subtraction_loop()
        elif operation == 3:
            multiplication_loop()
        elif operation == 4:
            division_loop()
        elif operation == 0:
            i = False
            print('Exiting...')
            sleep(1)
        else:
            print('Incorrect selection...')
            sleep(1)


# Run main()
if __name__ == '__main__':
    main()