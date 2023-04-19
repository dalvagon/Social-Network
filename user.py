class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()

    def add_friend(self, user):
        self.friends.add(user)

    def get_friends(self):
        return self.friends

    def has_friend(self, user):
        return user in self.friends
