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
        var nums = new [] {1, 2, 3, 4};
        var output = new [] {24,12,8,6};
        var result = _solution.ProductExceptSelf(nums);
        result.Should().BeEquivalentTo(output);
    }
    
    [Test]
    public void Test2()
    {
        var nums = new [] {-1,1,0,-3,3};
        var output = new [] {0,0,9,0,0};
        var result = _solution.ProductExceptSelf(nums);
        result.Should().BeEquivalentTo(output);
    }
}