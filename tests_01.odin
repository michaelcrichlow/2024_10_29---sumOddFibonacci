package test

import "core:fmt"
print :: fmt.println


main :: proc() {

	print(sumOddFibonacci(10))
	print(sumOddFibonacci(1_000))
	print(sumOddFibonacci(4_000_000))

	free_all(context.temp_allocator)

	// OUTPUT:
	// 10
	// 1785
	// 4613732
}

create_fibonanni_array_up_to :: proc(n: int) -> []int {
	local_array := make([dynamic]int, allocator = context.temp_allocator)
	append(&local_array, 0, 1)
	num := 1

	for num < n {
		num = local_array[len(local_array) - 1] + local_array[len(local_array) - 2]
		if num <= n {
			append(&local_array, num)
		}
	}

	return local_array[:]
}

sumOddFibonacci :: proc(n: int) -> int {
	fib_array := create_fibonanni_array_up_to(n)
	local_array := make([dynamic]int, allocator = context.temp_allocator)

	for val in fib_array {
		if val % 2 != 0 {
			append(&local_array, val)
		}
	}
	return sum_iterable(local_array[:])
}
