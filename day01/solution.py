
def solve1(arr1: list[int], arr2: list[int]) -> int:
    """
    Takes in the two lists, sorts them, and then finds the total distance differences
    """
    if len(arr1) != len(arr2):
        raise ValueError("Array lengths are not equal")

    # Sort both in O(nlogn) time
    arr1.sort()
    arr2.sort()

    total: int = 0

    i: int = 0
    while i < len(arr1):
        i1: int = arr1[i]
        i2: int = arr2[i]

        difference: int = abs(i1 - i2)
        total += difference

        i += 1

    return total

def solve2(arr1: list[int], arr2: list[int]) -> int:
    counts: dict[int, int] = {}
    for num in arr2:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    total: int = 0
    for num in arr1:
        if num not in counts:
            continue

        total += (num * counts[num])
    
    return total

if __name__ == "__main__":

    arr1: list[int] = []   
    arr2: list[int] = []   

    file = open("./input.txt")
    lines: list[str] = file.read().splitlines()
    file.close()

    for line in lines:
        i1, i2 = line.split("   ")
        i1: int = int(i1)
        i2: int = int(i2)

        # We could do a heap here but eh lets see
        arr1.append(i1)
        arr2.append(i2)

    answer1: int = solve1(arr1, arr2)
    print(answer1)

    answer2: int = solve2(arr1, arr2)
    print(answer2)
