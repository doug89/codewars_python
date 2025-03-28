import math
def alignment(string, length, position, padding):
    pos = position.lower()
    if pos not in "lcr":
        return None
    if length < len(string):
        return None
    if len(padding) != 1:
        return None
    pad_len = length - len(string)
    if pos == "l":
        return string + padding * pad_len
    if pos == "r":
        return padding * pad_len + string
    if pos == "c":
        return padding * int(math.floor(pad_len/2)) + string + padding * int(math.ceil(pad_len/2))

word = "Hello"
print(f"|{alignment(word, 4, "l", " ")}|")
print(f"|{alignment(word, 4, "c", " ")}|")
print(f"|{alignment(word, 4, "r", " ")}|")
