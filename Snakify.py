Sum of three numbers

a = int(input())
b = int(input())
c = int(input())
print(a + b+c)


Hi John

N=input()
print('Hi ' +N)


Square

n=int(input())
print(n**2)


Area of a Right Triangle

a = int(input())
b = int(input())
print((a*b)/2)

Hellow Harry

name = input()
print('Hello,', name+'!')

Apple Sharing

n = int(input())
k = int(input())
print(k // n)
print(k % n)

Two Timestamps

hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
    - hours_1 * 3600 - minutes_1 * 60 - seconds_1)
    
School Desks

a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

Last digit of integer 

def last_digit(n):
    """Returns the last digit of n."""
    n = str(n)
    return int(n[len(n)-1])

print(last_digit(int(input("Which number? "))))

Tens Digit 

n = int(input())
print(n // 10 % 10)

Sum of Digits 

n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)

Fractional Part 

x = float(input())
print(x - int(x))

First Digit after decimal Point

x = float(input())
print(int(x * 10) % 10)

Car Route 

from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))

Digital Clock

n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)

Total Cost

a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)

Clock Face - 1

h = int(input())
m = int(input())
s = int(input())

print(h * 30 + m * 30 / 60 + s * 30 / 3600)

Clock Face - 2

alpha = float(input())
print(alpha % 30 * 12)