favourate_shows = ['The 100','Game of Thrones',
					'Breaking Bad']

thing_running = None

def play(movie_or_show):
	global thing_running
	print('|||||||||| NETFLIX ||||||||||||')
	print(movie_or_show)
	thing_running = movie_or_show

def pause():
	print('Paused',thing_running)