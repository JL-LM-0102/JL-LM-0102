#!/usr/bin/env python3
import os
import time
import sys
import random
from getpass import getpass

# ألوان مهدئة
CYAN = '\033[96m'
DIM_GREEN = '\033[38;5;40m'
DARK_RED = '\033[38;5;88m'
YELLOW = '\033[38;5;226m'
END = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def smooth_transition():
    # تأثير انتقالي سلس
    for _ in range(15):
        print(CYAN + '•' * random.randint(10, 30) + END)
        time.sleep(0.05)
    clear_screen()

def animate_jakel():
    # تصميم أنيق مع توقيتات مدروسة
    jakel_ascii = [
        f"{DARK_RED}   ██╗ █████╗ ██╗  ██╗███████╗██╗     {END}",
        f"{DIM_GREEN}   ██║██╔══██╗██║ ██╔╝██╔════╝██║     {END}",
        f"{DARK_RED}   ██║███████║█████╔╝ █████╗  ██║     {END}",
        f"{DIM_GREEN}██╗██║██╔══██║██╔═██╗ ██╔══╝  ██║   ██╗{END}",
        f"{DARK_RED}╚█████╔╝██║  ██║██║  ██╗███████╗███████╗{END}",
        f"{DIM_GREEN} ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝{END}"
    ]
    
    # ظهور متدرج للسطور
    for line in jakel_ascii:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        time.sleep(0.2)

def subtle_glitch(text, repeats=3):
    # تأثير غليتش خفيف
    for _ in range(repeats):
        glitched = ''.join([c if random.random() > 0.1 else '░' for c in text])
        print(f"{DARK_RED}{glitched}{END}", end='\r')
        time.sleep(0.1)
    print(f"{DIM_GREEN}{text}{END}")

def show_banner():
    clear_screen()
    smooth_transition()
    
    print("\n"*2)
    animate_jakel()
    time.sleep(0.5)
    
    subtle_glitch("ᎻᎥ ᏃᏢ / ᏞᏃ , ᎽᏫᏌ ᏁᎬᎬᎠ ᎿᏫ ᏰᎬ ᏚᎷᎯᎡᎿ ᎿᏫ ᏚᏦᎥᏢ ᎿᏫ ᏁᎬᏔ ᏚᎿᎬᏢ🧠")
    time.sleep(1)
    
    print_typing(f"\n{DIM_GREEN}[{CYAN}✓{DIM_GREEN}] Secure Terminal Activated\n", 0.03)

def print_typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    show_banner()
    
    while True:
        try:
            pwd = getpass(f"{YELLOW}\n[?] Enter Encryption Key: {END}")
            if pwd == "1979":
                print(f"{DIM_GREEN}\n[+] Access Granted!{END}")
                print(f"{DARK_RED}Establishing Secure Connection...{END}")
                
                # شريط تحميل هادئ
                for i in range(1, 21):
                    print(f"{CYAN}▏{'█' * i}{' ' * (20-i)}▕ {5*i}%", end='\r')
                    time.sleep(0.1)
                
                print(f"\n{YELLOW}ᏁᎬᏔ ᏚᎿᎬᏢ ᏌᎡᏞ🔗: {CYAN}https://t.ly/w_3Es{END}\n")
                break
            else:
                print(f"{DARK_RED}\n[!] Authentication Failed{END}")
                print(f"{DIM_GREEN}ᎽᏫᏌᎡ ᏢᏔᎠ ᎥᏚ ᏔᎡᏫᏁᎶ❌🔐.....{END}")
                time.sleep(2)
                show_banner()
        except KeyboardInterrupt:
            print(f"{DARK_RED}\n\n[!] ᎿᎻᎬ ᏚᎬᏚᏚᎥᏫᏁ ᏔᎯᏚ ᎬᏁᎠᎬᎠ ᏰᎽ ᏃᏢ / ᏞᏃ🏴‍☠️{END}")
            sys.exit()

if __name__ == "__main__":
    main()