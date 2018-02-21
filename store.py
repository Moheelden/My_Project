import itertools


class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
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
        return result

    def get_by_name(self, name):
        all_members = self.get_all()
        result = []
        for member in all_members:
            if member.name == name:
                result.append(member)
                break
        return result

    def get_members_with_posts(self, all_posts):

        all_members = self.get_all()

        for member , post in itertools.product(all_members , all_posts) :
            if member.id is post.member_id:
                all_members.append(post)

        return all_members

    def get_top_two(self, all_posts):
        all_members = self.get_all()
        self.get_members_with_posts(all_posts)

        result = sorted(all_members, key=lambda top: len(top.posts), reverse=True)
        return result[:2]

class PostStore:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = PostStore.last_id
        self.posts.append(post)
        PostStore.last_id += 1

    def get_all(self):

        return (self.posts)

    def get_by_id(self, id):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def entity_exists(self, post):
        result = True
        if self.get_by_id(post.id) is None:
            result = False
        return result

    def delete(self, id):
        post = self.get_by_id(id)

        if self.get_by_id(id) is not None:
            PostStore.posts.remove(post)
            print("delete post with succes")
        else:
            print(" post dosn't exist")

    def update(self, post):
        result = post
        all_posts = self.get_all()

        for index, current_post in enumerate(all_posts):
            if current_post.id == post.id:
                all_posts[index] = post
                print("Update succsesfull")
                break
        return result

    def get_by_name(self, title):
        all_posts = self.get_all()
        result = []
        for post in all_posts:
            if post.name == post:
                result.append(post)
                break
        return result
