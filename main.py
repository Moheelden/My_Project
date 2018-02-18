from models import Member  , Post
from store import MemberStore , PostStore

def create_members():
    member1 = Member("Mohammed" , 20)
    member2 = Member("Omar" , 22)
    member3 = Member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)
    return member1 ,member2 ,member3


def store_should_add_models(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def stores_should_be_similar():

    member_store1 = MemberStore()
    member_store2 = MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


members_instances = create_members()
member1, member2, member3 = members_instances

member_store = MemberStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

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

print(post_store.get_by_id(1))
print(post_store.get_by_id(2))

print("*******search posts*******")
print(post_store.entity_exists(post1))
#print(post_store.entity_exists(post2))

print ("***** delete posts *****")
post_store.delete(3)
print (post_store.get_all())












