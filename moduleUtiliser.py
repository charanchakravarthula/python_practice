# importing the entire module\

import module
print(module.summer(1,2))

# importing partcular func from a module
from module import subber
print(subber(3,2))

# using alias
import module as mad
print(mad.multiplr(3,6))

from package import mdlpckg
mdlpckg.executer()

from package.mdlpckg import executer
executer()

from package.subpackage.subpckgmdl import mdl
mdl()