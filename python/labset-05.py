num = int(input("Enter a numerator: "))
den = int(input("Enter a denominator: "))
try:
    result = num / den
    print(f"Result: {num} / {den} = {result}")
except ZeroDivisionError:
    print("Division by zero not allowed")
 
 
  
