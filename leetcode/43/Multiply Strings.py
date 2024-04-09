class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
    
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def strToList(str):
            """
                :type num: str
                :rtype: List[int]
                """
            num = []
            for symbol in str:
                num.append(int(symbol))
            return num

        def listMultipliedByDigit(num, digit):
            if digit == 0: return [0 for i in range(len(num))]
            if digit == 1: return num
            buffer = 0
            product = []
            for i in range(len(num) - 1, -1, -1):
                product.append((num[i] * digit + buffer)%10)
                buffer = (num[i] * digit + buffer) // 10
            if buffer != 0: product.append(buffer)
            return product[::-1]

        def sumOfLists(num1, num2):
            buffer = 0
            sum = []
            for i in range(- 1, -1 - len(num1), -1):
                sum.append((num1[i] + num2[i] + buffer) % 10)
                buffer = (num1[i] + num2[i] + buffer) // 10
            for i in range(-1 - len(num1), -1 - len(num2), -1):
                sum.append((num2[i] + buffer) % 10)
                buffer = (num2[i] + buffer) // 10
            if buffer > 0: sum.append(buffer)
            return sum[::-1]

        def listOfProducts(number1, number2):
            lst = []
            for i in range(len(number2) - 1, -1, -1):
                lst.append([i for i in dictOfProd[number2[i]]])
                for j in range(i , len(number2) - 1):
                    lst[-1].append(0)
            return lst

        if num1 == "0" or num2 == "0": return "0"
        number1 = strToList(num1)
        number2 = strToList(num2)
        dictOfProd = {}
        for i in range(10):
            dictOfProd[i] = listMultipliedByDigit(number1, i)

        products = listOfProducts(number1, number2)
        if len(products) == 1: answer = products[0]
        else:
            answer =  sumOfLists(products[0], products[1])
            for i in range(2, len(products)):
                answer = sumOfLists(answer, products[i])
        strAnswer = "".join(map(str, answer))
        return strAnswer