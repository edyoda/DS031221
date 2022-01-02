seller = None
Buyer = None
Price = None
count = 0
def create():
	global count
	file_name = str(count)+"invoice"
	fp = open('invoices/'+file_name,'w')
	fp.write('Seller = ' + seller+'\n')
	fp.write('Buyer = '+ Buyer+'\n')
	fp.write('Price = '+ str(Price)+'\n')
	fp.close()
	count+=1