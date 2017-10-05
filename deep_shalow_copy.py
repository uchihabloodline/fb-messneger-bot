import copy
color1 = ['Red', 'Blue']
color2 = ['White','Black']
color3 = [color1 , color2]
# normal copy
color4 = color3
print (id(color3) == id(color4))        # True - color3 is the same object as color4
print (id(color3[0]) == id(color4[0]))  # True - color4[0] is the same object as color3[0]
# shallow copy
color4 = copy.copy(color3)
print (id(color3) == id(color4))        # False - color4 is now a new object
print (id(color3[0]) == id(color4[0]))  # True - The new variable refers to the original variable.
# deep  copy
color4 = copy.deepcopy(color3)
print (id(color3) == id(color4))        # False - color4 is now a new object
print (id(color3[0]) == id(color4[0]))  # False - color4[0] is now a new object
