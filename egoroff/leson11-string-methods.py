print('oke'.upper()) #OKE
print('oke111'.upper()) #OKE111
print('OMG'.lower()) #omg
a = 'hello'
print(a.upper())#HELLO
print(a.lower())#hello
print('something'.count('t'))#1
print('puma'.count('a', 2))#1
print('something'.count('f', 1, 7))#0
print(a.find('l'))#2
print(a.rfind('o'))#4
print(a.replace('o', '!!!!!!!!!!!!!'))#hell!!!!!!!!!!!
print(a.isalpha())#True
print('100'.isdigit())#True
b = '88000050035'
print(int(b))#88000050035
l = '875'
print(l.rjust(5))875
n = 'bomzh bomzhov bomzhevich'
print(n.split())#'bomzh', 'bomzhev', 'ch'
print(len(n.split()))#3
print(n.split('i'))#'bomzh bomzhov bomzhev', 'ch'
