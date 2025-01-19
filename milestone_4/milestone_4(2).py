from typing import List, Tuple

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i 


assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

#Time complexity^ O(n) , Space complexity: O(n)