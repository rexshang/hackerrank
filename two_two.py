'''
Created on Nov 8, 2016

@author: erexsha
'''
import sys

_end = '_end_'
root = dict()

def make_trie(word):
    current_dict = root
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end

def in_trie(word):
    current_dict = root
    #  there could be multiple matches, return all matches
    match = 0
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
            if _end in current_dict:
                match = match + 1
        else:
            break
   
    return match

def build_power_trie():
    value = ['1']
    make_trie(value)
    length = 1
    for i in range (0, 10):
        carry = 0
        for j in reversed(range(length)):
            doub = int(value[j]) * 2 + carry
            carry = doub / 10
            doub = doub % 10
            value[j] = str(doub)
        else:
            if carry > 0:
                value.insert(0, str(carry))
                length = length + 1
        #print value
        make_trie(value)
    print root
        
def count_two_two(val):
        count = 0
        length = len(val)
        for i in range(length):
            word = val[i:length]
            count = count + in_trie(word)
        else:
            return count

def myMain():        
    build_power_trie()
    
    tc = int(raw_input().strip())
    for iter in range(tc):
        val = raw_input().strip()
        print count_two_two(val)
        
#cProfile.run('myMain()')
myMain()