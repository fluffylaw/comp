# Author of this file: Lydia Wang!

def sortcat(n, *arg):
    alist = []
    s = ''
    mostCommonCharacter = 0
    argc = len(arg)

    for j in range(0, n):
        longest = 0
        longest_index = 0
        for i in range(0, len(arg)):
            if i not in alist:
                k = len(arg[i])
                if longest < k:
                    longest = k
                    longest_index = i

        s += arg[longest_index]
        alist += [longest_index]
        
    print(s)


sortcat(2, 'abc', 'df', 'x')
