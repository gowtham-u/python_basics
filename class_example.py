class Result:
    name = None
    marks = 0
    grade = None

def result(name, marks, grade):
    return name,marks*2,grade


cse = Result()
cse.name = 'gowtham'
cse.marks = 70
cse.grade = 'c'

mech = Result()
mech.name = 'gokul'
mech.marks = 80
mech.grade = 'b'

eee = Result()
eee.name = 'john'
eee.marks = 90
eee.grade = 'a'

cse_score = result(cse.name,cse.marks,cse.grade)
mech_score = result(mech.name,mech.marks,mech.grade)
eee_score = result(eee.name,eee.marks,eee.grade)


print(cse_score)
print(mech_score)
print(eee_score)
print(cse.__dict__)
print(mech.__dict__)
print(eee.__dict__)