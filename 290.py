import sys

class Problem():
    def __init__(self):
        self.digit_signature = [(137 * d) % 10 for d in range(10)]
        self.digit_carry = [(137 * d) // 10 for d in range(10)]
        #print(self.digit_signature)
        #print(self.digit_carry)

    def solve(self):
        for n in [18]:
            #self.get_bruteforce(10**n)
            self.get(n)

    def get(self, n):
        diff_map = { 0 : { 0 : 1 } }

        for i in range(n):
            new_diff_map = {}
            for d in range(10):
                for diff in diff_map:
                    for carry in diff_map[diff]:
                        x = carry + self.digit_signature[d]
                        new_signature = x % 10
                        new_diff = diff + d - new_signature
                        new_carry = self.digit_carry[d] + (x // 10)
                        if new_diff not in new_diff_map:
                            new_diff_map[new_diff] = {}
                        if new_carry not in new_diff_map[new_diff]:
                            new_diff_map[new_diff][new_carry] = 0
                        new_diff_map[new_diff][new_carry] += diff_map[diff][carry]
                        #print(new_signature, new_diff, new_carry)
            diff_map = new_diff_map
        print(self.__get_count(diff_map))
            #print(new_diff_map)

    def __get_count(self, diff_map):
        #print(diff_map)
        count = 0
        for diff in diff_map:
            for carry in diff_map[diff]:
                if diff == self.get_digit_sum(carry):
                    count += diff_map[diff][carry]
                    #print(diff, carry, diff_map[diff][carry])
        return count

    def get_bruteforce(self, n):
        count = 0
        for i in range(n):
            if self.get_digit_sum(i) == self.get_digit_sum(137 * i):
                #print(i)
                count += 1
        print(count)

    def get_digit_sum(self, n):
        result = 0
        d = n
        while d > 0:
            result += (d % 10)
            d = d // 10
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
