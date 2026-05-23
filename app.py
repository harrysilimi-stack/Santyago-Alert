from modules.banner import banner
from modules.alerts import send_alert
from modules.system import clear

while True:
    clear()
    banner()

    print("[1] Send Alert")
    print("[2] Exit")

    choice = input("\n[?> ")

    if choice == "1":
        msg = input("Message: ")
        send_alert(msg)
        input("\nDone...")

    elif choice == "2":
        break
