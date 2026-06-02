def gcd_lcm(num1, num2):
    # Store original values for LCM calculation
    a, b = num1, num2
    
    
    while b > 0:
        a, b = b, a % b
    gcd_result = a
    
    # LCM = (num1 * num2) / GCD
    lcm_result = (num1 * num2) // gcd_result
    
    return gcd_result, lcm_result

# Execution
first_val = int(input("Enter first integer: "))
second_val = int(input("Enter second integer: "))

gcd, lcm = gcd_lcm(first_val, second_val)
print("Greatest Common Divisor (GCD): ",gcd)
print("Least Common Multiple (LCM): ",lcm)