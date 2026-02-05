"""
Nihar patel
fab 5, 2026
ET 721
lab 4
"""

print ("\n ------ Example 1: ") 
contacts= {
    'Bill': '718-111-2222',
    'Rick': '718-000-1111',
    'Mary': '800-222-3333'
}
print(f"original dictionary{contacts}")

contacts ['Rick'] = '347-000-1111'
print (f"update dictionary {contacts}")
contacts['Peter'] = '888-000-1111'
print (f"update dictionary with new pair = {contacts}")
print ("\n ------ Example 2:  loop through a dictinary")
for v in contacts:
    print(v)

for v in contacts:
    print(contacts[v])

for v in contacts:
    print (f'{v} phone number is contacts[v]')

print ("\n ------ Example 3:  item(), Keys(), methods(), in dictinary")
print (f" all key o nthe dictionary {contacts.items()}")
print (f"all keys in dictinary {contacts.keys()}")
print (f"all keys in dictinary {contacts.values()}")

print ("\n ------ Example 4:  Check if key is 'in or 'not in' dictionary") 
check_name = 'Lucky'
chekc = check_name in contacts
print (f"is {check_name} in the dictinary")

print ("\n ------ Example 5: length of dictinary" ) 
print (f"contacts has {len(contacts)} Key-value pairs")

print ("\n ------ Example 6:  rempmove pairs") 
print (f"original dictionary ={contacts}")
contacts.pop ('Mary')
print(f"update disctionary = {contacts}")

print ("\n ------ Example 7: get method")
print (f"Key-value pair = {contacts.get('Bill')}")

print ("\n ------ Example 8: update method") 
contacts.update({'Annie' : '718-888-9999'})
print(f"{contacts}")

print ("\n ------ Exercise") 

