from bank_account import BankAccount

# CheckingAccount inherits from BankAccount
class CheckingAccount(BankAccount):
	# The constructor calls the superclass constructor
	def __init__(self, starting_balance, annual_interest_rate):
		super().__init__(starting_balance, annual_interest_rate)

	# check_status() updates the account status based on the current balance
	def check_status(self):
		if self._current_balance_this_month < 25:
			self._account_status = "Inactive"
		else:
			self._account_status = "Active"

	# withdraw() method applies withdrawal fee, checks for sufficient funds, and updates account status
	# Overrides the one from BankAccount
	def withdraw(self, amount):
		withdrawal_fee = 0.10
		if self._current_balance_this_month - amount - withdrawal_fee < 0:
			print("\nInsufficient funds to make the withdrawal.")
			service_charge = 15
			if self._current_balance_this_month - service_charge < 0:
				print("Account will become negative after applying the service charge.")
			self._current_balance_this_month -= service_charge
			self._service_charge_this_month += service_charge
		else:
			super().withdraw(amount)
			self._current_balance_this_month -= withdrawal_fee

		if self._current_balance_this_month < 0:
			self._account_status = "Inactive"
			print("Account is now inactive due to a negative balance.")

	# Overridden deposit() method calls the superclass method and updates account status
	def deposit(self, amount):
		super().deposit(amount)
		self.check_status()

	# calc_interest() calculates the monthly interest
	def calc_interest(self):
		monthly_interest_rate = self._annual_interest_rate / 12
		monthly_interest = self._current_balance_this_month * monthly_interest_rate
		self._current_balance_this_month += monthly_interest

	# close_month() applies monthly fee, withdrawal fees, and resets values
	def close_month(self):
		monthly_fee = 5
		withdrawal_fee = 0.10 * self._num_withdrawals_this_month
		self._service_charge_this_month += monthly_fee + withdrawal_fee
		self._current_balance_this_month -= self._service_charge_this_month
		super().close_month()

	# display_report() method displays the account report
	def display_report(self):
		print("\n**********************************  **********")
		print(f"Checking Account Report:")
		print(f"Starting Balance This Month:        ${self._starting_balance_this_month:.2f}")
		print(f"Total Deposits This Month:          ${self._total_deposits_this_month:.2f}")
		print(f"Number of Deposits This Month:      {self._num_deposits_this_month}")
		print(f"Total Withdrawals This Month:       ${self._total_withdrawals_this_month:.2f}")
		print(f"Number of Withdrawals This Month:   {self._num_withdrawals_this_month}")
		print(f"Service Charges This Month:         ${self._service_charge_this_month:.2f}")
		#print(f"  - Monthly fee: $5.00")
		if self._num_withdrawals_this_month:
			print(f"  - Withdrawal fee:             ${0.10 * self._num_withdrawals_this_month:.2f}")
		print(f"Current Balance:                    ${self._current_balance_this_month:.2f}")
		print(f"Account Status:                     {self._account_status}")
		print("**********************************  **********")