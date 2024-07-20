import mysql.connector
import tabulate
connections = mysql.connector.connect(
    host="localhost",
    user="naveen",
    password="pongal1V@da",
    database="baby_names"
)
mn = {
    "starting_name": None,
    "ending_name": None,
    "Category": None,
    "length": None,
    "gender": None
}

print("Note:")
print("you can choose one or more choices but To view all tha name you cannot choose other choices")
print("\n")
choice = int(input("1.starting_name\n2.ending_name\n3.category\n4.length\n5.gender\nEnter your choice:\t"))
choices = []
for i in str(choice):
    if i not in choices:
        choices.append(int(i))
if 1 in choices:
   mn['starting_name']\
       = input("Enter the starting letter : ").upper()
if 2 in choices:
    mn['ending_name'] = input("Enter the ending letter : ").lower()
if 4 in choices:
    mn['length'] = int(input("Enter the length of the name : "))
if 3 in choices:
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
        else:
            print("Invalid input")
            continue
if 5 in choices:
    while True:
        mn['gender'] = input("Enter the gender(M or F) : ").upper()
        if mn['gender'] == "M":
            mn['gender'] = "Male"
            break
        elif mn['gender'] == "F":
            mn['gender'] = "Female"
            break
        else:
            print("Invalid input")
            continue
m = ["name like '{}%'".format(str(mn['starting_name'])), "name like '%{}'".format(str(mn['ending_name'])), "category = '{}'".format(str(mn['Category']))
    , "char_length(name)={}".format(mn['length']),"gender = '{}'".format(str(mn['gender']))]

cursor = connections.cursor()
data  = []
select_statement = "select * from names where"
for i in str(choice):
    if len(choices) != 1:
        select_statement += " " + m[int(i)-1]
        select_statement += " " +"and"
        choices.remove(int(i))
    else:
        select_statement += " " + m[int(i)-1]
cursor.execute(select_statement)
names = cursor.fetchall()
connections.commit()
for i in names:
    name = [i[1],i[3]]
    data.append(name)
table = tabulate.tabulate(data,headers = ["Name","Category"])
print(table)

