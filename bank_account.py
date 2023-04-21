from abc import ABC, abstractmethod

# BankAccount is an abstract class that other account types will inherit from
class BankAccount(ABC):
	# The constructor initializes the account's starting balance, current balance,
	# deposits, withdrawals, annual interest rate, service charge, and account status
	def __init__(self, starting_balance, annual_interest_rate):
		self._starting_balance_this_month = starting_balance
		self._current_balance_this_month = starting_balance
		self._total_deposits_this_month = 0
		self._num_deposits_this_month = 0
		self._total_withdrawals_this_month = 0
		self._num_withdrawals_this_month = 0
		self._annual_interest_rate = annual_interest_rate
		self._service_charge_this_month = 0
		self._account_status = "active"  # "active" or "inactive"

	# deposit() method updates the current balance, total deposits, and the number of deposits
	def deposit(self, amount):
		self._current_balance_this_month += amount
		self._total_deposits_this_month += amount
		self._num_deposits_this_month += 1

	# withdraw() method updates the current balance, total withdrawals, and the number of withdrawals
	def withdraw(self, amount):
		self._current_balance_this_month -= amount
		self._total_withdrawals_this_month += amount
		self._num_withdrawals_this_month += 1

	# reset_month() method resets the values for the start of a new month
	def reset_month(self):
		self._starting_balance_this_month = self._current_balance_this_month
		self._total_deposits_this_month = 0
		self._num_deposits_this_month = 0
		self._total_withdrawals_this_month = 0
		self._num_withdrawals_this_month = 0
		self._service_charge_this_month = 0

	# calc_interest() and close_month() methods are an abstract method that are implemented in the subclasses
	@abstractmethod
	def calc_interest(self):
		pass

	@abstractmethod
	def close_month(self):
		pass
	
	
	
	
	
	
	
	
	
