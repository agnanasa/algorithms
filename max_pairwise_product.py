def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()  # Sorts the list in place
    return numbers[n-1] * numbers[n-2]  # Access the two largest numbers


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

