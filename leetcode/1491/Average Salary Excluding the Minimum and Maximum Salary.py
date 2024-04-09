class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min = 0
        max = 0
        sum = float(salary[0] + salary[1])
        if (salary[0] > salary[1]):
            min = salary[1]
            max = salary[0]
        else:
            min = salary[0]
            max = salary[1]
        for i in range(2, len(salary)):
            if salary[i] > max: max = salary[i]
            if salary[i] < min: min = salary[i]
            sum += salary[i]
        return float("{:.5f}".format((sum - min - max) / (len(salary) - 2)))