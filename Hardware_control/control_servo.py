from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

SERVO_MIN_ANGLE = -90
SERVO_MAX_ANGLE = 90
SERVO_MIN_PULSE_WIDTH = 1000000
SERVO_MAX_PULSE_WIDTH = 2000000

# Function to convert angle to pulse width
def angle_to_pulse_width(angle):
    return SERVO_MIN_PULSE_WIDTH + int((angle - SERVO_MIN_ANGLE) / (SERVO_MAX_ANGLE - SERVO_MIN_ANGLE) * (SERVO_MAX_PULSE_WIDTH - SERVO_MIN_PULSE_WIDTH))

# Setup servo pins
pin_x = 26
pin_y = 18
pwm_x = PWM(Pin(pin_x))
pwm_y = PWM(Pin(pin_y))

pwm_x.freq(50)
pwm_y.freq(50)
pwm_x.duty_ns(MID)
pwm_y.duty_ns(MID)

# Function to move servo to a specified angle
def move_to_angle(servo, angle):
    if servo == 'x':
        pwm = pwm_x
    elif servo == 'y':
        pwm = pwm_y
    else:
        print("Invalid servo selection")
        return
    
    pulse_width = angle_to_pulse_width(angle)
    pwm.duty_ns(pulse_width)

# Move both motors to specified target angles
def move_to_target_angles(target_angle_x, target_angle_y):
    move_to_angle('x', target_angle_x)
    move_to_angle('y', target_angle_y)

# Get target angles from user input
def get_target_angles_from_input():
    while True:
        try:
            target_angle_x = float(input("Enter target angle for X (-90 to 90 degrees): "))
            target_angle_y = float(input("Enter target angle for Y (-90 to 90 degrees): "))
            if -90 <= target_angle_x <= 90 and -90 <= target_angle_y <= 90:
                return target_angle_x, target_angle_y
            else:
                print("Angles must be between -90 and 90 degrees")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example: Move motors to user-specified angles
if __name__ == "__main__":
    target_angle_x, target_angle_y = get_target_angles_from_input()
    move_to_target_angles(target_angle_x, target_angle_y)

