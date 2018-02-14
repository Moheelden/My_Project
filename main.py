from models import Member  , Post
from store import MemberStore , PostStore

name1 = "ahmed"
name2 = "kkkk"

age1 = 35
age2 = 28

member1 = Member(name1 , age1)
member2 = Member(name2 , age2)

member_store = MemberStore()

member_store.add(member2)
member_store.add(member2)

print (member_store.get_all())

post1 = Post("title1","topic1")
post2 = Post("title2","topic2")
post3 = Post("title", "topic3")

post_store = PostStore()

post_store.add(post1)
post_store.add(post2)

print (post_store.get_all())









