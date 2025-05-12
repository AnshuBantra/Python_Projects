import sys
import tracker.tracker as trk #import Expense, ExpenseTracker
import utils.user_interaction as ui

def main():
    options_ = {1:'Add Expense', 2:'List Expense', 3:'Delete Expense', 4:'Finance Report', 0:'Exit'}
    types_ = ['Income', 'Expense']
    categories_ = ['Freelance', 'Job', 'Business']
    tracker = trk.ExpenseTracker()

    ui.clear_screen()
    while True:
        selection = ui.put_menu(options_)
        match selection:
            case 0:
                    print('Exiting System ... ...')
                    sys.exit()
            case 1:
                print('Adding Transaction:')
                amount_ = ui.get_amount('Transaction amount')
                type_ = ui.get_type(types_)
                category_ = ui.get_type(categories_)
                if amount_ and type_ and category_:
                    tracker.add_expense(trk.Expense(amount_, type_, category_))
            case 2:
                tracker.list_expenses()
            case 3:
                tracker.delete_expense()
            case 4:
                tracker.finance_report()

if __name__ == "__main__":
    main()