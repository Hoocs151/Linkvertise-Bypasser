import requests
from os import system
import os
import pyperclip

def clear_screen():
    system("cls || clear")

def set_title(title):
    system(f"title {title}" if os.name == "nt" else f"PS1='\\[\\e]0;{title}\\a\\]'; clear")

def blue(text):
    return "".join(f"\033[38;2;{30 + i * 3};{144 + i * 3};{255}m{c}" for i, c in enumerate(text))

def yellow(text):
    return "".join(f"\033[38;2;{255 - i * 3};{255 - i * 3};{102 + i * 2}m{c}" for i, c in enumerate(text))

def red(text):
    return "".join(f"\033[38;2;255;{100 + i * 3};{100 + i * 3}m{c}\033[0m" for i, c in enumerate(text))

uwu1 = []

def uwu2(link):
    global uwu1
    if link in uwu1:
        print(yellow("\n[+] This link has already been bypassed! [+]\n"))
        return link
    headers = {
        "origin": "https://thebypasser.com",
        "referer": "https://thebypasser.com/"
    }
    try:
        response = requests.get(f"https://api.toksaver.com/bypass/{link}", headers=headers)
        destination_link = response.json()["link"]
        pyperclip.copy(destination_link)
        uwu1.append(link)
        print(yellow("\n[+] Link copied to clipboard! [+]\n"))
        return destination_link
    except:
        return None

if __name__ == "__main__":
    clear_screen()
    set_title("Linkvertise Bypasser - Successful: 0 - Failed: 0")
    print(blue("╔══════════════════════════════════════════════════════════╗"))
    print(blue("║              Welcome to Linkvertise Bypasser             ║"))
    print(blue("╚══════════════════════════════════════════════════════════╝"))
    successful_links = 0
    failed_links = 0
    while True:
        linkvertise_link = input(blue("\n[>] Please enter a Linkvertise link: "))
        destination_link = uwu2(linkvertise_link)

        if destination_link:
            successful_links += 1
            print(yellow(f"\n[>] Destination link: {destination_link}\n"))
        else:
            failed_links += 1
            print(red("\n[!] An unexpected error occurred\n"))

        set_title(f"Linkvertise Bypasser - Successful: {successful_links} - Failed: {failed_links}")
        choice = input(blue("[>] Press Enter to bypass another link or Q to quit: "))
        if choice.lower() == "q":
            break
