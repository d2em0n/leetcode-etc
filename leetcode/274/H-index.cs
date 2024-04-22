public class Solution
{
    public int HIndex(int[] citations)
    {
        var n = citations.Length;
        var temp = new int[citations.Length + 1];
        foreach (var citation in citations)
        {
            if (citation > n)
            {
                temp[n] += 1;
            }
            else
            {
                temp[citation] += 1;
            }

        }
        var total = 0;
        for (var i = n; i > -1; i--)
        {
            total += temp[i];
            if (total >= i)
            {
                return i;

            }
        }
        return total;

    }
}