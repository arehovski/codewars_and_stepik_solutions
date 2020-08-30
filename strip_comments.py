"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


import re


def solution(string,markers):
    if not markers:
        return string
    markers_str = ''
    for marker in markers:
        markers_str += '\\' + marker
    pattern = fr"([{markers_str}].*?)(\n|$)"
    matched = re.findall(pattern, string)
    for match in matched:
        string = string.replace(' ' + match[0], '')
        string = string.replace(match[0], '')
    return string
