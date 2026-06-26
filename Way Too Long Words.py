total_words = int(input())

for _ in range(total_words):
    current_word = input().strip()

    if len(current_word) > 10:
        abbreviated_word = (
            current_word[0]
            + str(len(current_word) - 2)
            + current_word[-1]
        )
        print(abbreviated_word)
    else:
        print(current_word)