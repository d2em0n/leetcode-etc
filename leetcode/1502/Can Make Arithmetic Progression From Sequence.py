class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
            if len(arr) == 2: return True
            arr.sort()

            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] == arr[i-1] - arr[i-2]:
                    continue
                else: return False

            return True