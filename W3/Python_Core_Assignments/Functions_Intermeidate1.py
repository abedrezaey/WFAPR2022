# Update Values in Dictionaries and Lists


x = [ [5,2,3], [10,8,9] ]
x [1] [0] = 15
print(x)





students = [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students [0] ['last_name'] = 'Bryant'
print(students)






sports_directory = {
      'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
      'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'] [0] = 'Andres'
print(sports_directory)






z = [ {'x': 10, 'y': 20} ]

z [0] ['y'] = 30

print(z)




# Iterate Through a List of Dictionaries

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


for iterateDictionary in students:
      for key in  iterateDictionary: 
            print(key, ":", iterateDictionary [key])


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# 04 - Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
for info in dojo:
      print( info, dojo [info])


# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon