#!/home/sasha/anaconda3/bin/python

str = '((((((((((((((2, 3)))))))))))))'
balance = 0

for skobka in str:
    if  skobka == '(':
        balance = balance +1 # цикл проходить по рядку і шукає наші скобочки, додаючи за кожну ( скобочку +1 в змінну balance
    elif skobka ==')': 
        balance = balance -1 # тепер шукає іншу скобочку і віднімає 1 за кожну
if balance == 0:
    print('Parenthesis is balanced')

else:
    print("Well you can clearly see that this %s is not  balanced " % str)
