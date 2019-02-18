def is_anagrama(a, b):
    if len(a) != len(b):
        return 0
    for i in range(len(a)):
        if a[i] in b:
            b.replace(a[i], "0", 1)
            a.replace(a[i], "0", 1)
        else:
            return 0
    if b == a:
        return 1


a = "fresa"
b = "frase"
c = "holaa"

d = "aaaaaaabb"
e = "aaaaabbbb"
print(is_anagrama(d, e))
print(is_anagrama(a, b))
print(is_anagrama(a, c))
