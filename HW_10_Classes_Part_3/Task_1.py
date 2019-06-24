import pprint 


class Auto(object):
	def __init__(self, eng_capacity, mileage, color, max_speed, max_fuel_supply, price):
		self.eng_capacity = eng_capacity
		self.mileage = mileage
		self.color = color
		self.max_speed = max_speed
		self.max_fuel_supply = max_fuel_supply
		self.price = price

	def __repr__(self):
		return 'Auto(eng_capacity={}, mileage={}, color={}, max_speed={}, ' \
		            'max_fuel_supply={}, price={})' \
		            .format(self.eng_capacity, self.mileage, self.color, self.max_speed, \
		            	    self.max_fuel_supply, self.price)

	def __gt__(self, other):
		if self.price > other.price:
			return True
		if self.price == other.price and \
		   self.eng_capacity > other.eng_capacity:
			return True
		if self.price == other.price and \
		   self.eng_capacity == other.eng_capacity and \
		   self.max_fuel_supply > other.max_fuel_supply:
			return True
		return False


autos = [Auto(38, 20001, 'red', 280, 50, 3600),
         Auto(41, 20002, 'red', 280, 45, 1200),
         Auto(38, 20003, 'red', 280, 60, 3500),
         Auto(35, 20004, 'red', 280, 40, 6000),
         Auto(38, 20005, 'red', 280, 55, 3500),
         Auto(38, 20006, 'red', 280, 35, 1100),
         Auto(40, 20006, 'red', 280, 37, 1100)]

pprint.pprint(sorted(autos))