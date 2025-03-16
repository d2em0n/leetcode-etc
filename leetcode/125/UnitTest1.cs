using FluentAssertions;
namespace TestProject1;

public class Tests
{
    private Solution _solution;
    [SetUp]
    public void Setup()
    {
        _solution = new Solution();
    }

    [Test]
    public void Test1()
    {
        var s = "A man, a plan, a canal: Panama";
        var output = true;
        var result = _solution.IsPalindrome(s);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test2()
    {
        var s = "race a car";
        var output =false;
        var result = _solution.IsPalindrome(s);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test3()
    {
        var s = " ";
        var output =true;
        var result = _solution.IsPalindrome(s);
        result.Should().Be(output);
    }
}