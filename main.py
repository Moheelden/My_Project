from models import Member  , Post
from store import MemberStore , PostStore

name1 = "ahmed"
name2 = "ali"

age1 = 35
age2 = 28

member1 = Member(name1 , age1)
member2 = Member(name2 , age2)
member3 = Member("zzzz",50)
member4 = Member("aaaa",70)
member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)
member_store.add(member4)

print (member_store.get_all())

id1 = member_store.get_by_id(member1)
id2 = member_store.get_by_id(member2)
print("***** get members *****")
print (id1)
print (id2)

found1 = member_store.entity_exists(member1)
found2 = member_store.entity_exists(member3)
found3 = member_store.entity_exists(member4)
print("*******search member*******")
print (found1)
print (found2)

print ("***** delete member *****")
member_store.delete(member4)
print (member_store.get_all())

title1 = "title1"
title2 = "title2"
title3 = "title3"

topic1 = "topic1"
topic2 = "topic2"
topic3 = "topic3"

post1 = Post(title1,topic1)
post2 = Post(title2,topic2)
post3 = Post(title3, topic3)

post_store = PostStore()

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print (post_store.get_all())

print("***** get posts *****")
print(post_store.get_by_id(post1))
print(post_store.get_by_id(post2))

print("*******search posts*******")
print(post_store.entity_exists(post1))
#print(post_store.entity_exists(post2))

print ("***** delete posts *****")
post_store.delete(post2)
print (post_store.get_all())












