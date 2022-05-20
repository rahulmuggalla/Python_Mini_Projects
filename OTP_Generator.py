import random

print("Enter 1 if you want to create 4 digit OTP")
print("Enter 2 if you want to create 6 digit OTP")

digits = int(input("Enter 1 or 2: "))
if digits == 1:
    otp = random.randint(1000, 9999)
    print(str(otp))
elif digits == 2:
    otp = random.randint(100000, 999999)
    print(str(otp))
else:
    print("You can enter only 1 or 2")