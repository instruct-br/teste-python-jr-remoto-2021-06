https://docs.python.org/dev/library/unicodedata.html#module-unicodedata
https://www.python.org/dev/peps/pep-3131/#id12
https://www.python.org/dev/peps/pep-3131/
https://www.python.org/dev/peps/pep-0423/#use-a-single-name


rules for version identifie
https://www.python.org/dev/peps/pep-0440/#id24


https://www.python.org/dev/peps/pep-0440/#id81

import re
def is_canonical(version):
    return re.match(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

Regex I made 
https://regex101.com/r/5WLamu/1
"(\d.)*(a|b|c|post|!|\+|dev|\.)*\d"gm

https://docs.djangoproject.com/en/3.2/topics/security/


I decise use a MVC arqueiteture and I truste in Models departem of Data banck as crieat 
This API only acept projetc name usen regular character without banckspace because this
 name is pasd whti paramete in get requisiton 

STARTER_LIST = ["Lu", "Ll", "Lt", "Lm", "Lo", "Nl"]
CONTINUE_LIST = ["Mn", "Mc", "Nd", "Pc", "Lu", "Ll", "Lt", "Lm", "Lo", "Nl"]

Import unicodedata 
from unicodedata import category
if category(name[0]) in starter_list or name[0] == '_' :
    for letter in name[1:]:
        if category(letter) in not continue_list:
            reise XABLAU #TODO
"
The identifier syntax is <XID_Start> <XID_Continue>*.

The exact specification of what characters have the XID_Start or XID_Continue properties can be found in the DerivedCoreProperties file of the Unicode data in use by Python (4.1 at the time this PEP was written), see [6]. For reference, the construction rules for these sets are given below. The XID_* properties are derived from ID_Start/ID_Continue, which are derived themselves.

ID_Start is defined as all characters having one of the general categories uppercase letters (Lu), lowercase letters (Ll), titlecase letters (Lt), modifier letters (Lm), other letters (Lo), letter numbers (Nl), the underscore, and characters carrying the Other_ID_Start property. XID_Start then closes this set under normalization, by removing all characters whose NFKC normalization is not of the form ID_Start ID_Continue* anymore.

ID_Continue is defined as all characters in ID_Start, plus nonspacing marks (Mn), spacing combining marks (Mc), decimal number (Nd), connector punctuations (Pc), and characters carrying the Other_ID_Continue property. Again, XID_Continue closes this set under NFKC-normalization; it also adds U+00B7 to support Catalan.

All identifiers are converted into the normal form NFKC while parsing; comparison of identifiers is based on NFKC.

A non-normative HTML file listing all valid identifier characters for Unicode 4.1 can be found at http://www.dcl.hpi.uni-potsdam.de/home/loewis/table-3131.html.

"
"Lu", "Ll", "Lt", "Lm", "Lo", "Nl",
---START---
 uppercase letters (Lu), 
 lowercase letters (Ll), 
 titlecase letters (Lt), 
 modifier letters (Lm), 
 other letters (Lo), 
 letter numbers (Nl),
 the underscore, 
 and characters carrying the Other_ID_Start property.


"XID_Start then closes this set under normalization, by removing all characters whose NFKC normalization is not of the form ID_Start ID_Continue* anymore"

"Mn", "Mc", "Nd", "Pc", "Lu", "Ll", "Lt", "Lm", "Lo", "Nl",
 ---continue---
 plus nonspacing marks (Mn),
 spacing combining marks (Mc), 
 decimal number (Nd), 
 connector punctuations (Pc), 
 and characters carrying the Other_ID_Continue property. 

 Again, XID_Continue closes this set under NFKC-normalization; it also adds U+00B7 to support Catalan.
