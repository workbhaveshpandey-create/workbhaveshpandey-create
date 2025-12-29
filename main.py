import sys
import time
import random

class BhaveshPandey:
    def __init__(self):
        self.user = "KreoDev"
        self.role = ["Full Stack Developer", "IoT Engineer", "Musician"]
        self.stack = {
            "Web": ["React", "TypeScript", "Node.js", "Firebase"],
            "Hardware": ["Arduino", "Raspberry Pi", "Circuit Design"],
            "AI": ["Python", "Data Science", "Face Recognition"]
        }
        self.music_experience = {
            "Piano": "7 Years",
            "Vocals": "Classical Degree Holder",
            "Percussion": "Drums & Beatboxing"
        }

    def typing_effect(self, text, speed=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def boot_system(self):
        print("\033[96m") # Cyan Color
        ascii_art = """
        ██╗  ██╗██████╗ ███████╗ ██████╗ 
        ██║ ██╔╝██╔══██╗██╔════╝██╔═══██╗
        █████╔╝ ██████╔╝█████╗  ██║   ██║
        ██╔═██╗ ██╔══██╗██╔══╝  ██║   ██║
        ██║  ██╗██║  ██║███████╗╚██████╔╝
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ 
        """
        print(ascii_art)
        print("\033[0m")
        
        self.typing_effect(f"[SYSTEM] Initializing Profile for {self.user}...", 0.05)
        time.sleep(0.5)
        self.typing_effect("[LOAD] Loading Hardware Drivers (Arduino/Pi)... SUCCESS")
        self.typing_effect("[LOAD] Loading Web Modules (React/Node)... SUCCESS")
        self.typing_effect("[LOAD] Tuning Instruments... SUCCESS")
        print("-" * 40)

    def show_stats(self):
        print("\n\033[92m>> ACCESSING ACADEMIC RECORDS \033[0m")
        print(f"Education: B.Tech Data Science & IoT @ Amrapali University")
        print(f"Board Stats: 10th (85.2%) | 12th (75.2% PCM+CS)")
        
        print("\n\033[93m>> HARDWARE PROJECTS \033[0m")
        projects = [
            "IoT E-Waste Segregation (INSPIRE Award 2024)",
            "Real-time Face Rec System",
            "Smart Home Automation"
        ]
        for p in projects:
            print(f"[*] {p}")

    def play_music_profile(self):
        print("\n\033[95m>> LAUNCHING AUDIO ENGINE \033[0m")
        for instrument, time_period in self.music_experience.items():
            print(f"🎵 Playing: {instrument} ({time_period} exp)")
            time.sleep(0.2)
        self.typing_effect("\n[QUOTE] 'Music is the hidden arithmetic of the soul.'")

if __name__ == "__main__":
    me = BhaveshPandey()
    me.boot_system()
    
    while True:
        choice = input("\n[MENU] Select: [1] Stats [2] Music [3] Exit > ")
        if choice == "1":
            me.show_stats()
        elif choice == "2":
            me.play_music_profile()
        elif choice == "3":
            me.typing_effect("Shutting down system. Goodbye, User.")
            break
        else:
            print("Invalid command.")
