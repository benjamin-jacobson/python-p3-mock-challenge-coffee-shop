class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
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
        return [o for o in Order.all if o.coffee is self]
    
    def customers(self):
        '''Returns a unique list of all customers who have ordered a particular coffee.Customers must be of type Customer'''
        return list({o.customer for o in Order.all if o.coffee is self})
    
    # def num_orders(self): # TODO ben solution, below is simpler
    #     '''Returns the total number of times a coffee has been ordered
    #         Returns 0 if the coffee has never been ordered
    #     '''
    #     if self.orders() == []:
    #         return 0
    #     else:
    #         return len(self.orders())

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self): # TODO ben solution, below is simpler
        '''Returns the average price for a coffee based on its orders
            Returns 0 if the coffee has never been ordered
        '''
        if self.orders() == []:
            return 0
        else:
            return  sum([o.price for o in Order.all if o.coffee is self]) / len(self.orders())

    # def average_price(self):
    #     return mean([order.price for order in self.orders()])

# class Customer:
#     all = [] # BEN this failed on the mutable string test due to _ use
#     def __init__(self, name):
#         self._name = name
#         type(self).all.append(self)

#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,name):
#         if isinstance(name,str) and (1 >= len(name) >=15):
#             self._name = name
        # else:
        #     raise Exception("Name property should be string and 0-15 characters")

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    def orders(self):
        '''Returns a list of all orders for that customer. Orders must be of type Order'''
        return [o for o in Order.all if o.customer is self]
    
    def coffees(self):
        '''Returns a unique list of all coffees a customer has ordered.Coffees must be of type Coffee'''
        return list({o.coffee for o in Order.all if o.customer is self})
    
    def create_order(self, coffee, price):
        '''Receives a coffee object and a price number as arguments
            Creates and returns a new Order instance and associates it with that customer and the coffee object provided.
        '''
        return Order(self,coffee,price)  # TODO seems wrong
    

    @classmethod
    def most_aficionado(cls, coffee): # Note this is solution code
        '''Receives a coffee object argument
            Returns the Customer instance that has spent the most money on the coffee instance provided as argument.
            Returns None if there are no customers for the coffee instance provided.'''
        # if not isinstance(coffee, Coffee):
        #     raise Exception
        if coffee_all_orders := [
            order for order in Order.all if order.coffee is coffee
        ]:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)


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