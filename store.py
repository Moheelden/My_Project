class MemberStore :

    members = []

    def add(self,member):

        self.members.append(member)
        return(self.members)

    def get_all(self):

        return(self.members)

class PostStore :

    posts = []

    def add(self,post):

       self.posts.append(post)
       return(self.posts)

    def get_all(self):

        return (self.posts)




