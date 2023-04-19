# Social-Network

<h1>How did you represent the social network? Why did you choose this representation?</h1>
I represented the social network as a graph. The graph is represeted as an adjacency list. An instance of the SocialNetwork class holds a list of user objects. Each user object holds a name and a set of friends. 
I chose this representation because it is the most efficient way to represent a social network. It is also the most intuitive way to represent a social network.
<br>

<h1>What algorithm did you use to compute the shortest chain of friends? What alternatives did you consider? Why did you choose this algorithm over the alternatives?</h1>
I used a breadth first search to compute the shortest chain of friends.
<br>
I considered using a depth first search, but I decided against it because it would not be as efficient as a breadth first search.
Because the breadth first search visits all the nodes at the current level before moving on to the next level, it will find a node at a shallow level faster than a depth first search. DFS can be faster if the node you are looking for is at a deeper level, but a social network is usually a dense graph, so the node you are looking for is likely to be at a shallow level.
<br>
I also considered using a Dijkstra's algorithm, but I decided against it my graph is unweighted. Dijkstra's algorithm is used for weighted graphs. I could have use Dijkstra's algorithm if I had assigned weight 1 to all the edges, but then it would have been the same as using a breadth first search.
The efficiency of the breadth first search is O(V+E), where V is the number of users and E is the number of friendships in the network. This is because the algorithm visits each node once and each edge at most once.
<br>

<h1>Please enumerate the test cases you considered and explain their relevance.</h1>
I considered the following test cases:
<br>
1. The shortest chain of friends between two users who are friends: I built a social network with multiple users and made sure that the shortest chain of friends between two users who are friends was found.
<br>
2. The shortest path between a user and himself: I built a social network with multiple users and made sure that the shortest chain of friends between a user and himself has length 0.
<br>
3. There is no path between two users: I built a social network with multiple users and made sure that the shortest chain of friends between two users who are not friends was not found.
<br>
4. A user can't be friends with himself: I built a social network with multiple users and made sure that a user can't be friends with himself.
<br>
5. One or both of the users are not in the social network: I built a social network with multiple users and made sure that the shortest chain of friends between two users who are not in the social network was not found.
