login_info = {'Mohit':'@#123',
              'Krunal':'3333',
              'Kartik':'call'}

def log_in(username,password):
	pw = login_info.get(username)
	if pw != password:
		print('Wrong username or password')
		return False
	else:
		return True