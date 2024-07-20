import mysql.connector
import tabulate

connections = mysql.connector.connect(
    host="localhost",
    user="naveen",
    password="pongal1V@da",
    database="baby_names"
)
mn = {
    "starting_letter": None,
    "ending_letter": None,
    "Category": None,
    "length": None,
    "gender": None
}
MN = {
    "starting_letter": 1,
    "ending_letter": 2,
    "Category": 3,
    "length": 4,
    "gender": 5
}

choices = []
mn['starting_letter'] = input("Enter the starting letter : ").upper()
mn['ending_letter'] = input("Enter the ending letter : ").lower()
mn['length'] = input("Enter the length of the name : ")
if mn['length'] != '':
    mn['length'] = int(mn['length'])
while True:
    mn['Category'] = input("1. Hinduism\n2. Christianity\n3. Islam\nEnter the category of the name :")
    if mn['Category'] == "1":
        mn['Category'] = "Hinduism"
        break
    elif mn['Category'] == "2":
        mn['Category'] = "Christianity"
        break
    elif mn['Category'] == "3":
        mn['Category'] = "Islam"
        break
    elif mn['Category'] == "":
        pass
        break
    else:
        print("Invalid input")
        continue
while True:
    mn['gender'] = input("Enter the gender(M or F) : ").upper()
    if mn['gender'] == "M":
        mn['gender'] = "Male"
        break
    elif mn['gender'] == "F":
        mn['gender'] = "Female"
        break
    elif mn['gender'] == "":
        pass
        break
    else:
        print("Invalid input")
        continue
choices.append(mn['starting_letter'])
choices.append(mn['ending_letter'])
choices.append(mn['Category'])
choices.append(mn['length'])
choices.append(mn['gender'])
choice = []
for i,j in mn.items():
    if j != '':
        choice.append(i)
choices = []
for i in choice:
    choices.append(MN[i])
choice = "".join(map(str,choices))

m = ["name like '{}%'".format(str(mn['starting_letter'])), "name like '%{}'".format(str(mn['ending_letter'])),"category = '{}' ".format(str(mn['Category']))
     , "char_length(name)={}".format(mn['length']),"gender = '{}'".format(str(mn['gender']))]
cursor = connections.cursor()
name = []
if len(choices) == 0:
    select_statement = "select * from names"
    cursor.execute(select_statement)
    names = cursor.fetchall()
    for i in names:
        data = [i[1],i[3]]
        name.append(data)
else:
    select_statement = "select * from names where"
    for i in choice:
        if len(choices) != 1:
            select_statement += " " + m[int(i)-1]
            select_statement += " " + "and"
            choices.remove(int(i))
        else:
            select_statement += " "+m[int(i)-1]
    cursor.execute(select_statement)
    result = cursor.fetchall()
    for i in result:
        data = [i[1],i[3]]
        name.append(data)
headers = ["Name","Category"]
table = tabulate.tabulate(name)
print(table)
