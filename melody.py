from pathlib import Path


def main():
    
    name = Path(__file__).name[:-3]
    inp = open(f'{name}in.txt', 'r')
    inpc = inp.read().split("\n")

    notes = chunks(inpc[1:], 3)
    first_note = []

    n = int(inpc[0].split()[0])
    k = int(inpc[0].split()[1])

    if not 3 <= n <= 99999:
        print("N is not a valid input (Must be between 3 and 99999, inclusive)")
        return
    
    if not (n / 3).is_integer():
        print("N is not a valid input (Must be a multiple of 3)")
        return

    if not 1 <= k <= 100000:
        print("K is not a valid input (Must be between 1 and 100000, inclusive)")
        return

    for i in inpc[1:]:
        if not 1 <= int(i) <= k:
            print(f"Notes entered are invalid (Must be between 1 and {k}, inclusive)")
            return
    
    final = 0
    
    for i, note in enumerate(notes):
        if i == 0:
            first_note = note
        else:
            if note[0] != first_note[0]:
                final += 1
            if note[1] != first_note[1]:
                final += 1
            if note[2] != first_note[2]:
                final += 1

    out = open(f'{name}out.txt', 'w')
    out.write(str(final))
    inp.close()
    out.close()


def chunks(xs, n):
    n = max(1, n)
    return (xs[i:i+n] for i in range(0, len(xs), n))


if __name__ == '__main__':
    main()