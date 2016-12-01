'''
Created on Nov 10, 2016

@author: erexsha
'''
FAIL = -1

transitions = {}
outputs = {}
fails = {}
    
def aho_corasick():
    global transitions
    global outputs
    global fails

    new_state = 0


    value = ['1']
    values = []
    values.append('1')
    
    for i in range (0, 801):
        carry = 0
        for j in reversed(range(len(value))):
            doub = int(value[j]) * 2 + carry
            carry = doub / 10
            doub = doub % 10
            value[j] = str(doub)
        else:
            if carry > 0:
                value.insert(0, str(carry))
        #print value
        values.append(''.join(value))
    

    for keyword in values:
        state = 0

        for j, char in enumerate(keyword):
            res = transitions.get((state, char), FAIL)
            if res == FAIL:
                break
            state = res

        for char in keyword[j:]:
            new_state += 1
            transitions[(state, char)] = new_state
            state = new_state

        outputs[state] = [keyword]

    queue = []
    for (from_state, char), to_state in transitions.items():
        if from_state == 0 and to_state != 0:
            queue.append(to_state)
            fails[to_state] = 0

    while queue:
        r = queue.pop(0)
        for (from_state, char), to_state in transitions.items():
            if from_state == r:
                queue.append(to_state)
                state = fails[from_state]

                while True:
                    res = transitions.get((state, char), state and FAIL)
                    if res != FAIL:
                        break
                    state = fails[state]

                failure = transitions.get((state, char), state and FAIL)
                fails[to_state] = failure
                outputs.setdefault(to_state, []).extend(
                    outputs.get(failure, []))
                
def match(string):
    global transitions
    global outputs
    global fails

    state = 0
    results = []
    for i, char in enumerate(string):
        while True:
            res = transitions.get((state, char), state and FAIL)
            if res != FAIL:
                state = res
                break
            state = fails[state]

        for match in outputs.get(state, ()):
            pos = i - len(match) + 1
            results.append((pos, match))

    return results

aho_corasick()
print match("24256")