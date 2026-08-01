class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        visit = set(deadends)
        if "0000" in visit:
            return -1

        begin = {"0000"}
        end = {target}
        steps = 0

        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin

            steps += 1
            temp = set()
            for lock in begin:
                for i in range(4):
                    for j in [-1, 1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextLock = lock[:i] + digit + lock[i+1:]

                        if nextLock in end:
                            return steps
                        if nextLock in visit:
                            continue
                        visit.add(nextLock)
                        temp.add(nextLock)
            begin = temp
        return -1