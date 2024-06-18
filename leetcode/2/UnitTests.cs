using LC2;

namespace AddTwoNumbersTest
{
    [TestClass]
    public class UnitTest1
    {
        public static ListNode IntArrayToListNode(int[] array)
        {
            if (array.Length == 0) throw new Exception();
            var current = new ListNode(array[0], null);
            var result = current;
            for (int i = 1; i < array.Length; i++)
            {
                current.next = new ListNode(array[i]);
                current = current.next;
            }
            return result;
        }

        public static int[] ListNodeToIntArray(ListNode listNode)
        {
            var list = new List<int>();
            while (listNode.next != null)
            {
                list.Add(listNode.val);
                listNode = listNode.next;
            }
            list.Add((int)listNode.val);
            return list.ToArray();
        }

        public static int[] EvaluateResult(int[] arr1, int[] arr2)
        {
            var l1 = IntArrayToListNode(arr1);
            var l2 = IntArrayToListNode(arr2);

            var solution = new Solution();
            var result = solution.AddTwoNumbers(l1, l2);
            return ListNodeToIntArray(result);
        }

        public static void Test(int[] arr1, int[] arr2, int[] givenResult)
        {
            var evaluatedResult = EvaluateResult(arr1, arr2);
            Assert.AreEqual(evaluatedResult.Length, givenResult.Length); 
            for (int i = 0; i < givenResult.Length; i++)
                Assert.AreEqual(evaluatedResult[i], givenResult[i]);
        }
        [TestMethod]

        public void Test1()
        {
            Test(new [] { 2, 4, 3}, new [] { 5, 6, 4}, new [] {7, 0, 8 } );
        }

        [TestMethod]
        public void Test2()
        {
            Test(new[] {0}, new[] {0}, new[] {0});
        }

        [TestMethod]
        public void Test3()
        {
            Test(new[] { 9, 9, 9, 9, 9, 9, 9 }, new[] { 9, 9, 9, 9 }, new[] { 8, 9, 9, 9, 0, 0, 0, 1 });
        }

        [TestMethod]
        public void Test4()
        {
            Test(new[] { 8, 3, 2 }, new[] { 9, 2, 1 }, new[] { 7, 6, 3 });
        }
    }
}