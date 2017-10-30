### run main.py with one argument that is an int representing the size of the budget

import sys
from copy import deepcopy

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
    return items



### parses the "people" text file
### returns a list of Person objects
### dependencies: food and drinks dictionaries should be set already
def parse_people_file(file_name, drinks, food):
    people = []
    f = open(file_name,"r")
    lines = f.readlines()
    for i in range(len(lines)/3):
        index = i*3
        name = lines[index].strip()
        drinks = lines[index+1].strip().split(",")
        food = lines[index+2].strip().split(",")
        people += [Person(name, drinks, food)]
    return people




'''
#############
# Algorithm #
#############
Goal:
    1. Try to make sure every person has at least one food or drink
        from their preferences. Perform this in order from
        least exprnsive prefs to most expensive prefs for each
        food and drink item per person. There is also a prefernce
        for food over drinks, because you people need to eat but
        they don't need to have drinks assuming there's water
        provided.
    2. If budget is maxed out before this criteria 1 is met,
        then just return. There's no way to make it better.
    3. Else if every person gets one food or drink item from their,
        prefs, then find the second least expensive pref for each person,
        and buy those.
        Perform this step until budget is maxed out or until every person
        gets every food and drink item in their prefs.
    4. If budget is still not maxed out, then just return the amount left
        over from the budget. It's unnecessary to spend more money on food
        and drinks if everybody alredy has all the food and drinks they want.
'''

class Person:
    ### name    -> string
    ### drinks  -> list of strings sorted by unit price
    ### food    -> list of strings sorted by unit price
    def __init__(self, name, _drinks, _food):
        self.name = name
        self.drinks = sorted(_drinks, key=lambda item: drinks[item])
        self.food = sorted(_food, key=lambda item: food[item])

    def __repr__(self):
        return repr((self.name, self.drinks, self.food))
    
### Dependency
### Order matters here. "people" should be set last beccause it
### depends on "food" and "drinks" to sort the lists
food = parse_items_file("test_data/food1.txt")
drinks = parse_items_file("test_data/drinks1.txt")
people = parse_people_file("test_data/people1.txt", drinks, food)
people_unmodified = deepcopy(people)
bag = dict()
### pops the item from 
def add_item_to_bag(item):
    try:
        bag[item] += 1
    except:
        bag[item] = 1
            
def all_items_popped():
    for person in people:
        if len(person.drinks) > 0 or len(person.food) > 0:
            return False
    return True

while budget > 0:
    old_budget = 0 + budget
    if all_items_popped():
        break;
    people_by_drink = sorted(people, key=lambda person: drinks[person.drinks[0]] if len(person.drinks)>0 else 0)
    people_by_food = sorted(people, key=lambda person: food[person.food[0]] if len(person.food)>0 else 0)
    for person in people_by_food:
        if len(person.food) > 0 and food[person.food[0]] <= budget:
            item = person.food.pop(0)
            add_item_to_bag(item)
            budget -= food[item]
    for person in people_by_drink:
        if len(person.drinks) > 0 and drinks[person.drinks[0]] <= budget:
            item = person.drinks.pop(0)
            add_item_to_bag(item)
            budget -= drinks[item]

    ### case where budget is not zero but we can
    ### no longer purchase anything.
    if old_budget == budget:
        break;


####################
### Pretty Print ###
####################
print '\nFood and drinks accounted for:'
for p1,p2 in zip(people, people_unmodified):
    checked_food = [val for val in p2.food if val not in p1.food]
    checked_drinks = [val for val in p2.drinks if val not in p1.drinks]
    #print (p1.name +'drinks :' + str(checked_drinks) + '\tfood :' + str(checked_food)).expandtabs(30)
    print '\tName: {0:16} Drinks: {1:30} Food: {2:30}'.format(p1.name, checked_drinks,checked_food)
print '\nFood and drinks that were to too expensive to purchase per person:'
for p in people:

    print '\tName: {0:16} Drinks: {1:30} Food: {2:30}'.format(p.name, p.drinks,p.food)

print '\nQuantity and total cost spent for each item:'
for index, key in zip(range(len(bag)), bag):
    if key in food:
        cost = bag[key]*food[key]
    else:
        cost = bag[key]*drinks[key]
    print '{0:6} {1:<20} quantatiy: {2:<9} total_cost: {3:<12}'.format(index+1, key, bag[key], cost).ljust(5)
    #print ('\t'+str(index) +" "+ key+'\tquantity : ' + str(bag[key]) + '\ttotal_cost s: '+ str(cost)).expandtabs(30)
         
print 'Total cost:',sum([bag[key]*food[key] for key in bag if key in food] +
                        [bag[key]*drinks[key] for key in bag if key in drinks])
print 'Amount left over:', budget
