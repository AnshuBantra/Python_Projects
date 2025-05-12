import os, sys, functools
from typing import Callable

options_ = {1:'Add Expense', 2:'List Expense', 3:'Delete Expense', 4:'Finance Report', 0:'Exit'}

def retry_on_exception(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'Error: {e}')
                if func.__name__ == 'get_option':
                    choice = input(f'\t\t0 - Exit\n\t\t1 - Main Menu\n\t\tAny other key to retry: ')
                else:
                    choice = input(f'\t\t0 - Exit\n\t\tAny other key to retry: ')
                if  choice == '0':
                    print('Exiting System ... ...')
                    sys.exit()
                elif choice == '1':
                    if func.__name__ == 'get_option':
                        return -1
                    else:
                        break
    return wrapper        

def enter_to_continue() -> None:
    input('\n\nPress Enter ↵ to continue ... ...')

def itr_join(itr: tuple[int]) -> str:
    itr = [*map(str, itr)]
    return f"({'/'.join(itr)})"

@retry_on_exception
def get_option(options: list[int], idx:str = 'Index') -> int:
    optns = itr_join(options)
    val_ = int(input(f'Enter {idx} Option {optns}: '))
    if  val_ not in options:
        raise ValueError(f'Invalid Value: Choose a valid option {optns}')
    else:
        return int(val_)

@retry_on_exception
def get_amount(category_: str) -> float:
    amount = float(input(f'Enter {category_}: '))
    if  amount < 0:
        raise ValueError('Negative Value')
    else:
        return amount

@retry_on_exception
def get_type(types_: list[str]) -> str:
    types = itr_join(types_)
    type_ = input(f'Enter Type {types}: ').capitalize()
    if type_ not in types_:
        raise ValueError(f'Incorrect Type: Choose a valid option {types}')
    else:
        return type_

def put_report(income: float, expense: float) -> None:
    width = len(f'Total Expense = {income}{expense}            ')
    print(f'{"Finance Report:".center(width)}\n{'-'*width}')
    print(f'{" Total Income = ".ljust(18)}$ {income:16,.2f}')
    print(f'{" Total Expense = ".ljust(18)}$ {expense:16,.2f}')
    print(f'{'-'*width}\n{" Total Balance = ".ljust(18)}$ {income - expense:16,.2f}\n{'-'*width}')
    enter_to_continue()

def clear_screen() -> None:
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def put_menu(options_: dict) -> int:
    for k, v in options_.items():
        print(f'{k}:\t{v}')

    return get_option([*options_.keys()], 'menu')


def main():
    pass

if __name__ == '__main__':
    main()