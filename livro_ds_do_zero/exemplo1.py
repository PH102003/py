users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

print(f"pares: {friendship_pairs[0], friendship_pairs[1]}")

friendships = {user["id"]: [] for user in users}
print(f"Amizades:{friendships}\n \n")
"""nesse caso aqui, é demonstrado com qual número é feito "amizade", 
exemplo, o amigo 0, faz amizade com o 1 e 2, etc...
""" 
for i, j in friendship_pairs:
    friendships[i].append(j) # Adicione j como amigo do usuário i
    friendships[j].append(i) # Adicione i como amigo do usuário j
    print(friendships)