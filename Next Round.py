total_players, qualifying_place = map(int, input().split())

scores = list(map(int, input().split()))

cutoff_score = scores[qualifying_place - 1]

qualified = 0

for score in scores:
    if score >= cutoff_score and score > 0:
        qualified += 1

print(qualified)