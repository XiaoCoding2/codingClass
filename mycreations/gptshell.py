lines = [
    [1, 2, 3],
    [2, 3, 3],
    [1, 3, 3]
]

max_score = 0

for start in range(3):  # pebble starts under cup 1, 2, or 3
    cups = [0, 0, 0]
    cups[start] = 1
    score = 0
    for a, b, g in lines:
        a -= 1
        b -= 1
        g -= 1
        cups[a], cups[b] = cups[b], cups[a]
        if cups[g] == 1:
            score += 1
    max_score = max(max_score, score)

print("Correct USACO Output:", max_score)
