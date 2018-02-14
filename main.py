from models import Member  , Post
from store import MemberStore

name1 = "ahmed"
name2 = "kkkk"

age1 = 35
age2 = 28

member1 = Member(name1 , age1)
member2 = Member(name2 , age2)
print (str(member1.name))
member_store = MemberStore()

print(member_store.add(member2))





