import copy
import itertools


class BaseStore():
    def _init_(self,data_provider,last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self,item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_item_instances = self.get_all()
        result = None
        for item_instance in all_item_instances:
            if item_instance.id == id:
                yield item_instance
                result = item_instance
        return  result

    def update(self,item_instance):
        all_item_instances = self.get_all()
        result = item_instance

        for index,current_item_instance in enumerate(all_item_instances):
            if current_item_instance.id == item_instance.id :
                all_item_instances[index] = item_instance
                break
        return result

    def delete(self,id):
        item_instance = self.get_by_id(id)
        if item_instance is not None :
            self._data_provider.remove(item_instance)

    def entity_exists(self,item_instance):
        result = True
        if self.get_by_id(item_instance.id):
            result = False
        return result

class MemberStore(BaseStore):
    members = []
    last_id = 1

    def _init_(self):
        super()._init_(MemberStore.members , MemberStore.last_id)

    def get_by_name(self, member_name):
        all_members = self.get_all()

        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = copy.deecopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id is post.member_id:
                member.posts.append(post)

    def get_top_two(self, all_posts):
        member_with_posts = list(self.get_members_with_posts(all_posts))
        member_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield member_with_posts[0]
        yield member_with_posts[1]
'''def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        if self.get_by_id(id) is not None:
            MemberStore.members.remove(member)
            print("delete with succes")
        else:
            print("member doesn't exist")

    def update(self, member):
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                print("Update succsesfull")
                break
        return result'''



class PostStore(BaseStore):
    posts = []
    last_id = 1

    def _init_(self):
        super()._init_(PostStore, PostStore.last_id)

    def get_posts_by_date(self, datetime):
        all_posts = self.get_all()
        result = []
        for post in all_posts:
            if post.date == datetime :
                result.append(post)
                break
        return result



