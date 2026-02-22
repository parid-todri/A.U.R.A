# AURA – Intelligent Therapeutic Backpack (AAC System)

## Overview

AURA is a wearable Assistive Augmentative Communication (AAC) system designed for children with Autism Spectrum Disorder (ASD) or sensory overload challenges. Integrated into a standard backpack, AURA enables instant emotional communication and real-time co-regulation during high-stress situations.

The system is built around a Raspberry Pi 4 and uses 8 mechanical tactile buttons for zero-cognitive-load activation.

---

## Problem Statement

During sensory overload, many children temporarily lose access to verbal communication. Traditional AAC tools (PECS cards or tablets) often fail in crisis moments due to:

- High cognitive load  
- Complex navigation  
- Screen dependency  
- Fine motor skill requirements  

AURA addresses this gap by providing a tactile, immediate-response communication system.

---

## System Architecture

**Input**
- 8 Mechanical Tactile Buttons (GPIO-based)

**Processing**
- Raspberry Pi 4  
- Python Software (Tkinter + Pygame)  
- Headless Linux Mode  
- Hybrid RAM Cache Architecture  

**Outputs**
- Audio Output (Headphones – calming therapy + guided prompts)
- Visual Output (Rear LCD – emotional state display for adults)

---

## Hardware Components

- Raspberry Pi 4  
- 7” LCD Display  
- 8 Mechanical Arcade Buttons  
- 25,000 mAh Battery Pack  
- Headphones  
- GPIO Wiring with Internal Pull-Up Configuration  

---

## Software Stack

- Python 3  
- Tkinter (GUI handling)  
- Pygame (Audio engine)  
- RPi.GPIO / lgpio  
- Headless Linux environment  

---

## Key Technical Features

### Hybrid RAM Cache
Custom memory optimization system:
- Preloads critical audio assets into RAM
- Dynamically loads/unloads visual assets
- Prevents Linux OOM Killer crashes

### GPIO Cleanup Protection
- Automatic GPIO release on exit
- Process cleanup logic
- Prevents “GPIO Busy” errors

### Auto-Reset System
- Returns to “Ready State” after 60 seconds
- Prevents overstimulation
- Conserves battery life

---

## Performance

- ~0.1 second response latency  
- Stable under repeated activation testing  
- Headless boot for fast startup  

---

## Emotional Button Mapping (Example)

1. Anxiety  
2. Frustration  
3. Pain  
4. Cold  
5. Thirst / Hunger  
6. Toilet  
7. Need a Break  
8. Help  

---

## Future Development (AURA 2.0)

- Biometric sensors (heart rate monitoring)
- Bluetooth parent companion app
- Lightweight lithium battery system
- AI-based predictive crisis detection
- Waterproof 3D printed casing

---

## Project Goals

- Reduce cognitive load during crisis  
- Enable instant non-verbal communication  
- Support emotional co-regulation  
- Preserve child dignity in public environments  
- Provide localized (Albanian) assistive technology  

---

## Disclaimer

AURA is currently a functional prototype and not a certified medical device. Further validation and testing with specialists is required for clinical implementation.

---

## Authors

Parid Todri  
Kaltri Kuka  
Elio Dikolli  
Dea Vasili  

New York High School  
ZVAP Tiranë  

---

## License

Educational and research prototype – not for commercial medical deployment without further validation.