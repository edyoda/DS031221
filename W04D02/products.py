products_details = [
{
	'Name': 'Mac Book Pro 16 inches',
	'Price': 200000,
	'Id': 'A101',
	'Color': 'Space-Grey',
	'Seller': 'Rohan'
},
{
	'Name': 'Rotating Chair',
	'Price': 7000,
	'Id': 'C234',
	'Color': 'Black',
	'Seller': 'Abdul Qadir'
}
]

def show_products():
	for product in products_details:
		print('---------------------')
		print(product['Name'])
		print('Buy at ',product['Price'])
		print('Change Color',product['Color'])
		print('Sold by ',product['Seller'])
		print('Id = ',product['Id'])

def add_new_product():
	name = input("Product Name")
	price = float(input("Price in Float"))
	id_of_product = input("Id")
	color = input("Color")
	seller = input("Seller")
	products_details.append({
		'Name':name,
		"Price":price,
		"Id": id_of_product,
		"Color": color,
		"Seller": seller
		})








