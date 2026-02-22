# Software Architecture

## 1. System Overview

AURA runs in headless Linux to reduce background load.

Boot sequence:
1. System boot
2. Python auto-launch
3. RAM preload
4. Enter Ready State

---

## 2. Core Modules

gpio_handler.py
- Reads button states
- Debounce logic
- Event dispatch

audio_engine.py
- Dual-channel audio
- Volume limiter
- Fade-in / fade-out

ui_manager.py
- LCD rendering
- Emotional state display

cache_manager.py
- Hybrid RAM Cache logic
- Preload strategy
- Dynamic release

state_manager.py
- Controls system state transitions
- Handles timers
- Prevents overlapping triggers

cleanup_manager.py
- GPIO release
- Process kill safeguards
- Safe exit handling

---

## 3. Memory Management

Strategy:
- Preload critical assets
- Avoid loading large visuals at runtime
- Explicit object dereferencing
- Garbage collection monitoring

---

## 4. Latency Optimization

- Minimal blocking operations
- Preloaded audio buffers
- Efficient event loop