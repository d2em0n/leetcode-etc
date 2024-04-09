class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for command in operations:
            if command == "C":
                record.pop(-1)
            elif command =="D":
                record.append(record[-1] * 2)
            elif command == "+":
                record.append(record[-1]+record[-2])
            else: record.append(int(command))
        sum = 0
        for i in record:
            sum += i
        return sum