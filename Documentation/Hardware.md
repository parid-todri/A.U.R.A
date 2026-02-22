# Hardware Documentation

## Core Components
- Raspberry Pi 4
- 7” LCD Display
- 8 Mechanical Buttons
- 25,000 mAh Battery
- Headphones

## GPIO Pin Mapping# Hardware Documentation

## 1. Core Components

- Raspberry Pi 4 (4GB recommended)
- 7” HDMI LCD Display
- 8 Industrial Mechanical Buttons
- 25,000 mAh Battery Pack
- Audio Headphones
- GPIO Wiring (Pull-Up Config)

---

## 2. GPIO Mapping Example

Button 1 → GPIO17
Button 2 → GPIO27
Button 3 → GPIO22
Button 4 → GPIO5
Button 5 → GPIO6
Button 6 → GPIO13
Button 7 → GPIO19
Button 8 → GPIO26

Each button:
GPIO Pin → Button → GND

Internal pull-up enabled.

---

## 3. Electrical Design Notes

- Shared ground across system
- Active LOW logic
- Debounce handled in software
- Voltage: 3.3V GPIO safe range

---

## 4. Power Management

Battery:
- 5V output
- USB-powered Pi
- Minimum 3A current recommended

Safety:
- Insulated connections
- Strain relief for wires
- No exposed conductive elements

---

## 5. Mechanical Integration

Buttons mounted on strap for ergonomic access.
LCD mounted on rear for adult visibility.
Internal mounting protects Raspberry Pi from impact.

Example:
Button 1 → GPIO17
Button 2 → GPIO27
Button 3 → GPIO22
...

## Wiring Configuration
- Internal Pull-Up enabled
- Button connects GPIO → GND when pressed
- Active LOW logic

## Power Supply
- 5V battery via USB
- Common ground shared across system

## Safety
- Insulated wiring
- Secure button mounting
- Battery protection