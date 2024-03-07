from dataclasses import dataclass


class Customer():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Customer deleted")
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

    def delete_customer(self):
        print("Customer deleted")
    
    def show_customer(self):
        print(self.name, self.age)

if __name__ == "__main__":

    first_customer = Customer("Serkan", 25)
    print(first_customer)