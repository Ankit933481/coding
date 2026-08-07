class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, and 7
        temp_t = t
        c2 = c3 = c5 = c7 = 0

        while temp_t % 2 == 0:
            c2 += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            c3 += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c5 += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            c7 += 1
            temp_t //= 7

        # Prime factors > 7 cannot be formed by any digit product
        if temp_t > 1:
            return "-1"

        # Prime factor count lookup table for digits 0-9
        f2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        f3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        f5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        f7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        # Returns the minimum number of digits needed to supply (r2, r3, r5, r7) factors
        def min_len(r2, r3, r5, r7):
            r2 = max(0, r2)
            r3 = max(0, r3)
            r5 = max(0, r5)
            r7 = max(0, r7)

            min_23_digits = float("inf")
            # Try combining twos and threes into digit '6' (0, 1, or 2 times)
            for k6 in range(3):
                rem2 = max(0, r2 - k6)
                rem3 = max(0, r3 - k6)
                d2 = (rem2 + 2) // 3  # Using 8s (and 4, 2)
                d3 = (rem3 + 1) // 2  # Using 9s (and 3)
                min_23_digits = min(min_23_digits, k6 + d2 + d3)

            return r5 + r7 + min_23_digits

        # Fills a string of target `length` with lexicographically smallest valid digits
        def fill_smallest(length, r2, r3, r5, r7):
            res = []
            for i in range(length):
                rem_len = length - 1 - i
                for d in range(1, 10):
                    nr2 = r2 - f2[d]
                    nr3 = r3 - f3[d]
                    nr5 = r5 - f5[d]
                    nr7 = r7 - f7[d]
                    if min_len(nr2, nr3, nr5, nr7) <= rem_len:
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        N = len(num)

        # Precalculate prefix factor counts up to the first '0'
        prefix_factors = [(0, 0, 0, 0)]
        zero_idx = N
        for idx, ch in enumerate(num):
            if ch == "0":
                zero_idx = idx
                break
            p2, p3, p5, p7 = prefix_factors[-1]
            d = int(ch)
            prefix_factors.append(
                (p2 + f2[d], p3 + f3[d], p5 + f5[d], p7 + f7[d])
            )

        # Attempt to keep a prefix of length i (from min(N, zero_idx) down to 0)
        for i in range(min(N, zero_idx), -1, -1):
            p2, p3, p5, p7 = prefix_factors[i]
            rem_c2 = c2 - p2
            rem_c3 = c3 - p3
            rem_c5 = c5 - p5
            rem_c7 = c7 - p7

            # Case: num itself has no zeroes and is already divisible by t
            if i == N:
                if min_len(rem_c2, rem_c3, rem_c5, rem_c7) == 0:
                    return num
                continue

            # Try replacing digit num[i] with a larger digit d > num[i]
            start_digit = int(num[i]) + 1
            for d in range(start_digit, 10):
                nr2 = rem_c2 - f2[d]
                nr3 = rem_c3 - f3[d]
                nr5 = rem_c5 - f5[d]
                nr7 = rem_c7 - f7[d]
                rem_len = N - 1 - i
                if min_len(nr2, nr3, nr5, nr7) <= rem_len:
                    prefix_str = num[:i] + str(d)
                    suffix_str = fill_smallest(rem_len, nr2, nr3, nr5, nr7)
                    return prefix_str + suffix_str

        # If length N cannot accommodate the required product, expand to length > N
        req_len = min_len(c2, c3, c5, c7)
        target_len = max(N + 1, req_len)
        return fill_smallest(target_len, c2, c3, c5, c7)