# (c) Jimmy DeLano 2020
# Acadian Problem set

### ******************** helper functions ************************

def count(orig, find):
    """
    Given a String orig and a String find, count the number of times
    find appears in orig

	>>> count('', 'a')
	0

	>>> count('abcabc', 'a')
	2

	>>> count('abcabc','ab')
	2

    >>> count('abcabc', 'def')
    0

	"""
    assert len(find) > 0
    start = 0
    end = len(find)
    count = 0
    for _ in range(end, len(orig)+1):
        if orig[start:end] == find:
            count += 1
        start += 1
        end += 1
    return count

### *************************** part a ****************************

def swap(origStr, count, find, replace):
    """
    Swap count number of occurances of find with replace in origStr.
    If find is not in origStr, swap returns origStr.

	>>> swap('abcabc', 1, 'tom', 'cruise')
	'abcabc'
	>>> swap('abcabc', 1, 'a', 'd')
	'dbcabc'
    >>> swap('abcabc', 2, 'a', 'd')
    'dbcdbc'
    >>> swap('ABCabc', 2, 'A', 'X')
    'XBCabc'
	"""
    newStr = ''
    for i, chr in enumerate(origStr):
        if count == 0:
            newStr += origStr[i:]
            break
        else:
            if chr == find:
                newStr += replace
                count -= 1
            else:
                newStr += chr
    return newStr

def switcheroo1A(s, c1, c2):
    """
    this function solves question a (switcheroo1). switcheroo1A
    swaps occurrences of c1 in the first half of string s with
    occurrences of c2 in the second half of string s.

	>>> switcheroo1A('abcabc', 'tom', 'cruise')
	'abcabc'

	>>> switcheroo1A('deffabac','e','a')
	'daffabec'

    >>> switcheroo1A('', 'x', 'y')
    ''

	"""
    # count the number in first and second half
    # take the minimum
    # go through front and back and swap
    length = len(s)//2
    first = s[:length]
    second = s[length:]
    firstCount = count(first, c1)
    secondCount = count(second, c2)
    swaps = min(firstCount, secondCount)

    newFirst = swap(first, swaps, c1, c2)
    # need to iterate backwards, then flip it back around
    newSecond = swap(second[::-1], swaps, c2, c1)[::-1]

    return newFirst + newSecond

### *************************** part b ****************************

def swapStrings(origStr, count, find, replace):
    """
    This function is the same as swap but with swapStrings.
    If find isn't in origStr, it returns origStr

    >>> swapStrings('abccba', 1, 'cc', 'dd')
    'abddba'

    >>> swapStrings('abccba', 2, 'cc', 'dd')
    'abddba'

    >>> swapStrings('abccba', 2, 'a', 'XX')
    'XXbccbXX'

    >>> swapStrings('abccba', 1, 'bc', '')
    'acba'

    >>> swapStrings('abccba', 1, 'xx', 'dd')
    'abccba'

    >>> swapStrings('xxx', 0, 'abc', 'def')
    'xxx'
    """
    if (count == 0):
        return origStr

    newStr = ''
    start = 0
    end = len(find)
    for i in range(end, len(origStr)+1):
        if count == 0:
            newStr += origStr[end-1:]
            return newStr
        else:
            if origStr[start:end] == find:
                newStr += replace
                count -= 1
                if (count > 0):
                    start += len(find)
                    end += len(find)
                    continue
            else:
                if i == len(origStr):
                    newStr += origStr[start:]
                else:
                    newStr += origStr[start]
        start += 1
        end += 1
    return newStr

def switcheroo2B(s, s1, s2):
    """
    this is my iterative solution to question B
    switcheroo2 swaps occurrences of s1 in the first half of string
    s with occurrences of s2 in the second half of string s.

    >>> switcheroo2B('abcabdefff','ab','eff')
    'effcabdabf'

    >>> switcheroo2B('defffabcab','eff','ab')
    'dabfabceff'

    >>> switcheroo2B('xxxxxx', 'abc', 'def')
    'xxxxxx'

    >>> switcheroo2B('wowowowo', 'wo', 'ow')
    'owwowwoo'

    >>> switcheroo2B('qwerty', 'we', 'XX')
    'qwerty'
    """
    length = len(s)//2
    first = s[:length]
    second = s[length:]
    firstCount = count(first, s1)
    secondCount = count(second, s2)
    swaps = min(firstCount, secondCount)

    newFirst = swapStrings(first, swaps, s1, s2)
    # need to iterate backwards, then flip it back around
    newSecond = swapStrings(second[::-1], swaps, s2[::-1], s1[::-1])[::-1]
    return newFirst+newSecond


