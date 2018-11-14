#第9章 类
class Dog( ):
	#一次模仿小狗的简单尝试
	
	def __init__(self , name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + 'is now sitting')
		
	def roll_over(self):
		"""打滚"""
		print(self_name.title( ) + 'rolled over' )