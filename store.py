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
        for member in all_members:
            if member is  id:
                return member
        return None

    def entity_exists(self, member):
        all_members = self.get_all()
        if member in all_members:
            return True
        return False

    def delete(self,member):

        if member in MemberStore.members :
            MemberStore.members.remove(member)
            print ("delete with succes")
        #print ("member not exist")

class PostStore:
    posts = []
    lasst_id = 1

    def add(self, post):
        post_id = PostStore.lasst_id
        self.posts.append(post)
        PostStore.lasst_id += 1

    def get_all(self):

        return (self.posts)

    def get_by_id(self, id):
        all_posts = self.get_all()

        for post in all_posts:

            if post is id:
                return True
        return False

    def get_by_id(self, id):
        all_posts = self.get_all()
        for post in all_posts:
            if post is id:
                return post
        return None

    def entity_exists(self, post):
        all_posts = self.get_all()
        if post in all_posts:
            return True
        return False

    def delete(self, post):

        if post in PostStore.posts:
            PostStore.posts.remove(post)
            print("delete post with succes")

