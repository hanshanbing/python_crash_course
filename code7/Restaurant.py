#第9章 类
class Restaurant():
	"""创建餐厅类"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		
	def describe_restaurant(self):
		print(self.name.title())
		print(self.type.title())
	
	def open_restaurant(self):
		print("The restaurant in open!")
		
my_restaurant = Restaurant("han","su")
my_restaurant.describe_restaurant( )
my_restaurant.open_restaurant( )