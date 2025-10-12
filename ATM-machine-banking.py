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
def main():
    atm = ATM()
    print(Color.CYAN + "Welcome to the ATM Banking System!" + Color.RESET)
    atm.set_pin()
    if not atm.verify_pin():
       return
    while True:
       print("\nSelect an option:")
       print("1. Deposit")
       print("2. Withdraw")
       print("3. Check Balance")
       print("4. Exit")
       choice = input("Enter your choice (1-4): ")
       if choice == '1':
          atm.deposit()
       elif choice == '2':
          atm.withdraw()
       elif choice == '3':
          atm.check_balance()
       elif choice == '4':
          print(Color.CYAN + "Thank you for using the ATM Banking System. Goodbye!" + Color.RESET)
          break
       else:
          print(Color.RED + "Invalid choice! Please select a valid option." + Color.RESET)
if __name__ == "__main__":
    main() 
