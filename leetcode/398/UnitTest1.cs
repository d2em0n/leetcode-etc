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
        var s = "abc";
        var t = "ahbgdc";
        var output = true;
        var result = _solution.IsSubsequence(s, t);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test2()
    {
        var s = "axc";
        var t = "ahbgdc";
        var output = false;
        var result = _solution.IsSubsequence(s, t);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test3()
    {
        var s = "";
        var t = "ahbgdc";
        var output = true;
        var result = _solution.IsSubsequence(s, t);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test4()
    {
        var s = "b";
        var t = "abc";
        var output = true;
        var result = _solution.IsSubsequence(s, t);
        result.Should().Be(output);
    }
}