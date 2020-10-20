import copy

"""
3 Sum - Best score so far is 244/318 test cases passed
Time limit exceeded on this input (length 121):
[0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,
-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,
1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,
-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]
Last attempted 10.14.20
Submission Detail: https://leetcode.com/submissions/detail/408722022/
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = 0
    partition = pivot + 1
    for i in range(pivot + 1, len(arr)):
        if arr[i] < arr[pivot]:
            arr[i], arr[partition] = arr[partition], arr[i]
            partition += 1
    arr[pivot], arr[partition-1] = arr[partition-1], arr[pivot]
    sorted_list = quick_sort(arr[0:partition-1]) + [arr[partition-1]] + quick_sort(arr[partition::])
    return sorted_list


def arr_is_equal(arr1, arr2):
    if arr1[0] == arr2[0] and arr1[1] == arr2[1] and arr1[2] == arr2[2]:
        return True
    return False


def three_sum(arr):
    if len(arr) < 3:
        return []
    sums_list = []
    unique_sums_list = []
    sorted_arr = quick_sort(arr)
    if sorted_arr[0] > 0 or sorted_arr[-1] < 0:
        return sums_list
    # find positive index
    pos_index = None
    for i in range(len(sorted_arr)):
        if sorted_arr[i] >= 0:
            pos_index = i
            break
    # create pairs of values, check to see if element equal to opposite of sum of pair exists in sorted_arr
    # if it does, add the array of those 3 values to sums_list
    # for i in range(len(sorted_arr)-1):
    for i in range(len(sorted_arr[0:pos_index+2]) - 1):
        for j in range(len(sorted_arr[i+1::])):
            half_sum = sorted_arr[i] + sorted_arr[i+j+1]
            if half_sum <= 0:
                for k in range(len(sorted_arr[pos_index::])):
                    if sorted_arr[pos_index::][k] == half_sum * -1 and k != i-pos_index and k != i+j+1-pos_index:  # k!=... prevents the same number from repeating in a triplet
                        sums_list.append(quick_sort([sorted_arr[i], sorted_arr[i+j+1], sorted_arr[pos_index::][k]]))
            else:
                for k in range(len(sorted_arr[0:pos_index])):
                    if sorted_arr[k] == half_sum * -1 and k != i and k != i+j+1:
                        sums_list.append(quick_sort([sorted_arr[i], sorted_arr[i+j+1], sorted_arr[k]]))
    # ignore duplicates in sums_list, return new list of unique solutions
    for list in sums_list:
        if len(unique_sums_list) == 0:
            unique_sums_list.append(list)
        else:
            is_unique = True
            for triple in unique_sums_list:
                if arr_is_equal(list, triple):
                    is_unique = False
            if is_unique:
                unique_sums_list.append(list)
    return unique_sums_list


# nums = [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]
# print(len(nums))
# print(three_sum(nums))
# print(len(three_sum(nums)))


"""
3 Sum Closest - Best score so far is 70/131 test cases passed
Last Attempted 10.14.20
Time Limit Exceeded
"""


def three_sum_closest(nums, target):
    def triplet_sum(triplet):
        return triplet[0] + triplet[1] + triplet[2]
    best_sum = nums[0] + nums[1] + nums[2]
    triplets = []
    # find all triplets possible from nums
    for i in range(len(nums)-2):
        for j in range(len(nums[i+1::])-1):
            for k in range(len(nums[i+j+2::])):
                triplets.append([nums[i], nums[i+j+1], nums[i+j+k+2]])
    for i in range(len(triplets)):
        sum = triplet_sum(triplets[i])
        if sum == target:
            return target
        if abs(sum-target) < abs(best_sum-target):
            best_sum = sum
    return best_sum

nums = [-49,-84,68,-30,30,-77,-15,-39,-98,-78,-96,13,10,14,-55,48,-13,-61,81,-77,9,85,-88,-86,-96,49,4,-34,83,67,85,-7,12,10,92,71,5,57,-11,-10,-72,65,-54,58,79,-6,-5,-93,14,44,56,-72,35,-87,4,-20,89,-85,15,-45,33,89,31,-89,15,-17,-12,31,-17,61,47,-29,98,-10,22,38,73,60,-39,82,-47,-58,-21,73,-72,25,-46,88,34,54,-19,-78,-84,-94,-18,-9,-7,-56,88,99,61,-10,-43,-83,62,-67,95,-4,-14,100,5,29,7,73,-46,20,60,81,95,-13,-32,69,56,-4,-2,68,79,-53,-14,81,-63,100,-97,-59,-9,12,84,0,19,76,8,63,-39,-38,-7,45,-51,-60,91,4,22,-74,-64,77,45,38,-95,-72,82,-52,-27,26,-74,-92,-70,97,13,-96,-77,-26,57,6,30,50,-19,68]
target = 30

# print(three_sum_closest(nums, target))


"""
Letter Combinations of a Phone Number
Last Attempted 10.18.20
Accepted w 28 ms runtime => 79.57th percentile; 14 MB memory usage => 99.98th percentile
"""


def letter_combinations(digits):
    if digits == "":
        return []
    digits_string = digits
    combinations = []
    new_combinations = []
    key = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    for letter in key[digits_string[0]]:
        combinations.append(letter)
    digits_string = digits_string[1:]
    while digits_string:
        for c in combinations:
            for letter in key[digits_string[0]]:
                new_combinations.append(c + letter)
        combinations = new_combinations
        new_combinations = []
        digits_string = digits_string[1:]
    return combinations


digits = "234"
# print(letter_combinations(digits))


"""
Merge Two Sorted Linked Lists
Last Attempted 10.18.20
Accepted w 28 ms runtime => 98.29th percentile; 14.1 MB memory usage => 99.99th percentile
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    temp = None
    runner1 = l1
    runner2 = l2
    if runner1.val <= runner2.val:
        head = runner1
    else:
        head = runner2
    while runner1 and runner2:
        if runner1.val <= runner2.val:
            try:
                while runner1.next.val <= runner2.val:
                    runner1 = runner1.next
            except AttributeError:
                pass
            temp = runner1.next
            runner1.next = runner2
            runner2 = runner2.next
            runner1.next.next = temp
        else:
            temp = runner1
            runner1 = runner2
            runner2 = runner2.next
            runner1.next = temp
    return head


list1 = ListNode(3, ListNode(5, ListNode(7)))
list2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))


def print_linked_list(ll):
    runner = ll
    while runner:
        print(runner.val)
        runner = runner.next


# print_linked_list(merge_two_lists(list1, list2))


"""
Generate Parentheses
Last Attempted 10.19.20
Accepted w 40 ms runtime => 31.67th percentile; 14.6 MB memory usage => 6.46th percentile
"""


def generate_parentheses(n):
    numPairs = n
    if numPairs == 0:
        return []
    combinations = [{
        "string": "(",
        "open": 1,
        "open_remaining": numPairs - 1
    }]
    new_combinations = []
    for i in range((numPairs * 2) - 1):
        for c in combinations:
            if c["open_remaining"] > 0 and c["open"] < numPairs:
                c1 = copy.copy(c)
                c1["string"] += "("
                c1["open"] += 1
                c1["open_remaining"] -= 1
                new_combinations.append(c1)
            if c["open"] > 0:
                c2 = copy.copy(c)
                c2["string"] += ")"
                c2["open"] -= 1
                new_combinations.append(c2)
        combinations = new_combinations
        new_combinations = []
    combinations = [c["string"] for c in combinations]
    return combinations


print(generate_parentheses(3))






