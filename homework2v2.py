#!/home/sasha/anaconda3/bin/python

str = '((((((((((((((2, 3)))))))))))))'
string_lenght = len(str)# рахуємо довжину рядка і записуємо в змінну

a = '('
b = ')'

left_side_amount = str.count(a, 0, string_lenght)
right_side_amount = str.count(b, 0, string_lenght) # раїуємо кількість одних і других дужок в рядку і результат записуєм в змінні

if left_side_amount == right_side_amount: # порівнюємо змінні і виводимо відповіне до результату повідомлення
    print('Parenthesis is balanced')
else:
    print('Parenthesis is not balanced')


