from collections import deque


class SocialNetwork:
    """A social network is a collection of users and their friendships."""

    def __init__(self, frienships):
        """
        Build a social network from a list of friendships.
        Parameters:
            friendships: list
                A list of tuples containing the names of two users that are friends.
        """
        self.frienships = frienships
        self.users = set()
        self.buildNetwork()

    def buildNetwork(self):
        """Build the network from the list of friendships"""
        for user1, user2 in self.frienships:
            if user1 == user2:
                raise ValueError("User cannot be friend with himself")

            self.users.add(user1)
            self.users.add(user2)
            user1.add_friend(user2)
            user2.add_friend(user1)

    def user(self, name):
        """Return the user with the given name if it exists, otherwise return None"""
        for user in self.users:
            if user.name == name:
                return user
        return None

    def shortest_path(self, userA, userB):
        """
        Find the shortest path between two users in the network using breadth-first search.
        Parameters:
            userA: User
                The first user's name.
            userB: User
                The second user's name.
        Returns:
            tuple
                A tuple containing a list of the users in the shortest path and the length of the path.
                If there is no path, the list should be None and the length should be -1.
        """
        start = self.user(userA)
        end = self.user(userB)

        if start == end:
            return [start], 0

        if start is None or end is None:
            raise ValueError("User not found")

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        prev = {start: None}  # previous node in the path

        while queue:
            user, depth = queue.popleft()
            if user == end:  # found the end, build the path
                path = []
                while user is not None:
                    path.append(user)
                    user = prev[user]

                return path[::-1], depth
            for friend in sorted(
                user.get_friends(), key=lambda x: x.name
            ):  # sort friends by name
                if friend not in visited:
                    queue.append((friend, depth + 1))
                    visited.add(friend)
                    prev[friend] = user

        return None, -1
