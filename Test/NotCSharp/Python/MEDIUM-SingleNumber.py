# https://leetcode.com/problems/single-number/discuss/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Logic: XOR will return 1 only on two different bits. 
        So if two numbers are the same, XOR will return 0. Finally only one number left.
        Imagine an array of 5 numbers [A,A,B,B,C], here C is the single number
        if we were to take xor of all numbers we have - A^A^B^B^C, 
        now A xor A = 0, B xor B = 0, 0 xor C = C. Hence we return C 
        '''
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res