class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        vector = [0, 0, 0]
        # 0 - North, 1 - East, 2 - South, 3 - West
        for command in instructions:
            if command == "R": 
                vector[2] += 1
                if vector[2] == 4: vector[2] = 0
            elif command == "L":
                vector[2] -= 1
                vector[2] = vector[2] % 4
                if vector[2] < 0: vector[2] += 4
            else:
                if vector[2] == 0: vector[1] += 1
                elif vector[2] == 1: vector[0] += 1
                elif vector[2] == 2: vector[1] -= 1
                elif vector[2] == 3: vector[0] -= 1

        if vector[0] == 0 and vector[1] == 0: return True
        elif vector[2] != 0: return True
        else: return False