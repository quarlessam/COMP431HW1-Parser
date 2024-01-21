#Jess Quarles (Onyen squarles)
#I pledge the UNC Honor Pledge

import sys
import re

def parse(x):

    print(x, end='')

    ws = "[ \t]+"
    ns = "[ \t]*"
    MAIL = "[Mm][Aa][Ii][Ll]"
    FROM = "[Ff][Rr][Oo][Mm]:"
    LOCAL = "[^ \t<>()\[\]\\.,;:@\"]+"
    DOMAIN = "([a-zA-Z][a-zA-Z0-9]*\.)*[a-zA-Z][a-zA-Z0-9]*"

    expression = "^" + MAIL
    if not re.compile(expression).match(x):
        return "ERROR -- mail-from-cmd"

    expression += ws
    if not re.compile(expression).match(x):
        return "ERROR -- whitespace"

    expression += FROM
    if not re.compile(expression).match(x):
        return "ERROR -- mail-from-cmd"

    expression += ns + "<"
    if not re.compile(expression).match(x):
        return "ERROR -- path"

    expression += LOCAL
    if not re.compile(expression).match(x):
        return "ERROR -- string"

    expression += "@"
    if not re.compile(expression).match(x):
        return "ERROR -- mailbox"

    expression += DOMAIN
    if not re.compile(expression).match(x):
        return "ERROR -- element"

    expression += ">"
    if not re.compile(expression).match(x):
        return "ERROR -- path"

    expression += ns + "$"
    if not re.compile(expression).match(x):
        return "ERROR -- CRLF"

    return "Sender ok"

for line in sys.stdin:
    print(parse(line))
