# Eduardo Pinto - Assignment 2 - Concordia

import os
import time
from savings_account import SavingsAccount
from checking_account import CheckingAccount



# displays options for selecting an account type
def display_bank_menu():
	print("\nBank Menu:")
	print("A - Savings")
	print("B - Checking")
	print("Q - Exit")


# display options for interacting with each account type
def display_savings_menu():
	print("\nSavings Menu:")
	print("A - Deposit")
	print("B - Withdrawal")
	print("C - Report")
	print("Q - Return to Bank Menu")


def display_checking_menu():
	print("\nChecking Menu:")
	print("A - Deposit")
	print("B - Withdrawal")
	print("C - Report")
	print("Q - Return to Bank Menu")


# clear_screen function clears the screen using the appropriate command for the operating system
# I have noticed that it doesn't work properly with PyCharm but runs well in Windows cmd and Linux terminal
def clear_screen():
	if os.name == 'nt':  # For Windows
		os.system('cls')
	else:  # For Unix-based systems (Linux and macOS)
		os.system('clear')


# two accounts created (savings and checking)
# main function also includes error handling to catch invalid user inputs and prompts the user to try again
def main():
	savings_account = SavingsAccount(25, 0.02)
	checking_account = CheckingAccount(5, 0.01)

	# prompts and interactions (with pauses for better visualization)
	while True:
		clear_screen()
		display_bank_menu()
		account_choice = input("\nSelect an account type: ").lower()

		if account_choice == "a":  # Savings Account
			while True:
				clear_screen()
				display_savings_menu()
				savings_choice = input("\nSelect an option: ").lower()
				if savings_choice == "a":
					try:
						amount = float(input("Enter the deposit amount: "))
						savings_account.deposit(amount)
						savings_account.display_report()
						input("Press ENTER to continue ")
					except ValueError:
						print("Invalid input. Please enter a valid number.")
						time.sleep(2)
				elif savings_choice == "b":
					try:
						amount = float(input("Enter the withdrawal amount: "))
						savings_account.withdraw(amount)
						savings_account.display_report()
						input("Press ENTER to continue ")
					except ValueError:
						print("Invalid input. Please enter a valid number.")
						time.sleep(2)
				elif savings_choice == "c":
					savings_account.display_report()
					savings_account.reset_month()
					savings_account.close_month()
					input("Press ENTER to continue ")
				elif savings_choice == "q":
					break
				else:
					print("Invalid choice. Please try again.")
					time.sleep(2)
		elif account_choice == "b":  # Checking Account
			while True:
				clear_screen()
				display_checking_menu()
				checking_choice = input("\nSelect an option: ").lower()
				if checking_choice == "a":
					try:
						amount = float(input("Enter the deposit amount: "))
						checking_account.deposit(amount)
						checking_account.display_report()
						input("Press ENTER to continue ")
					except ValueError:
						print("Invalid input. Please enter a valid number.")
						time.sleep(2)
				elif checking_choice == "b":
					try:
						amount = float(input("Enter the withdrawal amount: "))
						checking_account.withdraw(amount)
						checking_account.display_report()
						input("Press ENTER to continue ")
					except ValueError:
						print("Invalid input. Please enter a valid number.")
						time.sleep(2)
				elif checking_choice == "c":
					checking_account.display_report()
					checking_account.reset_month()
					checking_account.close_month()
					input("Press ENTER to continue ")
				elif checking_choice == "q":
					break
				else:
					print("Invalid choice. Please try again.")
					time.sleep(2)
		elif account_choice == "q":
			print("Exiting...")
			time.sleep(3)  # 3 second time before program exits
			break
		else:
			print("Invalid choice. Please try again.")
			time.sleep(2)


# checks if the current file is being executed as the main program
if __name__ == "__main__":
	main()
