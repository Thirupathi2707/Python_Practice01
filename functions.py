def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Education"))

def largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(largest([10, 25, 7, 40, 18]))

def second_largest(numbers):
    largest = numbers[0]
    second = None

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    return second

print(second_largest([10, 25, 7, 40, 18]))


def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
