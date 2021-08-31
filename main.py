from plrs import Lexer, EMPTY_TOKEN, Settings, Tokens
import matplotlib.pyplot as plt

RANK = {}

with open("text.txt") as file:

    current_token = EMPTY_TOKEN
    lexer = Lexer(file.read(), Settings.NONE)

    while current_token.token != Lexer.EOF:
        current_token = lexer.next()
        if current_token.token == Tokens.Identifier.value:
            if current_token.part not in RANK:
                RANK[current_token.part] = 1
            else:
                RANK[current_token.part] += 1

if __name__ == "__main__":
    data = sorted(RANK.values(), reverse=True)
    num_line = range(1, len(RANK) + 1)

    ranked = sorted(RANK.items(), key=lambda x: x[1], reverse=True)
    most_used = "\n" + "".join([f"-  {x}: {y}\n" for x, y in ranked[:10]])
    least_used = "\n" + "".join([f"-  {x}: {y}\n" for x, y in ranked[-10:]])

    print(f"Most used: {most_used}")
    print(f"Least used: {least_used}")

    plt.bar(num_line, data)
    plt.show()
