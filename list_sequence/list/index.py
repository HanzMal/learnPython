cities = ["Sleman", "Bantul", "Yogyakarta", "Gunungkidul", "Kulon Progo"]
print(cities[-1])

name = "Jokowi"
nameList = list(name)
print(nameList)

# lists are mutable, you can update any element in the list as long as you pass in a valid index number. If you pass in an index (either positive or negative) that is out of bounds for the list, then you will receive an IndexError
# cities[10] = "Surabaya" error karena ga sampai indeks 10 di cities
print(cities)

# destructuring list
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
print(name)
print(age)
print(job)

# The last concept we will look at is the slice operator (:). Similar to strings, you can access portions of a list by using the slice operator 
liverpoolLegend = ['Salah', 'Mane', 'Firmino', 'Henderson', 'Gerrard']
print(liverpoolLegend[1:4]) # ['Mane', 'Firmino', 'Henderson']

# method yang paling sering ada di python
liverpoolLegend.append('Van Dijk')
print(liverpoolLegend)

legend2 = ["Fowler", "Mcmanaman"]
liverpoolLegend.extend(legend2) #menggabungkan 2 array
print(liverpoolLegend)

numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned
numbers.pop(2)
print(numbers) #[1,2,4]