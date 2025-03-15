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
        var nums = new [] {2,3,-2,4};
        var output = 6;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test2()
    {
        var nums = new [] {-2,0,-1};
        var output = 0;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }

    [Test]
    public void Test3()
    {
        var nums = new [] {-2,3,-4};
        var output = 24;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }
}