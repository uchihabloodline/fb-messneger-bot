class Shivam:
	def __init__(self,first,last,skill,sleep_hr):
		self.first = first
		self.last = last
		self.skill = skill
		self.sleep_hr = sleep_hr

	def details(self):
		return '{} {}' .format(self.first, self.sleep_hr)

a1 = Shivam('shibu','baba','c',10)
a2 = Shivam('baba','ballu','python',10)

print(a1.details())

print(a1.first)
print(a2.skill)