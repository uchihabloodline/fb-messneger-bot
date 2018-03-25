def daco(msg):
	def in_deco():
		print(msg)
		return in_daco

out = daco('van')

out