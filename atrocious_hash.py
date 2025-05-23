data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow, citrus fruit"),
    ("grape", "a small, sweet fruit growing in branches"),
    ("melon", "sweet and juicy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """ A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str | None:
    """ Return the value for a key, or None if the key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
value = get("lemon")
print(value)
