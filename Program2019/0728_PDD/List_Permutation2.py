def permute(list, s):
    if list == 1:
        return s
    else:
        return [y + x
                for y in permute(1, s)
                for x in permute(list - 1, s)
                ]


if __name__ == '__main__':
    print(permute(1, ["a", "b", "c"]))
    print(permute(2, ["a", "b", "c"]))
    print(permute(3, ["a", "b", "c"]))
