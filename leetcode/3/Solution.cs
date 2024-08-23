namespace LC3
{
    public class Solution
    {
        public int LengthOfLongestSubstring(string s)
        {
            if (s.Length == 0) return 0;
            var q = new Queue<char>();
            var d = new Dictionary<char, int>();
            var maxCount = 1;
            q.Enqueue(s[0]);
            d.Add(s[0], 0);
            for (int i = 1; i< s.Length; i++)
            {
                if (!d.ContainsKey(s[i]))
                {
                    q.Enqueue(s[i]);
                    d.Add(s[i], i);
                }
                else
                {
                    maxCount = Math.Max(maxCount, q.Count);
                    var prevPos = d[s[i]];                    
                    var firstInQueue = q.Peek();
                    var j = d[firstInQueue];
                    d[s[i]] = i;                    
                    for (; j < prevPos; j++)
                    {
                        var valToDel = q.Dequeue();
                        d.Remove(valToDel);
                    }
                    q.Dequeue();
                    q.Enqueue(s[i]);
                }
            }
            maxCount = Math.Max(maxCount, q.Count);
            return maxCount;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
