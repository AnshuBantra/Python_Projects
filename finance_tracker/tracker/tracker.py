import json
import os
from datetime import datetime
import utils.json_handler as jh
import utils.user_interaction as ui


class Expense:
    def __init__(self, amount: float, type: str, category: str):
        self.__amount = amount
        self.__type = type
        self.__category = category
        self.__date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.__amount,
            "type": self.__type,
            "category": self.__category,
            "date": self.__date
        }
    
    def __str__(self):
        return f'{self.__date=}|{self.__type=}|{self.__category=}|{self.__amount=}'

class ExpenseTracker:
    FILE_PATH = os.path.join('data', 'tracker.json')

    def __init__(self):
        self.expenses = jh.load_data(self.FILE_PATH)

    def add_expense(self, expense: type[Expense]):
        self.expenses.append(expense.to_dict())
        jh.save_data(self.FILE_PATH, self.expenses)
        print("Expense added successfully!")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print(f"{'Idx'.rjust(3)} | {'Date & Time'.ljust(20)} | {'Type'.ljust(8)} | {'Category'.ljust(12)} | {'  Amount ($)'}")
        print(f"{'-'*3} | {'-'*20} | {'-'*8} | {'-'*12} | {'-'*13}")
        for idx, exp in enumerate(self.expenses, 1):
            print(f"{str(idx).rjust(3)} | {exp['date'].ljust(20)} | {exp['type'].ljust(8)} | {exp['category'].ljust(12)} | ${exp['amount']:>12,.2f}")
        ui.enter_to_continue()

    def delete_expense(self):
        idx = ui.get_option([idx for idx, exp in enumerate(self.expenses, 1)])
        if idx != -1:
            del self.expenses[idx-1]
            jh.save_data(self.FILE_PATH, self.expenses)
            print("Expense deleted.")

    def finance_report(self):
        income, expense = 0, 0
        for k, v in enumerate(self.expenses):
            if v['type'] == 'Income':
                income += v['amount']
            else:
                expense += v['amount']
        ui.put_report(income, expense)

    def main():
        pass

    if __name__ == '__main__':
        main()