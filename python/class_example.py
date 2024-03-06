from dataclasses import dataclass

@dataclass
class Customer():
    name: str
    age: int
    
    def delete_customer(self):
        print("Customer deleted")
    
    def show_customer(self):
        print(self.name, self.age)

if __name__ == "__main__":

    first_customer = Customer("Serkan", 25)
    first_customer.show_customer()