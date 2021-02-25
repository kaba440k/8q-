pi=float(3.14)
def summa_3(a, b, c):
  return a + b + c
  
def schet_bukv(line):
  schet=0
  for char in line:
      if char.isalpha():
          schet+=1
  return schet

def proizvedenie(n, m):
  return n * m

def delenie(y, h):
  return y / h

def S_kruga(x):
  return (x ** 2) * pi

def hypotenuse(l, o):
  return (l**2)+(o**2)

def S_sfery(r):
  return 4*pi*(r**2)

def calсulate_fibonacci(first_number, iterationsCount):
  result = [first_number, 1 ]
  while not len(result) == iterationsCount:
    last_number = len(result) - 1
    next_number = result[last_number] + result[last_number - 1] 
    result.append(next_number)
  return result


file_data =open('parametrs.txt', 'r') #['sum 10 10 5', 'chars df12312312tdfyt', 'multi 10 10 12', 'chars jkgbjh', 'chars', 'fibonacсi 1 7']
#input_file = file_data # = open("file_data", 'r')
for line in file_data: #input_file:
  try:
    parametrs=line.split()  
    command = parametrs[0] 
    if command == 'sum':
      summ=summa_3(int(parametrs[1]), int(parametrs[2]), int(parametrs[3]))
      print(f'Сумма: {summ}')

    elif command == 'chars':
      if len(parametrs) < 2:
        raise Exception(f'Command {parametrs[0]} no parametr') 
      char_count=schet_bukv(parametrs[1])
      print(f'Кол-во букв: {char_count}')

    elif command == 'fibonacci':
      fibonacci=calсulate_fibonacci(int(parametrs[1]), int(parametrs[2]))
      print(f'Fibonacci: {fibonacci}')

    elif command =='multi':
        proizvedenie=proizvedenie(int(parametrs[1]), int(parametrs[2]))
        print(f'Произведение : {proizvedenie}')

    elif command =='delenie':
        div=delenie(int(parametrs[1]), int(parametrs[2]))
        print(f'Результат деления: {div}')

    elif command =='S_kruga':
        ploshad=S_kruga(int(parametrs[1]))
        print(f'Площадь круга: {ploshad}')

    elif command =='hypotenuse':
        hypotenuse=hypotenuse(int(parametrs[1]), int(parametrs[2]))
        print(f'Гипотенуза: {hypotenuse}')

    elif command == 'S_sfery':
        S_sfery=S_sfery(int(parametrs[1]))
        print(f'Площадь сферы: {S_sfery}')

    

    else:
      raise Exception(f'Command {parametrs[0]} not found')     
  except Exception as e:
    print(f'#ERROR: In {line} : {e}')