#P94 创建字典列表

#创建一个用于存储外星人的空列表
aliens = [ ];

#创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

#改变前三个外星人的值
for alien in aliens[:3]:
	alien['color'] = 'yellow'
	alien['points'] = 10
	alien['speed'] = 'fast'

#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print('........')

#显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))