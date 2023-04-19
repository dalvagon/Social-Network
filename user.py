class User:
    """A user in the social network."""

    def __init__(self, name):
        """
        Build a user with a name and an empty set of friends.
        Parameters:
            name: str
                The user's name.
        """

        self.name = name
        self.friends = set()

    def add_friend(self, user):
        """Add a friend to the user's set of friends."""
        self.friends.add(user)

    def get_friends(self):
        """Return the user's set of friends."""
        return self.friends

    def has_friend(self, user):
        """Return True if the user is friends with the given user, otherwise return False."""
        return user in self.friends
