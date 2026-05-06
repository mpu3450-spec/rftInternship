#DICTIONARY BASED PHONEBOOK
#create a dictionary & prevent duplicate entry
book = {}
n = int(input("number of entries in dictionary:"))
for i in range(n):
    key = input("enter key:").upper()
    if key in book:
        print("contact already exist")
        continue
    book[key] = input("enter phone number:")
print(book)    

#search
search = input("enter contact:").upper()
for key in book:
    if book[key] == search:
        print("FOUND",key,":",book[key])

#delete a contact
delete_key = input("enter key to be deleted:").upper()
if delete_key in book:
    del book[delete_key]
    print("dictionary after deletion:",book)
else:
    print("key not found")    

#partial name search
partial = input("enter partial name to search:").upper()
if partial in key:
        print(f"{partial} in:",key," ",book[key])
else:
        print("NOT FOUND")    