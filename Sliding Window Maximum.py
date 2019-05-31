class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        window, result = [], []
        for index, number in enumerate(nums):
            if index >= k and window[0] <= index - k:
                window.pop(0)
            while window and nums[window[-1]] <= number:
                window.pop()
            window.append(index)
            if index >= k - 1:
                result.append(nums[window[0]])
        return result


if __name__ == '__main__':
    test = [7, 2, 4]
    s = Solution()
    res = s.maxSlidingWindow(test, 2)
    for r in res:
        print(r)

