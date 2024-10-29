def create_fibonanni_array_up_to(n: int) -> list[int]:
    local_array = [0, 1]
    num = 1
    while num < n:
        num = local_array[-1] + local_array[-2]
        if num <= n:
            local_array.append(num)

    return local_array


def sumOddFibonacci(n: int) -> int:
    fib_array = create_fibonanni_array_up_to(n)
    local_array = []
    for val in fib_array:
        if val % 2 != 0:
            local_array.append(val)
    return sum(local_array)


def main() -> None:
    print(sumOddFibonacci(10))
    print(sumOddFibonacci(1_000))
    print(sumOddFibonacci(4_000_000))

    # OUTPUT:
    # 10
    # 1785
    # 4613732


if __name__ == '__main__':
    main()
