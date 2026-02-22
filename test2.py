import os
from gpiozero import Button
from signal import pause

# 1. HARDWARE PINS (BCM Numbering)
VOL_UP_PIN = 23
VOL_DOWN_PIN = 24
POWER_PIN = 3  # Moved to the Master Wake-Up Pin!

# 2. AUDIO CONTROL FUNCTIONS
current_volume = 50 

def volume_up():
    global current_volume
    # Add 5, but use max() to prevent it from going over 100
    current_volume = min(100, current_volume + 5)
    print(f"🔊 Volume UP Triggered: Forcing to {current_volume}%")
    os.system(f"amixer set PCM {current_volume}%") 

def volume_down():
    global current_volume
    # Subtract 5, but use min() to prevent it from dropping below 0
    current_volume = max(0, current_volume - 5)
    print(f"🔉 Volume DOWN Triggered: Forcing to {current_volume}%")
    os.system(f"amixer set PCM {current_volume}%")

# 3. SAFE SHUTDOWN FUNCTION
def shutdown_pi():
    print("🛑 3-Second Hold Detected: SHUTTING DOWN...")
    # Safe shutdown command
    os.system("sudo shutdown -h now")

# 4. INITIALIZE BUTTONS
print("--- AURA Hardware Tester ---")
print("Press Vol Up (GPIO 23) or Vol Down (GPIO 24).")
print("Hold Power (GPIO 3) for 3 seconds to test shutdown.")

vol_up_btn = Button(VOL_UP_PIN, pull_up=True, bounce_time=0.1)
vol_up_btn.when_pressed = volume_up

vol_down_btn = Button(VOL_DOWN_PIN, pull_up=True, bounce_time=0.1)
vol_down_btn.when_pressed = volume_down

power_btn = Button(POWER_PIN, pull_up=True, hold_time=3.0)
power_btn.when_held = shutdown_pi

pause()