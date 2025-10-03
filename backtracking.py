def generate_parentheses(n: int) -> list[str]:
    
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:  # we can still add '('
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:  # we can add ')' only if more '(' exist
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


if __name__ == "__main__":
    N = int(input("Enter number of pairs: "))
    combos = generate_parentheses(N)
    print(f"All well-formed parentheses for n={N}:")
    for c in combos:
        print(c)
