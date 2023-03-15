#!/usr/bin/python3
def best_score(a_dictionary):
    x = 0
    result = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > x:
                result = k
                x = v
            return result
        else:
            return None
