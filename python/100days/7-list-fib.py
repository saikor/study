print('-----------fib------------------')
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(10):
        print(val)


if __name__ == '__main__':
    main()
    # print(type(fib(5)))  # <class 'generator'>
