# FreeStyle Engineering Challenge

You are planning a party for an arbitrary number of people and you need to buy drinks and food. Assume you’re given a budget (integer) and 3 files: 'people.txt', 'drinks.txt', 'food.txt'.

'people.txt' contains an arbitrary number of people with their preferred drinks and food; each entry will be 3 lines long (1st line: name (not unique), 2nd line: drinks (comma delimited, not sorted), 3rd line: food (comma delimited, not sorted). 

'drinks.txt' and 'food.txt' are arbitrarily large and each entry will be 1 line long in the following format: <drink or food name>:unit cost

Design and implement an algorithm that reads in the files and selects what drinks and foods you should purchase within your budget based on the information in the files. Be creative in how you optimize for food and drinks based on the known preferences.

Your answer should include an explanation of your algorithm, test cases, and a statement of all the assumptions you've made.

# Running

Run main.py with no arguments for default input values

one argument: (float) budget_size

or with three arguments: (float) budget_size, food_file_name, and drinks_file_name

# Dependency

Food and Drinks text files should be formatted in the following way:

food1:1

food2:2.5

...with no space next to the colon.

People text files should be formmated as:

Person Name

drink1,drink2,drink3

food1,food2,food3

...with no space after commas. 

However, in both cases, it's allowed to have a space in the item name. For example:

chicken sandwich:10

...is acceptable formatting.

