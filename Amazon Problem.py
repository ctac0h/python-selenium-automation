"""
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

"""

from random import randint


def first_unique(s):
    if s == '':
        return ''
    s = s.lower()
    ch = {}
    for x in s:
        if x in ch:
            ch[x] += 1
        else:
            ch[x] = 1
    for y in ch:
        if ch[y] == 1:
            return y
    return ''


def first_unique_case_sensitive_slow(s):
    for x in s:
        if s.lower().count(x.lower()) == 1:
            return x
    return ''


def first_unique_case_sensitive_cached(s):
    if s == '':
        return ''
    cache = set()
    for x in s:
        if x.lower() not in cache:
            if s.lower().count(x.lower()) == 1:
                return x
            else:
                cache.add(x.lower())
    return ''


# Tests
long_string = ''
for i in range(100000):
    long_string += str(randint(0, 9))
long_string += 'ZzXCcg'


print('first_unique:')
print(first_unique(''))                 # ''
print(first_unique('qwerty'))           # 'q'
print(first_unique('qwweerrttyy'))      # 'q'
print(first_unique('qqwweerrtty'))      # 'y'
print(first_unique('qwertyqwerty'))     # ''
print(first_unique('qwerqwe'))          # 'r'
print(first_unique('qw eqwe'))          # ' '
print(first_unique(long_string))        # 'x'
print('========')


print('first_unique_case_sensitive_cached:')
print(first_unique_case_sensitive_cached(''))                 # ''
print(first_unique_case_sensitive_cached('qwerty'))           # 'q'
print(first_unique_case_sensitive_cached('qwweerrttyy'))      # 'q'
print(first_unique_case_sensitive_cached('qqwweerrtty'))      # 'y'
print(first_unique_case_sensitive_cached('qwertyqwerty'))     # ''
print(first_unique_case_sensitive_cached('qwerqwe'))          # 'r'
print(first_unique_case_sensitive_cached('qw eqwe'))          # ' '
print(first_unique_case_sensitive_cached(long_string))        # 'X'
print('========')

print('first_unique_case_sensitive_slow')
print(first_unique_case_sensitive_slow(''))                 # ''
print(first_unique_case_sensitive_slow('qwerty'))           # 'q'
print(first_unique_case_sensitive_slow('qwweerrttyy'))      # 'q'
print(first_unique_case_sensitive_slow('qqwweerrtty'))      # 'y'
print(first_unique_case_sensitive_slow('qwertyqwerty'))     # ''
print(first_unique_case_sensitive_slow('qwerqwe'))          # 'r'
print(first_unique_case_sensitive_slow('qw eqwe'))          # ' '
print(first_unique_case_sensitive_slow(long_string))        # 'X'
print('========')


