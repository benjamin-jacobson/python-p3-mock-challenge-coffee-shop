class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and not hasattr(self, "name") and len(name) >=3:
            self._name = name
        # else:
        #     raise Exception("Name property should be string and 0-15 characters. NAme should not already be set.")
        
    def orders(self):
        '''Returns a list of all orders for that coffee. Orders must be of type Order'''
        return [o for o in ]
    
    def customers(self):
        '''Returns a unique list of all customers who have ordered a particular coffee.Customers must be of type Customer'''
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    all = []
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and (1 >= len(name) >=15):
            self._name = name
        # else:
        #     raise Exception("Name property should be string and 0-15 characters")
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self,price):
        if isinstance(price,float) and not hasattr(self,"price") and (1.0<= price <= 10.0):
            self._price = price 

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self,customer):
        if isinstance(customer,Customer):
            self._customer=customer

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self,coffee):
        if isinstance(coffee,Coffee):
            self._coffee = coffee