import zomato.order

foods = ['Biryani','Pizza','White Pasta']

def choose_food():
	for food in foods:
		print(food)
	food = input('Which food you want to order?')
	zomato.order.make_order(food)