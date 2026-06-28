class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)
   
cart1 = Cart() #instance object cart
cart1.add("Book")
cart1.add("Laptop")
cart1.add('Wireless mouse')

cart2 = Cart()
cart2.add('Ergo keyboard')
cart2.add('Monitor')

for item in cart1:
   print("cart 1", item, end=' ')

print("\n")

for item in cart2:
   print("cart 2", item, end=' ')