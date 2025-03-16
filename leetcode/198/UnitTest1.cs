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
        var nums = new [] {1, 2, 3, 1};
        var output = 4;
        var result = _solution.Rob(nums);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test2()
    {
        var nums = new [] {2,7,9,3,1};
        var output =12;
        var result = _solution.Rob(nums);
        result.Should().Be(output);
    }
}