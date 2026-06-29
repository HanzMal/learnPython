class Wallet:
    nama_dompet = "GOPAY" # class attribute 

    def __init__(self, balance): # instance attribute
        self.__balance = balance # For internal use by convention

    # 1. GETTER: Mengubah method menjadi seolah-olah atribut biasa
    @property
    def balance(self):
        print("Log: Seseorang sedang mengintip saldo!")
        return self.__balance
    
    # 2. SETTER: Menyisipkan validasi saat seseorang mencoba mengubah nilai. bisa mengubah value properti langsung
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        print(f"Log: Saldo berhasil diubah menjadi {amount}")
        self._balance = amount
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # Add to the balance safely
        else:
            raise ValueError('Amount must be positive')
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
           self.__balance -= amount # Remove from the balance safely
        else:
            raise ValueError('Insufficient funds')
    
    # def get_balance(self): # buat mengakses 
    #    return self.__balance #ubah semuanya kasih double underscore sekalian

account1 = Wallet(500)
account1.deposit(50)
# print(account1.get_balance()) # 550

acct_two = Wallet(450)
acct_two.withdraw(28)
# acct_two.withdraw(500) # ValueError: Insufficient funds
print("saldo acct_two: ", acct_two.balance)
# print(acct_two.get_balance()) # 422
# print(account1._balance) # masih bisa diakses
# print(account1.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'. Did you mean: '_balance'?