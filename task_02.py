from collections import deque as Deque

def is_palindrom(txt: str) -> bool:
    txt = txt.lower().replace(" ", "")

    deque: Deque = Deque()

    for letter in txt:
        deque.append(letter)

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
        
    return True

# TESTING

def _should_check_if_palindrom():
    assert is_palindrom("Wow")
    assert is_palindrom("Wo  w ")
    assert is_palindrom("Woow")
    assert not is_palindrom("Whow")


if __name__ == "__main__":
    _should_check_if_palindrom()