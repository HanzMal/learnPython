# dictionary => key-value pair
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

pempek_kapal_selam = dict([('name', 'Kapal Selam'), ('price', 5.9), ('calories_per_slice', 250), ('toppings', ['Cuko', 'Timun'])])
print('pempek1', pempek_kapal_selam)

# akses value
isi_value = pempek_kapal_selam['name']
print('nama pempek:', isi_value)

isi_value2 = pempek_kapal_selam.get('toppings', []) # get bisa dikasih nilai default yaitu [] atau bisa lainnya
print(isi_value2)

print('keys', pempek_kapal_selam.keys()) # keys dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
print('values', pempek_kapal_selam.values()) # values dict_values(['Kapal Selam', 5.9, 250, ['Cuko', 'Timun']])
print('items', pempek_kapal_selam.items())

# items
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
print(products.items())

# looping value price
for price in products.values():
    print("price", price)

# looping key products
for product in products.keys():
    print("product", product)

# looping key - value products
for productItem in products.items():
    print("productItem", productItem)

# discount 30% untuk setiap product
for product, price in products.items():
    products[product] = round(price * 0.7)

print(products)