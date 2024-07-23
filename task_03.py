from collections import deque as Deque


def is_symmetric(txt: str) -> bool:
    brackets: dict = {')': '(', '}': '{', ']': '['}

    stack: Deque = Deque()

    for char in txt:
        open_brackets = brackets.values()
        if char in open_brackets:
            stack.append(char)
            continue

        close_brackets = brackets.keys()
        if char in close_brackets:
            if not len(stack) or stack[-1] != brackets[char]:
                return False

            stack.pop()

    return not len(stack)


# TESTING

def _should_check_if_symmetric():
    assert is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}")
    assert not is_symmetric("( 23 ( 2 - 3);")
    assert not is_symmetric("( 11 }: ")


if __name__ == "__main__":
    _should_check_if_symmetric()
