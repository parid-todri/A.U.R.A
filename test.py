from gpiozero import Button
from signal import pause

print("--- AURA HARDWARE DIAGNOSTIC ---")
print("Waiting for button presses... (Press Ctrl+C to exit)")
print("--------------------------------")

# Dictionary mapping your BCM GPIO Pins to the Emotion
BUTTON_MAP = {
    5:  "HAPPINESS (I Lumtur)",
    6:  "SADNESS (I Trishtuar)",
    13: "ANGER (I Zemëruar)",
    19: "FEAR (I Frikësuar)",
    26: "ANXIETY (Në Ankth)",
    12: "FRUSTRATION (I Frustruar)",
    16: "EXCITEMENT (Shumë Energji)",
    20: "OVERWHELM (Mbingarkesë)",
    21: "CANCEL/RESET",
    23: "VOLUME UP",
    24: "VOLUME DOWN"
}

def on_press(btn):
    # This grabs the pin number of the button that was just pressed
    pin_num = btn.pin.number
    emotion = BUTTON_MAP.get(pin_num, "Unknown")
    print(f"✅ SUCCESS: GPIO {pin_num} triggered -> {emotion}")

# Keep track of the active buttons so they don't get garbage collected
active_buttons = []

# Loop through our map and activate the pins
for pin, name in BUTTON_MAP.items():
    try:
        # pull_up=True means we expect the button to connect the pin to Ground
        btn = Button(pin, pull_up=True)
        btn.when_pressed = on_press
        active_buttons.append(btn)
        print(f"Listening on GPIO {pin}...")
    except Exception as e:
        print(f"❌ ERROR on GPIO {pin}: {e}")

# This keeps the script running endlessly until you stop it
pause()