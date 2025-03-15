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
        var nums = new [] {1, 2, 3};
        var output = 6;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test2()
    {
        var nums = new [] {1,2,3,4};
        var output =24;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }

    [Test]
    public void Test3()
    {
        var nums = new [] {-1,-2,-3};
        var output = -6;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    }
    
    [Test]
    public void Test4()
    {
        var nums = new [] {-100,-98,-1,2,3,4};
        var output = 39200;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    } 
    [Test]
    public void Test5()
    {
        var nums = new [] {-3,-2,-1,0,0,0,0};
        var output = 0;
        var result = _solution.MaxProduct(nums);
        result.Should().Be(output);
    } 
}