### *************************** part c ****************************

def switch1Helper(str, count, c1, c2):
    """
    Recursive helper function for part c. Continues to check
    first char in the string for matches and replaces if there is one

    >>> switch1Helper('abac', 2, 'a', 'X')
    'XbXc'

    >>> switch1Helper('xxxxx', 1, 'a', 'b')
    'xxxxx'

    >>> switch1Helper('xxYxx', 2, 'Y', 'x')
    'xxxxx'

    >>> switch1Helper('xxxxx', 7, 'x', 'a')
    'aaaaa'
    """
    if (count == 0) or len(str) < 1:
        return str
    if (str[0] == c1):
        return c2 + switch1Helper(str[1:], count-1, c1, c2)

    return str[0] + switch1Helper(str[1:], count, c1, c2)

def switcheroo1C(s, c1, c2):
    """
    This function calls switch1Helper to complete question C --
    the recursive solution to switcheroo1

    >>> switcheroo1C('abacdeff','a','e')
    'ebacdaff'

    >>> switcheroo1C('xxxxxx', 'tom', 'cruise')
    'xxxxxx'

    >>> switcheroo1C('qwerty', 'we', 'yt')
    'qwerty'

    >>> switcheroo1C('qwerty', 'wq', 'ty')
    'qwerty'
    """
    length = len(s)//2
    first = s[:length]
    second = s[length:]
    firstCount = count(first, c1)
    secondCount = count(second, c2)
    swaps = min(firstCount, secondCount)

    newFirst = switch1Helper(first, swaps, c1, c2)
    # need to iterate backwards, then flip it back around
    newSecond = switch1Helper(second[::-1], swaps, c2, c1)[::-1]

    return newFirst+newSecond

### *************************** part d ****************************

def switch2Helper(str, count, s1, s2):
    """
    Helper function that swaps strings recursively

    >>> switch2Helper('abcab', 1, 'ab', 'eff')
    'effcab'

    >>> switch2Helper('abcab', 4, 'ab', 'eff')
    'effceff'

    >>> switch2Helper('xxxxx', 2, 'ab', 'eff')
    'xxxxx'

    >>> switch2Helper('', 1, 'ab', 'eff')
    ''

    >>> switch2Helper('xxxxx', 0, 'x', 'abc')
    'xxxxx'

    """
    assert len(s1) > 0
    if (count == 0) or len(str) < 1:
        return str

    if (str[:len(s1)] == s1):
        return s2 + switch2Helper(str[len(s1):], count-1, s1, s2)

    return str[0] + switch2Helper(str[1:], count, s1, s2)

def switcheroo2D(s, s1, s2):
    """
    This is my solution for part D. This function calls switch2Helper
    Recursive solution for switcheroo2

    >>> switcheroo2D('abcabdefff', 'ab', 'eff')
    'effcabdabf'

    >>> switcheroo2D('', 'ab', 'eff')
    ''

    >>> switcheroo2D('abababcdcdcdcd', 'ab', 'cd')
    'cdcdcdcdababab'

    >>> switcheroo2D('ssss', 'Q', 'q')
    'ssss'
    """
    length = len(s)//2
    first = s[:length]
    second = s[length:]
    firstCount = count(first, s1)
    secondCount = count(second, s2)
    swaps = min(firstCount, secondCount)

    newFirst = switch2Helper(first, swaps, s1, s2)
    newSecond = switch2Helper(second[::-1], swaps, s2[::-1], s1[::-1])[::-1]

    return newFirst+newSecond


## set up doctests for functions
def test():
	from doctest import testmod
	testmod()

if __name__ == "__main__":
    test()
