total_requests = int(input())

registered_users = {}

for _ in range(total_requests):
    username = input()

    if username not in registered_users:
        registered_users[username] = 1
        print("OK")
    else:
        new_username = username + str(registered_users[username])
        print(new_username)
        registered_users[username] += 1