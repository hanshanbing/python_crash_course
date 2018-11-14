﻿#第9章 类
class Car():
	"""汽车类"""
	
	def __init__(self, make, model, year):
		"""初始化汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name
	
	def read_odometer(self):
		"""打印里程信息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()