# System Architecture

## Overview

AURA follows a modular embedded architecture:

Input → Processing → Dual Output

## Input Layer
- 8 Mechanical Buttons (GPIO)
- Optional future biometric sensors

## Processing Layer
- Raspberry Pi 4
- Python runtime
- Hybrid RAM Cache
- State Manager

## Output Layer
1. Audio Output (Headphones)
2. Visual Output (LCD Display)

## Hybrid RAM Cache
- Preloads audio assets into RAM
- Dynamically loads visual assets
- Prevents Linux OOM crashes

## Error Protection
- GPIO cleanup handlers
- Process auto-kill routines
- Auto-reset after inactivity