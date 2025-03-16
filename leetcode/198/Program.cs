// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");

public class Solution
{
    public int Rob(int[] nums)
    {
        var len = nums.Length;
        if (len == 1)
            return nums[0];
        var second = nums[0];
        var first = Math.Max(nums[1], second);

        for (var i = 2; i < len; i++)
        {
            var cur = Math.Max(first, second + nums[i]);
            second = first;
            first = cur;
        }
        return first;
    }
}