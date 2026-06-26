days, total_hours = map(int, input().split())

minimum_hours = []
maximum_hours = []

for _ in range(days):
    low, high = map(int, input().split())
    minimum_hours.append(low)
    maximum_hours.append(high)

min_possible = sum(minimum_hours)
max_possible = sum(maximum_hours)

if total_hours < min_possible or total_hours > max_possible:
    print("NO")
else:
    print("YES")

    study_plan = minimum_hours.copy()
    remaining_hours = total_hours - min_possible

    for i in range(days):
        extra_capacity = maximum_hours[i] - study_plan[i]

        if remaining_hours >= extra_capacity:
            study_plan[i] += extra_capacity
            remaining_hours -= extra_capacity
        else:
            study_plan[i] += remaining_hours
            remaining_hours = 0

    print(*study_plan)