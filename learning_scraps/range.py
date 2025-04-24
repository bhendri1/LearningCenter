def show_range(stop):
    print(f'for i in range({stop}):')
    for i in range(stop):
        print(f'\t{i}')

def show_range_2(start, stop):
    print(f'for i in range({start}, {stop}):')
    for i in range(start, stop):
        print(f'\t{i}')

def show_range_3(start, stop, step):
    print(f'for i in range({start}, {stop}, {step}):')
    for i in range(start, stop, step):
        print(f'\t{i}')

if __name__ == "__main__":
    show_range(6)
    print()
    print()
    show_range_2(2, 6)
    print()
    print()
    show_range_3(2, 6, 2)