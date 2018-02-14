from models import Member

class MemberStore :

    members = []

    def add(self,member):

        i = 0
        lenght = 5

        while i <= lenght:
            self.members.append(member)
            i += 1
        return(self.members)

    def get_all(self):

        for e in self.members:
            print(self.members)

'''class TopicStore :
    members = []

    def add(self,membre):
        member = Member(name,age)
        i = 0
        lenght = 1

        z = (str(member))
        while i <= lenght:
            self.members.append(z)
            i += 1
        print(self.members)

    def get_all(self):

        for e in self.members:
            print(self.members)'''




