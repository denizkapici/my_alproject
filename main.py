import operator

def add(x, y):
    return operator.add(x, y)

def subtract(x, y):
    return operator.sub(x, y)

def multiply(x, y):
    return operator.mul(x, y)

def divide(x, y):
    if y == 0:
        return 'Hata! Sıfıra bölme işlemini gerçekleştiremezsiniz.'
    else:
        return operator.truediv(x, y)

print('4 İşlem Hesap Makinesi')
print('1. Toplama')
print('2. Çıkarma')
print('3. Çarpma')
print('4. Bölme')

secim = input('İşlemi seçiniz (1/2/3/4): ')

if secim in ('1', '2', '3', '4'):
    num1 = float(input('İlk sayıyı giriniz: '))
    num2 = float(input('İkinci sayıyı giriniz: '))

    if secim == '1':
        print(num1, '+', num2, '=', add(num1, num2))

    elif secim == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))

    elif secim == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))

    elif secim == '4':
        print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Geçersiz işlem')
