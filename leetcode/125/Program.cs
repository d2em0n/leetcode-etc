// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");

public class Solution
{
    public bool IsPalindrome(string s)
    {
        var len = s.Length;
        var left = 0;
        var right = len - 1;
        while (left < right)
        {
            while (left < right && !Char.IsLetterOrDigit(s[left]))
                left++;
            while (left < right && !Char.IsLetterOrDigit(s[right]))
                right--;
            if (Char.ToLower(s[left]) != Char.ToLower(s[right]))
                return false;
            left++;
            right--;
        }
        return true;
    }
}