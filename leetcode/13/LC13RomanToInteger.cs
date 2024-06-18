namespace Solution
{
    public class LC13RomanToInteger
    {
        public int RomanToInt(string s)
        {
            var answer = 0;
            var roman = new Dictionary<char, int>()
            {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000}
            };
            for (int i = 0; i < s.Length - 1; i++)
            {
                if (roman[s[i]] < roman[s[i + 1]]) answer -= roman[s[i]];
                else answer += roman[s[i]];
            }
            answer += roman[s[s.Length - 1]];
            return answer;
        }
    }
}