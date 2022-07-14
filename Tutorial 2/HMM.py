import random
bases = ['A', 'T', 'C', 'G']
states = []
string = ''


def at_rich_state(number):
    global string

    if len(string) < number:
        string += random.choices(bases, weights=(0.2698, 0.3237, 0.2028, 0.1985))[0]
        states.append('AT')
    else:
        return string

    while random.choices(['stay', 'go'], weights=(0.9998, 0.0002))[0] == 'stay' and len(string) < number:
        string += random.choices(bases, weights=(0.2698, 0.3237, 0.2028, 0.1985))[0]
        states.append('AT')

    if len(string) < number:
        return cg_rich_state(number)
    else:
        return string


def cg_rich_state(number):
    global string

    if len(string) < number:
        string += random.choices(bases, weights=(0.2459, 0.2079, 0.2478, 0.2984))[0]
        states.append('CG')
    else:
        return string

    while random.choices(['stay', 'go'], weights=(0.9997, 0.0003))[0] == 'stay' and len(string) < number:
        string += random.choices(bases, weights=(0.2459, 0.2079, 0.2478, 0.2984))[0]
        states.append('CG')

    if len(string) < number:
        return at_rich_state(number)
    else:
        return string


def main():
    start = random.choices(['at', 'cg'], weights=(0.5, 0.5))[0]

    if start == 'at':
        print(at_rich_state(200))
    else:
        print(cg_rich_state(200))

    print(states)


if __name__ == "__main__":
    main()

# show transitions between states using graph perhaps
# Submission for whole tutorial is pdf about two pages. don't show code
# no start state so randomly choose
