#-------------------------------------------------------------------------------
# Name:        Models
# Purpose:
#
# Author:      user
#
# Created:     10/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Member :

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
        return self.age

class Post :

    def __init__(self,title,topic):
        self.title = title
        self.topic = topic

    def __str__(self):
        return self.title
        return self.topic








