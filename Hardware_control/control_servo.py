import curses
from gpiozero import Servo

# Set the pin numbers for the servos
servo_pin_x = 12
servo_pin_y = 13

# Set the minimum and maximum pulse widths (in seconds) for the servos
min_pulse_width = 0.5 / 1000  # 0.5 ms
max_pulse_width = 2.5 / 1000  # 2.5 ms

# Create Servo instances
servo_x = Servo(servo_pin_x, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)
servo_y = Servo(servo_pin_y, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Set initial target angles
    target_angle_x = 0
    target_angle_y = 0
    
    while True:
        # Display current angles and instructions
        stdscr.addstr(0, 0, "Servo X - Current angle: {:.1f} degrees".format(target_angle_x))
        stdscr.addstr(1, 0, "Press LEFT/RIGHT arrow keys to adjust angle (increments of 5 degrees)")
        stdscr.addstr(2, 0, "Servo Y - Current angle: {:.1f} degrees".format(target_angle_y))
        stdscr.addstr(3, 0, "Press UP/DOWN arrow keys to adjust angle (increments of 5 degrees)")
        stdscr.refresh()
        
        # Capture key press
        key = stdscr.getch()
        
        # Adjust target angles based on key press
        if key == curses.KEY_UP:
            target_angle_y = min(target_angle_y + 5, 90)
        elif key == curses.KEY_DOWN:
            target_angle_y = max(target_angle_y - 5, -30)
        elif key == curses.KEY_LEFT:
            target_angle_x = max(target_angle_x - 5, -45)
        elif key == curses.KEY_RIGHT:
            target_angle_x = min(target_angle_x + 5, 45)
        
        # Move servos to the new target angles
        servo_x.value = target_angle_x / 60
        servo_y.value = target_angle_y / 90

try:
    curses.wrapper(main)
except KeyboardInterrupt:
    # Clean up
    servo_x.close()
    servo_y.close()
