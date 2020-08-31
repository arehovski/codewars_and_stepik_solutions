"""
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of
appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""


def sum_pairs(ints, s):
    checked = []

    def inner(ints, s):
        for i in range(len(ints) - 1):
            if ints[i] in checked:
                continue
            if not (s - ints[i]) in ints[i + 1:]:
                checked.append(ints[i])
                continue
            else:
                index = ints.index(s - ints[i], i + 1)
                possible_sum = inner(ints[i + 1:index], s)
                if possible_sum:
                    return possible_sum
                return [ints[i], ints[index]]
    return inner(ints, s)
