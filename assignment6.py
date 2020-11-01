"""
Matthew Dawson
Module 6 HW
11/01/20
mjdawson@uno.edu
"""

import sys
import json

#open the input json file with context manager
with open("input.json", "r") as input:
    #load the json data to the customers (as a dictionary)
    customers = json.load(input)

#are all customer numbers unique? 
#initiate the temp list
temp = []
#loop through each value in the custoners dictionary "clients" key
for value in customers["clients"]:
    #appen the clients id to the temp list
    temp.append(value["id"])

#add values to set, eliminating duplicate values
unique = set(temp)
#add value to tuple, convert temp list to tuple
original = (temp)

#if the length of teh set is not equal to the length of the tuple, that means we have duplicate ids
if len(unique) != len(original):
    print("There are duplicate id numbers in the data, exiting!!")
    sys.exit()
#else all the ids are unique
else:
    print("All customer ids are unique!!!")

"""
1. 
Create a set of each customer email and test for uniqueness
"""
#initiate the emails list
emails = []
#loop through each value in the custoners dictionary "clients" key
for value in customers["clients"]:
    #append the clients emails to the emamils list
    emails.append(value["email"])

#add values to set, eliminating duplicate values
emails_unique = set(emails)
#add value to tuple, convert emails list to tuple
emails_original = (emails)

#if the length of the set is not equal to the length of the tuple, that means we have duplicate ids
if len(emails_unique) != len(emails_original):
    print("There are duplicate emails in the data, exiting!!")
    sys.exit()
#else all the ids are unique
else:
    print("All customer emails are unique!!!")

"""
2.
Create a dictionary of each cusomter, each one should 
contain the name and email of each customer
write this as JSON to a new file called email_list.json
"""
#initiate customer dict
customers_dict = {}
#initiate the list of dictionaries inside customers_dict
customers_dict["customers"] = []

#initiate email dict (one for each customer)
email_dict = {}

#loop through input customers dict and add names and emails to new dict
for value in customers["clients"]:
    email_dict["name"] = value["name"]
    email_dict["email"] = value["email"]
    customers_dict["customers"].append(email_dict)

#write to json file
with open("email_list.json", "w") as write_file:
    json.dump(customers_dict, write_file)


"""
3.
open the original file again, this time set each male
customers isActive status to false
write this new data to a file called current_customers
"""
#reopen the input json file with context manager
with open("input.json", "r") as input:
    #load the json data to the new_customers (as a dictionary)
    new_customers = json.load(input)

for value in new_customers["clients"]:
    if value["gender"] == "male":
        value["isActive"] = False

#write to json file
with open("current_customers.json", "w") as write_file:
    json.dump(new_customers, write_file)
