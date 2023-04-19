#!/usr/bin/env python3

import re
def mail_correcto(string):
    return bool(re.search('^[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$',string)) #[.] o \.

print(mail_correcto("lujan.garrigo@gmail.com"))
print(mail_correcto("lujan-garrigo@gmail.com"))
print(mail_correcto("lujan_garrigo_@gmail.com"))

print(re.search('[a-z]',"hola")) #[.] o \.)