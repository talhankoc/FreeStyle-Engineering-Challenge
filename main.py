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


class Person:
    ### name    -> string
    ### drinks  -> list of strings sorted by unit price
    ### food    -> list of strings sorted by unit price
    def __init__(self, name, drinks, food):
        self.name = name
        self.drinks = drinks
        self.food = food

    def __repr__(self):
        return repr((self.name, self.drinks, self.food))

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
        _drinks = lines[index+1].strip().split(",")
        _drinks = sorted(_drinks, key=lambda item: drinks[item])
        _food = lines[index+2].strip().split(",")
        _food = sorted(_food, key=lambda item: food[item])
        people += [Person(name, _drinks, _food)]
    print people
    return people




'''
#############
# Algorithm #
#############
Goal:
    * Buy food and drinks without surpassing the budget
    1. Try to make sure every person has one food or drink
        from their preferences. Perform this in order from
        least exprnsive prefs to most expensive prefs for each
        food and drink item per person.
    2. If budget is maxed out before this criteria is met,
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

### Dependency
### Order matters here. "people" should be set last beccause it
### depends on "food" and "drinks" to sort the lists
food = parse_items_file("test_data/food1.txt")
drinks = parse_items_file("test_data/drinks1.txt")
people = parse_people_file("test_data/people1.txt", drinks, food)
items_to_buy = dict()

while budget > 0:
    people_by_drink = sorted(people, key=lambda person: drinks[person.drinks[0]] if len(person.drinks)>0 else 0)
    people_by_food = sorted(people, key=lambda person: food[person.food[0]] if len(person.food)>0 else 0)
    #print people_by_drink
    #print people_by_food
    ###iterate through both sorted lists
    for i in range(len(people)):
        ###base case
        person = people_by_drink[i]
        if len(person.drinks) > 0 and drinks[person.drinks[0]]<=budget:
            d = person.drinks[0]
            print d
            try:
                items_to_buy[d] += 1
            except:
                items_to_buy[d] = 1
            budget -= drinks[d]
            
        person = people_by_food[i]
        if len(person.food) > 0 and food[person.food[0]]<=budget:
            f = person.food.pop(0)
            print f
            try:
                items_to_buy[f] += 1
            except:
                items_to_buy[f] = 1
            budget -= food[f]
    budget -= 1
    
print items_to_buy
total_cost = 0
for key in items_to_buy:
    if key in food:
        cost = items_to_buy[key]*food[key]
    else:
        cost = items_to_buy[key]*drinks[key]
    print 'Cost for', key, 'is', cost
    total_cost += cost
print 'Total cost:',total_cost
print 'Amount left over:', budget

        
