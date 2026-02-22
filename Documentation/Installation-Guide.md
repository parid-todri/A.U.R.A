# Installation Guide

## 1. Hardware Setup

- Wire buttons using pull-up config
- Connect LCD via HDMI
- Connect battery
- Connect headphones

---

## 2. Software Setup

Flash Raspberry Pi OS Lite.

Enable SSH (optional).

Install dependencies:

sudo apt update
sudo apt install python3-pip
pip3 install pygame

Clone repository:

git clone https://github.com/yourrepo/aura.git

Navigate:

cd aura/src

Run:

python3 main.py

---

## 3. Auto Start Setup

Add to rc.local or create systemd service for auto-launch.