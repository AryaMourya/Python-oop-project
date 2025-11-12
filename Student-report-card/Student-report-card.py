#Student Report Card
from colorama import Fore, Style, init
init(autoreset=True)
class Color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW + Style.__dict__BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL
class StudentReportCard:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        
        def calculate_total(self):
            return sum(self.marks.values())
        def claculate_percentage(self):
            total_marks = self.calculate_total()
            return (total_marks / (len(self.marks))*100)
        
        def calculate_grade(self):
            percent =
        self.calculate_percentage()
        if percent >= 90:
            return ''  