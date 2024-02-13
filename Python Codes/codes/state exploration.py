class item:
    def __init__(self, name:str, price:float, quantity:float=0) :
        
        assert price >=0, f"price {price} is not greater than zero"
        assert quantity>=0 ,f" quntity {quantity} is not greater than zero"
        
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def calculate_total_price (self):
        return self.price*self.quantity
        
        
        
item1= item("laptop",100,-9)
print (item1)
print (item1.calculate_total_price())
print 