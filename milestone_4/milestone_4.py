from typing import List
def find_sum(target: int, li: List[int]) -> tuple[int , int]:
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return i,j
assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)} 

# Time Complexity: O(n^2) , Space Complexity: O(1)