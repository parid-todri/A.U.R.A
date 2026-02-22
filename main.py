import os
import sys
import time
import pygame
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from gpiozero import Button

# --- CONFIGURATION ---
ASSETS_DIR = "/home/paridtodri/cantaassets"
COOLDOWN_SECONDS = 3.0  
AUTO_RESET_MS = 60000  # 60 seconds in milliseconds

# Emotion Pins 
PIN_MAP = {
    5:  {"id": "01", "name": "happy", "label": "HAPPY"},
    6:  {"id": "02", "name": "sad", "label": "SAD"},
    13: {"id": "03", "name": "anger", "label": "ANGER"},
    19: {"id": "04", "name": "fear", "label": "FEAR"},
    26: {"id": "05", "name": "anxiety", "label": "ANXIETY"},
    12: {"id": "06", "name": "frustration", "label": "FRUSTRATION"},
    16: {"id": "07", "name": "excitement", "label": "EXCITEMENT"},
    20: {"id": "08", "name": "overwhelm", "label": "OVERWHELM"}
}
PIN_CANCEL = 21

# Hardware Control Pins
VOL_UP_PIN = 23
VOL_DOWN_PIN = 24
POWER_PIN = 3

# --- THE AURA ENGINE ---
class AuraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AURA Prototype")
        self.root.configure(bg='black')
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda e: sys.exit()) 

        # 1. SETUP AUDIO SYSTEM & STARTUP VOLUME
        pygame.mixer.init()
        self.bg_channel = pygame.mixer.Channel(0)    
        self.voice_channel = pygame.mixer.Channel(1) 
        
        self.current_volume = 50
        os.system(f"amixer set PCM {self.current_volume}%")

        # 2. SETUP SCREEN CONTAINER
        self.label = Label(root, bg='black')
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # 3. STATE VARIABLES
        self.current_frame = 0
        self.gif_frames = []
        self.is_animating = False
        self.last_trigger_time = 0
        self.memory_cache = {} 
        self.current_emotion_label = "" 
        self.auto_reset_id = None # Tracker for the 60-second timer

        # 4. PRELOAD EVERYTHING
        self.show_text("LOADING ASSETS...\nPLEASE WAIT")
        self.root.update() 
        self.preload_all_assets()

        # 5. INITIALIZE HARDWARE
        self.buttons = []
        self.setup_gpio()

        # 6. READY!
        self.show_text("AURA SYSTEM\nREADY")

    def show_text(self, text):
        self.label.config(text=text, image="", compound=NONE, fg="white", bg="black", font=("Arial", 36, "bold"), pady=0)

    def preload_all_assets(self):
        print("--- PRELOADING ASSETS INTO RAM ---")
        for pin, data in PIN_MAP.items():
            cache = {'frames': [], 'bg': None, 'voice': None}
            
            gif_path = os.path.join(ASSETS_DIR, f"{data['id']}_{data['name']}_icon.gif")
            if os.path.exists(gif_path):
                try:
                    img = Image.open(gif_path)
                    cache['frames'] = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(img)]
                except Exception as e:
                    print(f"Error loading GIF for {data['name']}: {e}")
            
            bg_path = os.path.join(ASSETS_DIR, f"{data['id']}_{data['name']}_bg.wav")
            voice_path = os.path.join(ASSETS_DIR, f"{data['id']}_{data['name']}_voice.wav")
            
            if os.path.exists(bg_path):
                cache['bg'] = pygame.mixer.Sound(bg_path)
            if os.path.exists(voice_path):
                cache['voice'] = pygame.mixer.Sound(voice_path)
                
            self.memory_cache[data['id']] = cache

    def setup_gpio(self):
        print("--- INITIALIZING GPIO ---")
        for pin, data in PIN_MAP.items():
            try:
                btn = Button(pin, pull_up=True, bounce_time=0.1)
                btn.when_pressed = lambda p=pin: self.handle_press(p)
                self.buttons.append(btn)
            except Exception as e:
                print(f"❌ ERROR Emotion GPIO {pin}: {e}")

        try:
            cancel_btn = Button(PIN_CANCEL, pull_up=True, bounce_time=0.1)
            cancel_btn.when_pressed = self.reset_system
            self.buttons.append(cancel_btn)
        except:
            pass

        try:
            vol_up_btn = Button(VOL_UP_PIN, pull_up=True, bounce_time=0.1)
            vol_up_btn.when_pressed = self.volume_up
            self.buttons.append(vol_up_btn)

            vol_down_btn = Button(VOL_DOWN_PIN, pull_up=True, bounce_time=0.1)
            vol_down_btn.when_pressed = self.volume_down
            self.buttons.append(vol_down_btn)

            power_btn = Button(POWER_PIN, pull_up=True, hold_time=3.0)
            power_btn.when_held = self.shutdown_pi
            self.buttons.append(power_btn)
        except Exception as e:
            print(f"❌ ERROR Hardware GPIO: {e}")

    # --- HARDWARE CONTROL METHODS ---
    def volume_up(self):
        self.current_volume = min(100, self.current_volume + 5)
        os.system(f"amixer set PCM {self.current_volume}%") 

    def volume_down(self):
        self.current_volume = max(0, self.current_volume - 5)
        os.system(f"amixer set PCM {self.current_volume}%")

    def shutdown_pi(self):
        print("🛑 SHUTTING DOWN...")
        self.stop_all_media()
        self.show_text("SHUTTING DOWN\nPOWERING OFF...")
        self.root.update()
        time.sleep(2) 
        os.system("sudo shutdown -h now")

    # --- EMOTION LOGIC METHODS ---
    def handle_press(self, pin):
        current_time = time.time()
        if current_time - self.last_trigger_time < COOLDOWN_SECONDS:
            return

        self.last_trigger_time = current_time
        data = PIN_MAP[pin]
        self.trigger_sequence(data)

    def trigger_sequence(self, data):
        self.stop_all_media()
        cache = self.memory_cache[data['id']]
        self.current_emotion_label = data['label']

        # Cancel any existing 60-second reset timer
        if self.auto_reset_id is not None:
            self.root.after_cancel(self.auto_reset_id)

        if cache['bg']:
            self.bg_channel.play(cache['bg'], loops=-1, fade_ms=1000)
        if cache['voice']:
            self.voice_channel.play(cache['voice'])

        if cache['frames']:
            self.gif_frames = cache['frames']
            self.current_frame = 0
            self.is_animating = True
            self.animate_gif()
        else:
            self.show_text(self.current_emotion_label)

        # Start a fresh 60-second timer to reset the screen
        self.auto_reset_id = self.root.after(AUTO_RESET_MS, self.reset_system)

    def animate_gif(self):
        if not self.is_animating:
            return
        frame = self.gif_frames[self.current_frame]
        
        self.label.config(
            image=frame, 
            text=self.current_emotion_label, 
            compound=TOP, 
            fg="white", 
            font=("Arial", 48, "bold"),
            pady=20 
        ) 
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.root.after(50, self.animate_gif)

    def stop_all_media(self):
        self.is_animating = False
        self.bg_channel.stop()
        self.voice_channel.stop()

    def reset_system(self):
        # Stop the timer if the user manually resets
        if self.auto_reset_id is not None:
            self.root.after_cancel(self.auto_reset_id)
            self.auto_reset_id = None
            
        self.stop_all_media()
        self.show_text("AURA SYSTEM\nREADY")

# --- STARTUP ---
if __name__ == "__main__":
    os.environ["DISPLAY"] = ":0"
    root = Tk()
    root.config(cursor="none")
    app = AuraApp(root)
    root.mainloop()