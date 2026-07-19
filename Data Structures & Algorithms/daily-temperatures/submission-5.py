class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temps = []
        stack_indexes = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack_temps:
                stack_temps.append(t)
                stack_indexes.append(i)
            elif stack_temps[-1] > t:
                stack_temps.append(t)
                stack_indexes.append(i)
            else:
                while stack_temps and stack_temps[-1] < t:
                    prev_index = stack_indexes.pop()
                    result[prev_index] = i - prev_index
                    stack_temps.pop()
                stack_temps.append(t)
                stack_indexes.append(i)
        return result
        