#Python Banking Program
from colorama import Fore,Style,init
init(autoreset=True)
class Color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW + Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL
class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = None

    def set_pin(self):
        while True:
         pin_input = input("Set your 4-digit PIN:")
         if pin_input.isdigit() and len(pin_input) == 4:
            self.pin = pin_input
            print(Color.GREEN + "PIN set sucessfully!"+Color.RESET)
            break
         else:
            print(Color.RED + "INVALID PIN! Please enter exactly 4-digits." + Color.RESET)

    def verify_pin(self):
       for attempt in range(3):
          entered_pin = input("Enter your 4-digit PIN: ")
          if entered_pin == self.pin:
             print(Color.GREEN + "PIN verified sucssesfully !" + Color.RESET)
          return True
       else:
          print(Color.YELLOW + f"Incorrect PIN.Attempts left: {2- attempt}" + Color.RESET)
          print(Color.RED + f"Too many failed attempts.Access blocked !" + Color.RESET)
       return False
    def deposit(self):
       amount = input("Enter deposit amount : Rs")
       if amount.isdigit() and int(amount) > 0:
          amount = float(amount)
          self.balance += amount
          print(Color.GREEN + f"Rs{amount} deposited successfully! New balance: Rs{self.balance}" + Color.RESET)
       else:
          print(Color.RED + "Invaild amount!" + Color.RESET)

    def withdraw(self):
       amount = input("Enter withdrawal amount : Rs")
       if amount.isdigit() :
        amount = float(amount)
        if amount <= 0:
           print(Color.RED + "Invaild amount!" + Color.RESET)
        elif amount > self.balance:
           print(Color.RED + "Invaild amount!" + Color.RESET)
        else:
           self.balance -= amount
           print(Color.GREEN + f"withdraw amount = Rs{amount} . New balance is : Rs{self.balance}" + Color.RESET)
       else:
          print(Color.RED + "Invaild input!" + Color.RESET)

    def check_balance(self):
       print(Color.CYAN + f"Your current balance is : Rs{self.balance}" + Color.RESET)
    print("")
