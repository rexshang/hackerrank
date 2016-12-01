'''
Created on Nov 10, 2016

@author: erexsha
'''
# vim:fileencoding=utf8
from collections import defaultdict

# *** Aho Corasick automaton ***
# reference pages:
# http://en.wikipedia.org/wiki/Aho-Corasick_string_matching_algorithm
# http://d.hatena.ne.jp/naoya/20090405/aho_corasick
# http://www.ninxit.com/blog/2011/05/09/ahocorasick-python/

class AhoCorasick(object):
    class Node(object):
        def __init__(self):
            self.next = defaultdict(AhoCorasick.Node)
            self.terms = []
            self.failure = None

    def __init__(self):
        self.root = AhoCorasick.Node()

 #   def __init__(self, terms = []):
 #       self.root = AhoCorasick.Node()
 #       for term in terms:
 #           self.add_string(term)
 #       self.make_failure_links()

    def add_string(self, term = ""):
        cur_node = self.root
        for char in term:
            cur_node = cur_node.next[char]
        cur_node.terms.append(term)

    def make_failure_links(self):
        # DFS: depth-first search
        def _make(parent):
            for (char, child) in parent.next.items():
                child.failure = (parent.failure.next.get(char) or
                                 self.root.next.get(char) or
                                 self.root)
                if child.failure.terms:
                    child.terms.extend(child.failure.terms)
                _make(child)

        self.root.failure = self.root
        for node in self.root.next.values():
            node.failure = self.root
        for node in self.root.next.values():
            _make(node)

    def match(self, query):
        results = []
        node = self.root
        for i in xrange(len(query)):
            char = query[i]
            node = (node.next.get(char) or
                    node.failure.next.get(char) or
                    self.root)
            for term in node.terms:
                results.append((i + 1 - len(term), len(term)))
        return results

    def __repr__(self):
        output = []
        def _debug(output, char, node, depth=0):
            output.append('%s[%s]%s' % (' '*depth, char, node.terms))
            for (key, n) in node.next.items():
                _debug(output, key, n, depth+1)
        _debug(output, '', self.root)
        return '\n'.join(output)


if __name__ == '__main__':
    value = ['1']
    ac = AhoCorasick()
    ac.add_string('1')
    
    for i in range (0, 21):
        carry = 0
        for j in reversed(range(len(value))):
            doub = int(value[j]) * 2 + carry
            carry = doub / 10
            doub = doub % 10
            value[j] = str(doub)
        else:
            if carry > 0:
                value.insert(0, str(carry))
        string = ''.join(value)
        ac.add_string(string)
#        ac.make_failure_links()
    ac.make_failure_links()
    print ac
    tc = int(raw_input().strip())
    for iter in range(tc):
        val = raw_input().strip()
        print ac.match(val)
        print len(ac.match(val))
