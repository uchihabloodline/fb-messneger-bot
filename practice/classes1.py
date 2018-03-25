class Student:
	count_student = 0
	def __init__(self,name,id_num,roll):
		self.name = name
		self.id = id_num		#id will be referenced and not id_num if calling fo its value.
		self.roll = roll

		Student.count_student += 1

	def all(self):
		return 'name={} with{} id and {} Roll'.format(self.name,self.id,self.roll)

st1 = Student('ferris',22,33)
st2 = Student('tailor',33,56)


st1.count_student = 4
print(st1.name)
print(st1.all())
print(st1.count_student)
print(Student.count_student)
#print(st1.__dict__)