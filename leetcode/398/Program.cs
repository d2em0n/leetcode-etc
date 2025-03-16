// See https://aka.ms/new-console-template for more information

Console.WriteLine("Hello World!");

public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        var tLength = t.Length;
        var sLength = s.Length;
        if (sLength == 0)
            return true;
        if (tLength ==0)
            return false;
        var first = 0;
        var second = 0;

        while (second < tLength)
        {
            if (first == sLength)
                return true;
            if (t[second] == s[first])
            {
                first++;
                second++;
            }
            else
                second++;
        }
        return first == sLength;
    }
}