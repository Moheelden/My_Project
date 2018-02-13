from models import Membre ,Post

name1 = "ahmed"
name2 = "ali"

age1 = 35
age2 = 28

membre1 = Membre(name1 , age1)
membre2 = Membre(name2 , age2)

print(str(membre1.name) + 5 * " " + " | " + str(membre1.age))
print(str(membre2.name) + 5 * " " + " | " + str(membre2.age))

post1 = Post("title1" , "topic1")

print( (post1.title) + 5 * " " + " | " + str(post1.topic) )




