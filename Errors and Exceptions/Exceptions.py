T=int(input())

try:
    for _ in range(T):
        a, b = map(int, input().split())
        div=a//b
        print(div)

except ValueError:
    print("Error Code: invalid literal for int() with base 10: '$'")
    
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")