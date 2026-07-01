class Motorcycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.model} engine started.")

class Yamaha(Motorcycle):
    identity = "has two cycles"
    def __init__(self, model):
        super().__init__("Yamaha", model)

    # def start_engine(self):
    #     print(f"{self.brand} {self.model} engine roars to life!")

    def start_engine(self):
        base = super().start_engine()
        print(f"{base}, {self.model} engine roars to life!")

vegaR = Yamaha("Vega R")
vegaR.start_engine()  # Output: Yamaha Vega R engine roars to life!
print("vegaR", vegaR.identity)  # Output: has two cycles