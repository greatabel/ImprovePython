
def bad_python_loop(seq):
    for idx in range(len(seq)):
        item = seq[idx]
        print(idx, '=>', item)

def better_loop(seq):
    for idx, item in enumerate(seq):
        print(idx, '=>', item)

if __name__ == '__main__':
    seq = ['abel', 'love', 'family']
    bad_python_loop(seq)
    print('#' * 20)
    better_loop(seq)