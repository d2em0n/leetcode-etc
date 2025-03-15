// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");
public class Solution 
{
    public int[] ProductExceptSelf(int[] nums)
    {
        var left = 1;
        var len = nums.Length;
        var answer = new int[len];
        for (var i = 0; i < len; i++)
        {
            answer[i] = left;
            left *= nums[i];
        }

        var right = 1;
        for (var i = len - 1; i > -1; i--)
        {
            answer[i] *= right;
            right *= nums[i];
        }
        return answer;
    }
}
 
