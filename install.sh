#!/bin/bash

# ==========================================
# RDX CALL - Auto Installer Script
# Developer: RDX KING (RDX CYBER TEAM)
# ==========================================

# কালার কোড (টার্মিনালে সুন্দর দেখানোর জন্য)
GREEN='\033[1;92m'
CYAN='\033[1;96m'
YELLOW='\033[1;93m'
RED='\033[1;91m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "=============================================="
echo "      ⚡ RDX CALL - AUTO INSTALLER ⚡"
echo "=============================================="
echo -e "${NC}"

# ১. ইন্টারনেট কানেকশন চেক
echo -e "${YELLOW}[*] Checking Internet Connection...${NC}"
if ! ping -c 1 google.com > /dev/null 2>&1; then
    echo -e "${RED}[!] No Internet Connection! Please connect and try again.${NC}"
    exit 1
fi
echo -e "${GREEN}[✓] Internet Connection OK.${NC}"

# ২. পাইথন এবং git ইনস্টল করা
echo -e "${YELLOW}[*] Installing Required Packages (Python, Git)...${NC}"
if command -v pkg > /dev/null 2>&1; then
    # Termux (Android)
    pkg update -y > /dev/null 2>&1
    pkg install python git -y > /dev/null 2>&1
elif command -v apt > /dev/null 2>&1; then
    # Ubuntu / Debian
    sudo apt update -y > /dev/null 2>&1
    sudo apt install python3 python3-pip git -y > /dev/null 2>&1
elif command -v yum > /dev/null 2>&1; then
    # CentOS / Fedora
    sudo yum install python3 python3-pip git -y > /dev/null 2>&1
else
    echo -e "${YELLOW}[!] Package manager not found. Make sure Python & Git are installed.${NC}"
fi
echo -e "${GREEN}[✓] Packages Installed Successfully.${NC}"

# ৩. পাইথন লাইব্রেরি (requests) ইনস্টল করা
echo -e "${YELLOW}[*] Installing Python Dependencies...${NC}"
pip install requests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[✓] Dependencies Installed.${NC}"
else
    echo -e "${RED}[!] Failed to install requests. Trying with pip3...${NC}"
    pip3 install requests > /dev/null 2>&1
fi

# ৪. টুলটি রান করা
echo -e "${YELLOW}[*] Starting RDX CALL Tool...${NC}"
sleep 1
clear

# মেইন পাইথন ফাইলটি রান করা
if [ -f "rdx.py" ]; then
    python rdx.py || python3 rdx.py
else
    echo -e "${RED}[!] Error: rdx.py not found!${NC}"
    echo -e "${YELLOW}[*] Make sure you are in the correct folder.${NC}"
fi
