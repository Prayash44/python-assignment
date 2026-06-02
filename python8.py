angles = [30, -15, 45, 200, 60, 90]

def check(angle):
    return angle >= 0 and angle <= 180

valid_angles = list(filter(check, angles))

def servo(angle):
    return angle * 10

servo_commands = list(map(servo, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)