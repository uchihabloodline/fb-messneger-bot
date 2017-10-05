
globvar = 0

a_string = "first string"
def set_get_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1
    print(globvar)

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_get_globvar_to_one()
print_globvar()       # Prints 1

print(a_string)

print(len(a_string))
print(a_string[6:12])
print(a_string[6:12] + " "+ "!!")

weekdays = ['Monday', 'Tuesday', 'wednesday','thursday','friday','saturday', 'its dd dd over']

print(weekdays[6])
print(weekdays[6] + ' ' 'and' + ' ' + weekdays[4])

mydict = {'name':'shivam', 'yr':3, 'branch':'CSE'}

print(mydict)
print(mydict['name'])
mydict['shinobi_class'] = 's rank'
print(mydict['shinobi_class'])