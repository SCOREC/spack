##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyPycparser(PythonPackage):
    """A complete parser of the C language, written in pure python."""
    homepage = "https://github.com/eliben/pycparser"
    url      = "https://pypi.io/packages/source/p/pycparser/pycparser-2.17.tar.gz"

    import_modules = ['pycparser', 'pycparser.ply']

    version('2.17', 'ca98dcb50bc1276f230118f6af5a40c7')
    version('2.13', 'e4fe1a2d341b22e25da0d22f034ef32f')

    depends_on('py-setuptools', type='build')
