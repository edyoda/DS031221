import auth
import products
from payment_gateway import main

username = input('Username')
password = input('Password')

is_user_valid = auth.log_in(username,password)
main.initialise_system()

if is_user_valid:
	print('***** AMAZON.COM ******')
	reply = int(input('Choose 1 of the following:0) Exit 1) Customer 2) Seller'))
	while reply != 0:
		if reply == 1:
			products.show_products()
			product_id = input('Type Product_Id to Buy')
			for prod_info in products.products_details:
				if prod_info['Id'] == product_id:
					amount = prod_info['Price']
			payment_method = main.choose_payment_method()
			main.pay(amount, payment_method)
		else:
			products.add_new_product()
		reply = int(input('Choose 1 of the following:0) Exit 1) Customer 2) Seller'))
	print('##Thank you for coming to Amazon.com##')