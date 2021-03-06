#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3.4
"""
#############################################################################
# CX_FREEZE
"""
Icone sous Windows: il faut:
=> un xxx.ico pour integration dans le exe, avec "icon=xxx.ico"
=> un xxx.png pour integration avec PyQt4 + demander la recopie avec includefiles.
"""

import sys, os
from cx_Freeze import setup, Executable

#############################################################################
# preparation des options

# chemins de recherche des modules
# ajouter d'autres chemins (absolus) si necessaire: sys.path + ["chemin1", "chemin2"]
path = sys.path

# options d'inclusion/exclusion des modules
includes = ["Download"]  # nommer les modules non trouves par cx_freeze
excludes = []
packages = []  # nommer les packages utilises

# copier les fichiers non-Python et/ou repertoires et leur contenu:
includefiles = []

if sys.platform == "win32":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Windows
elif sys.platform == "linux2":
    pass
    # includefiles += [...] : ajouter les recopies specifiques à Linux
else:
    pass
    # includefiles += [...] : cas du Mac OSX non traite ici

# pour que les bibliotheques binaires de /usr/lib soient recopiees aussi sous Linux
binpathincludes = []
if sys.platform == "linux2":
    binpathincludes += ["/usr/lib"]

# niveau d'optimisation pour la compilation en bytecodes
optimize = 0

# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = True

# construction du dictionnaire des options
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": includefiles,
           "bin_path_includes": binpathincludes,


           "optimize": optimize,
           "silent": silent
           }

# pour inclure sous Windows les dll system de Windows necessaires
if sys.platform == "win32":
    options["include_msvcr"] = True

#############################################################################
# preparation des cibles
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
    # base = "Console" # pour application en console sous Windows

icone = None
if sys.platform == "win32":
    icone = "icone.ico"

cible_1 = Executable(
    script="musicasDL.py",
    base=base,

    )


#############################################################################
# creation du setup
setup(
    name="Musicas",
    version="0.0.1",
    description="Download musique in youtube",
    author="E524",
    options={"build_exe": options},
    executables=[cible_1]
    )

    """
#############################################################################
# CYTHON

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Download
import gi

extensions = [
    Extension("musicasDL", ["musicasDL.py"],
        include_dirs = [],
        libraries = [],
        library_dirs = ["/usr/lib/python3.4"]),

    Extension("Download", ["Download.py"],
        include_dirs = [],
        libraries = [],
        library_dirs = ["/usr/lib/python3.4"]),

]





setup(
    name = "musicasDL",
    ext_modules = cythonize(extensions),
)
