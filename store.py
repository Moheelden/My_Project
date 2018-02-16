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
            if member.id ==  id:
                return member
        return None

    def entity_exists(self, member):

         if self.get_by_id(member.id)is member :
            return True
         return False

    def delete(self,member):

        if self.entity_exists(member) == True:
            MemberStore.members.remove(member)
            print ("delete with succes")
        else :
            print ("member doesn't exist")

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
        for post in all_posts:
            if post.id == id:
                return post
        return None

    def entity_exists(self, post):
        if self.get_by_id(post.id) is post :
            return True
        return False

    def delete(self, post):

        if self.entity_exists(post) == True :
            PostStore.posts.remove(post)
            print("delete post with succes")
        else :
            print (" post dosn't exist")

