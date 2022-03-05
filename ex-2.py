import json

users = []

def getUser():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    return { "name": name, "age": age }

def searchUsers(searchedName: str): 
    for item in users:
        if(item['name'] == searchedName):
            return item['age']
    return 'User does not exist!!'

def main():
    userCount = int(input("Enter user Count : "))
    
    for i in range(0, userCount):
        users.append(getUser())

    searchedName = input('Enter the name you wanna search : ')
    print(searchUsers(searchedName))

main()