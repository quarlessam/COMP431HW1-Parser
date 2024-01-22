#Jess Quarles (Onyen squarles)
#I pledge the UNC Honor Pledge

import sys
import re

def parse(x):
    print(x, end = "")
    y = x
    if not re.compile('^MAIL.*FROM:.*').match(y):
        raise UserWarning("mail-from-cmd")
    y = re.split(r'^MAIL',y)[1]
    y = whitespace(y)
    y = re.split(r'^FROM:', y)[1]
    y = nullspace(y)
    y = path(y)
    y = CRLF(y)
    print("Sender ok")

def whitespace(x):
    if not re.compile('^[ \t]+').match(x):
        raise UserWarning("whitespace")
    return re.split(r'^[ \t]+', x)[1]

def nullspace(x):
    if not re.compile('^[ \t]+').match(x):
        return x
    return re.split(r'^[ \t]+', x)[1]

def path(x):
    y = x
    if not re.compile('^<').match(y):
        raise UserWarning("path")
    y = re.split(r'^<', y)[1]
    y = mailbox(y)
    if not re.compile('^>').match(y):
        raise UserWarning("path")
    y = re.split(r'^>', y)[1]
    return y

def mailbox(x):
    y = x
    y = local_part(y)
    if not re.compile('^@').match(y):
        raise UserWarning("mailbox")
    y = re.split(r'^@', y)[1]
    y = domain(y)
    return y

def local_part(x):
    if not re.compile('^[^ \t<>()\[\]\\.,;:@\"]+').match(x):
        raise UserWarning("string")
    return re.split(r'^[^ \t<>()\[\]\\.,;:@\"]+', x)[1]

def domain(x):
    y = x
    y = element(y)
    while re.compile('^\.').match(y):
        y = re.split(r'^\.', y)[1]
        y = element(y)
    return y

def element(x):
    if not re.compile('^[a-zA-Z][a-zA-Z0-9]*').match(x):
        raise UserWarning("element")
    return re.split(r'^[a-zA-Z][a-zA-Z0-9]*', x)[1]

def CRLF(x):
    if not re.compile('^[ \t]*$').match(x):
        raise UserWarning("CRLF")
    return x

for line in sys.stdin:
    try: parse(line)
    except UserWarning as w:
        errorMsg = "ERROR -- " + w.args[0]
        print(errorMsg)
