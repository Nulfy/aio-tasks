from pathlib import Path


def main():
    
    name = Path(__file__).name[:-3]
    inp = open(f'{name}in.txt', 'r')
    inpc = inp.read().split("\n")

    # TODO: Work here
    #
    # ERROR/CONSTRAINT CHECK HERE
    # if int(n) < 100:
    #   print("Input N is invalid (Must be less than 100)")
    #   return
    #
    # CALCULATE HERE
    # first_line = inp[0]
    # next_n_lines = inp[1:]

    out = open(f'{name}out.txt', 'w')
    out.write()
    inp.close()
    out.close()


if __name__ == '__main__':
    main()