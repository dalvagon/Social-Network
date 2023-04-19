from collections import deque


class SocialNetwork:
    def __init__(self, frienships):
        self.frienships = frienships
        self.users = set()
        try:
            self.buildNetwork()
        except ValueError as e:
            raise ValueError(e)

    def buildNetwork(self):
        for user1, user2 in self.frienships:
            if user1 == user2:
                raise ValueError("User cannot be friend with himself")

            self.users.add(user1)
            self.users.add(user2)
            user1.add_friend(user2)
            user2.add_friend(user1)

    def user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def shortest_path(self, userA, userB):
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
        prev = {start: None}

        while queue:
            user, depth = queue.popleft()
            if user == end:
                path = []
                while user is not None:
                    path.append(user)
                    user = prev[user]

                return path[::-1], depth
            for friend in sorted(user.get_friends(), key=lambda x: x.name):
                if friend not in visited:
                    queue.append((friend, depth + 1))
                    visited.add(friend)
                    prev[friend] = user

        return None, -1
