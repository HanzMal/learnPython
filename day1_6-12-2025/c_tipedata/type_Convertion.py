integer_number = 123 #awalnya integer
float_number = 1.23 #ini float

new_number = integer_number + float_number # otomatis berubah jadi float

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

num_string = '12'
num_integer = 23

#Explicit type convertion
print("Data type of num_string before Type Casting:",type(num_string)) #string

# explicit type conversion
num_string = int(num_string) #become integer

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string #still integer

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

num = int(input('Enter a number: '))
