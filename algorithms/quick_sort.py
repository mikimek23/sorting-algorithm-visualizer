from random import randint

def quick_Sort(nums, low, high):
    yield ("current", low, high)
    if low >= high:
        return
    pivot = nums[high]
    yield ("pivot", high, pivot)
    i = low - 1
    for j in range(low, high):
        yield ("compare", j, high)
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
            yield ("swap", i, j)
            yield ("partition", i)
        else:
            yield ("no_swap", i, j)
    i += 1
    yield ("compare", i, high)
    nums[i], nums[high] = nums[high], nums[i]
    yield ("swap_pivot", i, high)
    yield ("pivot_fixed", i)
    yield ("left_partition", low, i - 1)
    yield from quick_Sort(nums, low, i - 1)
    yield ("right_partition", i + 1, high)
    yield from quick_Sort(nums, i + 1, high)


nums = [randint(1, 99) for _ in range(5)]
results = quick_Sort(nums, 0, len(nums) - 1)
for result in results:
    print(result)
