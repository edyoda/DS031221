from payment_gateway import upi
from payment_gateway  import card
from payment_gateway  import pay_on_delivery

list_of_payment_methods = ['upi','card','pay_on_delivery']

def initialise_system():
	upi.total_amount = 0
	card.total_amount = 0
	pay_on_delivery.total_amount = 0

def pay(amount, option):
	if option == 'upi':
		upi.pay(amount)

	elif option == 'card':
		card.pay(amount)

	else:
		pay_on_delivery.pay(amount)
	print('Payment Successfull for amount',amount)


def choose_payment_method():
	show_payment_methods()
	option = input('Choose the payment method')
	return option

def show_payment_methods():
	for payment_method in list_of_payment_methods:
		print(payment_method)



