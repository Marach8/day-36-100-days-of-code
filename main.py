import time, os
b = 'LIST OF NAMES'
print(f'\033[4m{b:^40}\033[0m')
time.sleep(1)
print()

main_list = []
def name():
  global main_list
  while True:
    ask1 = input('Enter Your First Name: ').capitalize().strip()
    time.sleep(1)
    ask2 = input('Enter Your Surname: ').capitalize().strip()
    full_name = f'{ask2} {ask1}'
    if full_name not in main_list:
      main_list.append(full_name)
      time.sleep(1)
      print()
      print('\033[32mData saved successfully!😎\033[0m')
      print()
      time.sleep(1.5)
      os.system('clear')
      time.sleep(2)
      printer()
      print()
    else:
      print()
      print('\033[31mThis name already exists!')
      print()
      time.sleep(2)
    querry = input('\033[0mWant to add another name? y/n: \033[0m').lower()
    if querry == 'y':
      print()
      continue
    else:
      break
  printer()
  print()
  print('\033[0mThese are the only names you have')


def printer():
  print()
  print('\033[4mSaved Names\033[0m')
  print()
  global main_list
  for i in range(len(main_list)):
    time.sleep(2)
    print(f'\033[36m{i+1}. \033[1;33m{main_list[i]}')

name()
