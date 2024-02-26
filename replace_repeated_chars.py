def replace_repeated_chars(s: str, k: int) -> str:
    # Initialize an empty list to hold the result characters
    result = []
    # Use a set to keep track of the characters seen in the last k characters
    seen = set()
    # Use a queue to keep track of the order of the last k characters seen
    queue = []

    for char in s:
        # If the character has been seen in the last k characters, replace it with '-'
        if char in seen:
            result.append('-')
        else:
            result.append(char)
            seen.add(char)
            queue.append(char)
            # If the queue length exceeds k, remove the oldest character from seen
            if len(queue) > k:
                removed_char = queue.pop(0)
                seen.remove(removed_char)

    return ''.join(result)

# Test the function with the provided examples
test_cases = [
    ("abcdefaxc", 10),
    ("abcdefaxcqwertba", 10)
]

outputs = [replace_repeated_chars(s, k) for s, k in test_cases]
outputs
