from bank_account import BankAccount

# SavingsAccount inherits from BankAccount
class SavingsAccount(BankAccount):
	# initializes the object with the starting balance and annual interest rate
	def __init__(self, starting_balance, annual_interest_rate):
		super().__init__(starting_balance, annual_interest_rate)
		
		
		
		

	# check_status() checks the account status by comparing the current balance of the account to 25
	def check_status(self):
		if self._current_balance_this_month < 25:
			self._account_status = "Inactive"
		else:
			self._account_status = "Active"

	# deposit() takes an amount as parameter, calls the method of the parent class to deposit the amount
	# and finally calls the check_status() to update the status
	def deposit(self, amount):
		super().deposit(amount)
		self.check_status()

	# withdraw() takes an amount as parameter, checks if account is inactive and act accordingly
	def withdraw(self, amount):
		if self._account_status == "Inactive":
			print("\nAccount is inactive. No withdrawals are allowed until the balance is above $25.")
			return
		# If account is active, checks if the amount to be withdrawn is greater than the current balance
		if self._current_balance_this_month - amount < 0:
			print("\nInsufficient funds to make the withdrawal.")
		else:
			super().withdraw(amount)
			if self._num_withdrawals_this_month > 4:
				extra_withdrawal_fee = 1
				self._current_balance_this_month -= extra_withdrawal_fee

		self.check_status()

	# calculates monthly interest based on the annual rate and current balance and adds it to the current balance.
	def calc_interest(self):
		monthly_interest_rate = self._annual_interest_rate / 12
		monthly_interest = self._current_balance_this_month * monthly_interest_rate
		self._current_balance_this_month += monthly_interest

	# close_month() checks number of withdrawals made and applies charges if conditions require, and then closes month
	def close_month(self):
		if self._num_withdrawals_this_month > 4:
			self._service_charge_this_month += (self._num_withdrawals_this_month - 4)
		super().close_month()

	#  display_report() prints a summary of the account information
	def display_report(self):
		print("\n**********************************  **********")
		print(f"Savings Account Report:")
		print(f"Starting Balance This Month:        ${self._starting_balance_this_month:.2f}")
		print(f"Total Deposits This Month:          ${self._total_deposits_this_month:.2f}")
		print(f"Number of Deposits This Month:      {self._num_deposits_this_month}")
		print(f"Total Withdrawals This Month:       ${self._total_withdrawals_this_month:.2f}")
		print(f"Number of Withdrawals This Month:   {self._num_withdrawals_this_month}")
		if self._num_withdrawals_this_month > 4:
			print(f"  - Extra withdrawal fee:       ${(self._num_withdrawals_this_month - 4):.2f}")
		print(f"Service Charges This Month:         ${self._service_charge_this_month:.2f}")
		print(f"Current Balance:                    ${self._current_balance_this_month:.2f}")
		print(f"Account Status:                     {self._account_status}")
		print("**********************************  **********")
