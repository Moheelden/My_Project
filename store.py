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
            if member.id ==  id:
                result = member
                break
        return result

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id)is  None :
            result = False
        return result

    def delete(self,id):
        member = self.get_by_id(id)
        if self.get_by_id(id) is not None :
            MemberStore.members.remove(member)
            print("delete with succes")
        else:
            print("member doesn't exist")

    def update(self,member):
        result = member
        all_members = self.get_all()

        for member in all_members :
            if self.get_by_id(id) == member.id :
                return result

        print ("Update succsesfull")

    def get_by_name(self, name):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.name == name:
                result = member
                break
        return result

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
        if self.get_by_id(post.id) is  None :
            result = False
        return result

    def delete(self, id):
        post = self.get_by_id(id)

        if self.get_by_id(id) is not None:
            PostStore.posts.remove(post)
            print("delete post with succes")
        else :
            print (" post dosn't exist")

    def update(self, post):

        all_posts = self.get_all()

        for post in all_posts:
            if self.get_by_id(id) == post.id:
                post.title = post.title
                post.topic = post.topic

        print("Update succsesfull")

    def get_by_name(self, title):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.name == post:
                result = post
                break
        return result

