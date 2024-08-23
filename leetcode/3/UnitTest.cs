namespace LC3.Tests
{
    [TestClass]
    public class UnitTest1
    {
        void TestLengthOfLongestSubstring(string s, int expectedResult)
        {
            var p = new Solution();
            var result = p.LengthOfLongestSubstring(s); 
            Assert.AreEqual(expectedResult, result);
        }

        [TestMethod]
        public void Case1()
        {
            TestLengthOfLongestSubstring("abcabcbb", 3);
        }
        [TestMethod]
        public void Case2()
        {
            TestLengthOfLongestSubstring("bbbbb", 1);
        }
        [TestMethod]
        public void Case3()
        {
            TestLengthOfLongestSubstring("pwwkew", 3);
        }

        [TestMethod]
        public void SingleSymbol()
        {
            TestLengthOfLongestSubstring(" ", 1);
        }

        [TestMethod]
        public void EmptryString()
        {
            TestLengthOfLongestSubstring("", 0);
        }
        [TestMethod]
        public void Case120()
        {
            TestLengthOfLongestSubstring("au", 2);
        }
        
        [TestMethod]
        public void Case155()
        {
            TestLengthOfLongestSubstring("aab", 2);
        }

        [TestMethod]
        public void Case157()
        {
            TestLengthOfLongestSubstring("dvdf", 3);
        }
    }
}