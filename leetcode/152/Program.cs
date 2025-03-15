// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");
public class Solution
{
    public int MaxProduct(int[] nums) 
    {
        var maxProduct = nums[0];
        var minProduct = nums[0];
        var result = nums[0];
        for (var i = 1; i < nums.Length; i++)
        {
            if (nums[i] < 0)
            {
                var buf = minProduct;
                minProduct = maxProduct;
                maxProduct = buf;
            }
            var posMax = maxProduct*nums[i];
            var posMin = minProduct*nums[i];
            maxProduct = Math.Max(nums[i], posMax);
            minProduct = Math.Min(nums[i], posMin);
            result = Math.Max(result, maxProduct);
        }
        return result;
    }
}
 
