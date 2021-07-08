# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mfem(CMakePackage):
    """Free, lightweight, scalable C++ library for finite element methods."""

    tags = ['FEM', 'finite elements', 'high-order', 'AMR', 'HPC']

    homepage = 'http://www.mfem.org'
    git      = 'https://github.com/mfem/mfem.git'

    maintainers = ['v-dobrev', 'tzanio', 'acfisher',
                   'goxberry', 'markcmiller86', 'cwsmith']

    test_requires_compiler = True

    version('4.2.0',
            '4352a225b55948d2e73a5ee88cece0e88bdbe7ba6726a23d68b2736d3221a86d',
            url='https://bit.ly/mfem-4-2', extension='tar.gz',
            preferred=True)

    variant('mpi', default=True,
            description='Enable MPI parallelism')
    variant('metis', default=True,
            description='Enable METIS support')
    variant('pumi', default=False,
            description='Enable functionality based on PUMI')
    variant('examples', default=False,
            description='Build and install examples')

    conflicts('+pumi', when='~mpi')

    depends_on('mpi', when='+mpi')
    depends_on('hypre@2.10.0:2.13.99', when='@:3.3.99+mpi')
    depends_on('hypre@:2.20.0', when='@3.4:4.2.99+mpi')
    depends_on('hypre', when='@4.3.0:+mpi')

    depends_on('metis', when='+metis')

    depends_on('pumi@2.2.3:', when='@4.2.0:+pumi')
    depends_on('pumi', when='+pumi~shared')
    depends_on('pumi+shared', when='+pumi+shared')

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define_from_variant('MFEM_USE_MPI', 'mpi'),
            self.define_from_variant('MFEM_USE_METIS', 'metis'),
            self.define_from_variant('MFEM_USE_PUMI', 'pumi'),
            self.define_from_variant('MFEM_ENABLE_EXAMPLES', 'examples'),
            '-DSKIP_SIMMETRIX_VERSION_CHECK=%s' %
            ('ON' if '~simmodsuite_version_check' in spec else 'OFF')
        ]

        if ('+metis' in spec) and spec['metis'].satisfies('@5:'):
            args += ['-DMFEM_USE_METIS_5=YES']

        if '+pumi' in spec:
            args += ['-DPUMI_DIR=%s' % spec['pumi'].prefix]
        if '+hypre' in spec:
            args += ['-DHYPRE_DIR=%s' % spec['hypre'].prefix]
        if '+metis' in spec:
            args += ['-DMETIS_DIR=%s' % spec['metis'].prefix]

        return args
