number1 = 0 
number2 = 1
number3 = 0

typedNumber = int(input('Digite um numero: \n'))

while typedNumber > number3:
    number3 = number1 + number2
    number1 = number2
    number2 = number3

if (typedNumber == 0 or typedNumber == 1):
    print('O numero %i esta na sequencia de Fibonacci' % typedNumber)
elif (typedNumber == number3):
    print('O numero %i esta na sequencia de Fibonacci' % typedNumber)
else:
    print('O numero %i NAO esta na sequencia de Fibonacci' % typedNumber)

