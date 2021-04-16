import random

mrdare = {
    "subjects": {"Maths": 3, "English": 2, "Civics": 1, "Rhetoric": 1,"Biology": 1, "Literature": 2}
}

# Ma


def main():
    # print("My anme")

    # rand = [random.sample(range(2), 2) for _ in range(2)]
    # print(rand)

    # for i in range(2):
    #     ran = []
    # av = 0

    for i in range(4):
        ran = unique_rand(0, 5, 5)
        # print("Num", ran)
        rand = ran[i]
        first_key = get_nth_key(mrdare["subjects"], rand)
        print(first_key, mrdare["subjects"][first_key])

        # ran = rand[i]

    # val = mrdare["subjects"][first_key]
    # print(val)


def get_first_key(dictionary):
    for key in dictionary:
        return key
    raise IndexError

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def unique_rand(inicial, limit, total):
    data = []

    i = 0

    while i < total:
        number = random.randint(inicial, limit)
        if number not in data:
            data.append(number)
            i += 1

    return data


if __name__ == '__main__':
    main()
