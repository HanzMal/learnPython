class Karyawan:
    pass

budi = Karyawan()

# Data ini didapat dinamis dari Form Website / API luar
input_dari_user = "alamat"
nilai_input = "Jakarta"

# Kamu tidak bisa tulis: budi.input_dari_user = nilai_input (nanti nama variabelnya malah jadi 'input_dari_user')
# Maka gunanya setattr:
setattr(budi, input_dari_user, nilai_input)

# Sekarang, objek budi otomatis punya properti alamat!
print(budi.alamat)  # Output: Jakarta
print(getattr(budi, input_dari_user))  # Output: Jakarta

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))

for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)): 
        value = getattr(person, attr)
        print(f'{attr}: {value}')

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token # sensitive
        self.temp_counter = 0 # temporary

session = UserSession(101, 'a1b2c3d4e5')

# List of attributes to remove dynamically before "saving" the session
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Loop through the remaining attributes with dir()
for attr in dir(session):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')
