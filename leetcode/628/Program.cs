// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");

public class Solution
{
    public int MaxProduct(int[] nums)
    {
        var sorted = nums.OrderByDescending(x => x)
            .ToArray();
        var len = sorted.Length;
        
        var first = sorted[1] * sorted[2] * sorted[0];

        var second = sorted[0] * sorted[len - 2] * sorted[len - 1];
        
        return Math.Max(first, second);
    }
}