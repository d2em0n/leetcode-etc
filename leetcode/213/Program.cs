// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");

public class Solution
{
    private static int RobHelper(IEnumerable<int> nums)
    {
        var first = 0;
        var second = 0;
        foreach (var num in nums)
        {
            var cur = Math.Max(first,  num + second);
            second = first;
            first = cur;
        }
        return first;
    }

    public int Rob(int[] nums)
    {
        var len = nums.Length;
        if (len == 1)
            return nums[0];
        var first = RobHelper(nums.Take(len - 1));
        var second = RobHelper(nums.Skip(1));
        return Math.Max(first, second);
    }
}