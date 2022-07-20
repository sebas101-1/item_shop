inv_items = {"thorn":{"rarity": "50", "value": "50"},"excalibur":{"30": "excalibur", "value": "45 "},"march":{"rarity": "20", "value": "40 "}}
item_keys = ["thorn","march","excalibur"]
# print(items)
c= "" #runs while loop

def menu():
  print("Item Inventory")
  print("--------------")
  print("A-Add")
  print("R-Remove")
  print("E-Edit")
  print("L -List items names")
  print("D- list details of items")
  print("Q-quit")
while (c != "Q" or c != "q"):
  
  menu()
  c = input("what will you do? ")
  if(c == "q" or c == "Q"):    
    break
  elif(c=="A" or c=="a"):
    item_name = input("Enter item name ")
    exist = False
    for key, value in inv_items.items():
      if (item_name in item_keys):
        exist = True
      if(exist):
        print("that item already exists")
        break
      else:
        item_value = float(input("Enter Value "))
        item_rarity = float(input("Enter rarity "))
        inv_items[item_name] = {}
        inv_items[item_name]["value"] = item_value
        inv_items[item_name]["rarity"] = item_rarity
        item_keys.append(item_name)
        print("------")
        print("item was added")
        break
  elif(c=="R" or c=="r"):
    there = False
    remove_item = input("Which item would you like to remove ")
    if (remove_item in item_keys):
        there = True
    else:
      print("Item doesnt exist ")
    if(there == True):
      del inv_items[remove_item]
      item_keys.remove(remove_item)
      print("item removed")
      print(item_keys)
  elif(c=="L"or c=="l"):
    for i in range(len(item_keys)):
      print("-----------------")
      print(item_keys[i-1])
    print("-----------------")
  elif(c=="D" or c=="d"):
    print("printing items")
    for k,v in inv_items.items():
      print("--------------------")
      print("Item ", k)
      for k in v:
        print(k + ":", v[k])
      print()
  
  elif(c=="E"or c=="e"):
    there = False
    edit_item = input("which item? ")
    if (edit_item in item_keys):
      there=True
    if there == False:
      print("this item doesnt exist")
    if there == True:
      name = input("new item name ")
      item_value = float(input("Enter Value "))
      item_rarity = float(input("Enter rarity "))
      del inv_items[edit_item]
      item_keys.remove(edit_item)
      item_keys.append(name)
      inv_items[name] = {}
      inv_items[name]["value"] = item_value
      inv_items[name]["rarity"] = item_rarity
      print("Item edited")
      print(item_keys)
  else:
    print("non-existent command")
print("quiting")    