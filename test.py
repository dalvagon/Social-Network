import unittest

from network import SocialNetwork
from user import User


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        alice = User("Alice")
        bob = User("Bob")
        charlie = User("Charlie")
        dave = User("Dave")
        ed = User("Ed")
        john = User("John")
        kyle = User("Kyle")
        monica = User("Monica")
        quandale = User("Quandale")
        finn = User("Finn")
        glen = User("Glen")

        friendships = [
            (alice, kyle),
            (alice, bob),
            (alice, ed),
            (alice, dave),
            (bob, ed),
            (bob, charlie),
            (bob, dave),
            (charlie, john),
            (dave, ed),
            (dave, kyle),
            (ed, john),
            (monica, finn),
            (monica, quandale),
            (finn, glen),
        ]

        self.network = SocialNetwork(friendships)

    def test_shortest_path(self):
        self.assertEqual(
            self.network.shortest_path("Alice", "Bob"),
            ([self.network.user("Alice"), self.network.user("Bob")], 1),
            "The shortest path between Alice and Bob is Alice -> Bob and has a length of 1",
        )

        self.assertEqual(
            self.network.shortest_path("Kyle", "John"),
            (
                [
                    self.network.user("Kyle"),
                    self.network.user("Alice"),
                    self.network.user("Ed"),
                    self.network.user("John"),
                ],
                3,
            ),
            "The shortest path between Kyle and John is Kyle -> ALice -> Ed -> John and has a length of 3",
        )

        self.assertEqual(
            self.network.shortest_path("John", "Dave"),
            (
                [
                    self.network.user("John"),
                    self.network.user("Ed"),
                    self.network.user("Dave"),
                ],
                2,
            ),
            "The shortest path between John and Dave is John -> Ed -> Dave and has a length of 2",
        )

        self.assertEqual(
            self.network.shortest_path("Quandale", "Glen"),
            (
                [
                    self.network.user("Quandale"),
                    self.network.user("Monica"),
                    self.network.user("Finn"),
                    self.network.user("Glen"),
                ],
                3,
            ),
            "The shortest path between Quandale and Glen is Quandale -> Monica -> Finn -> Glen and has a length of 3",
        )

    def test_same_user(self):
        self.assertEqual(
            self.network.shortest_path("Alice", "Alice"),
            ([self.network.user("Alice")], 0),
            "The shortest path between Alice and Alice is Alice and has a length of 0",
        )

    def test_no_path(self):
        self.assertEqual(
            self.network.shortest_path("Alice", "Monica"),
            (None, -1),
            "There is no path between Alice and Monica",
        )

    def test_duplicate_users(self):
        alice = User("Alice")
        friendships = [(alice, alice)]

        with self.assertRaises(ValueError):
            SocialNetwork(friendships)

    def test_users_exist(self):
        with self.assertRaises(ValueError):
            self.network.shortest_path("Alice", "Not a user")


if __name__ == "__main__":
    unittest.main()
