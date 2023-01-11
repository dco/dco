#!/usr/bin/env python3

import sys 
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize([sys.argv[1]], 
    compiler_directives={'language_level' : "3"}),
    script_args=['build_ext', '-b', './build', '-t', './tmp']
 )
