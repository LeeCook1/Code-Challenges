def stringify_list(arr):
    start, out = 0, []
    stop_indexes = [idx for idx, val in enumerate(arr) \
            if idx < len(arr) - 1 and val+1 != arr[idx +1]] + [len(arr)-1]
    for stop_ind in stop_indexes:
        range_str = str(arr[start]) 
        range_str += '-%s'%str(arr[stop_ind]) if start != stop_ind else ''
        out.append(range_str)
        start = stop_ind+1
    print(','.join(out))

def repeats(arr):
    tracker, exist = {}, set()
    for a in arr:
        exist |= {a} if a in tracker else set() 
        tracker[a] = None
    return sum(set(arr) - exist)

def test_repeats():
    tests = [ 
            ([4,5,7,5,4,8], 15),
            ([9,10,19,13,19,13],19),
            ([16,0,11,4,8,16,0,11],12),
            ([5,17, 18, 11, 13, 18, 11, 13],22),
            ([5,10,19,13,10,13],24)]

    _assert_test(tests, repeats)
    
def capitalize(string):
    even_altered = "".join([ s.upper() if i % 2 == 0 else s 
            for i,s in enumerate(string)])
    return [even_altered, even_altered.swapcase()]

def test_capitalize():
    tests = [
            ("abcdef", ['AbCdEf', 'aBcDeF']),
            ("codewars", ['CoDeWaRs', 'cOdEwArS']),
            ("abracadabra", ['AbRaCaDaBrA', 'aBrAcAdAbRa'])]

    _assert_test(tests, capitalize)

def isPrime(num):
    from math import sqrt
    return num >=2 and not [n for n in  range(2, int(sqrt(num))) if num % n == 0]

def maxMultiple(divisor, bound):
    for n in range(bound,0,-1):
        if n % divisor == 0:
            return n
    return max([n for n in range(bound, 0, -1) if n % divisor == 0])

def test_maxMultiple():
    tests = [
            ((2,7),6),
            ((3,10),9),
            ((7,17),14),
            ((10,50),50),
            ((37,200),185),
            ((7,100),98)]
    
    _assert_test(tests, maxMultiple)

def _assert_test(input_expect_arr, func):
    for test_input, expected in input_expect_arr:
        print(test_input,expected, func(*test_input))
        assert func(*test_input) == expected

def main():
    #test_maxMultiple()
    stringify_list([8, 11,12,13,14,15, 25,72,88])
if __name__ == '__main__':
    main()
