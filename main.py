### run main.py with one argument that is an int representing the size of the budget

import sys


#default value for budget if no arguments provided
if len(sys.argv) == 1:
    budget = 100
elif len(sys.argv) == 2:
    try:
        budget = int(sys.argv[1])
    except ValueError as verr:
        raise(verr)
else:
    raise Exception('Invalid Input. Should contain only a single argument (integer) denoting the budget size.')


### parses the food or drinks file
### returns a dictionary mapping food/drinks to price
### Assumptions stated in challange question
def parse_items_file(file_name):
    items = dict()
    f = open(file_name,"r")
    lines = f.readlines()
    for line in lines:
        key, value = line.strip().split(":")
        items[key] = float(value)
    print items
    return items

### parses the people file
### returns a list of tuples where
###     tuple[0] = name (string)
###     tuple[1] = drinks (list of strings)
###     tuple[2] = food (list of strings)
def parse_people_file(file_name):
    people = []
    f = open(file_name,"r")
    lines = f.readlines()
    for i in range(len(lines)/3):
        index = i*3
        name = lines[index].strip()
        drinks = lines[index+1].strip().split(",")
        food = lines[index+2].strip().split(",")
        people += [(name,drinks,food)]
    print people
    return people

people = parse_people_file("test_data/people1.txt")
food = parse_items_file("test_data/food1.txt")
drinks = parse_items_file("test_data/drinks1.txt")


