# -*- coding: utf-8 -*-
# Procrustes is a collection of interpretive chemical tools for
# analyzing outputs of the quantum chemistry calculations.
#
# Copyright (C) 2017-2018 The Procrustes Development Team
#
# This file is part of Procrustes.
#
# Procrustes is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Procrustes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
"""Setup and Install Module."""


from distutils.core import setup


setup(
    name='procrustes',
    version='0.0',
    description='Procrustes Package.',
    url='',
    license='MIT',
    author='Ayers Group',
    author_email='',
    package_dir={'procrustes': 'procrustes'},
    packages=['procrustes', 'procrustes.hungarian', 'procrustes.procrustes',
              'procrustes.procrustes.test'],
    # test_suite='nose.collector',
    requires=['numpy', 'numpy', 'sphinx', 'scipy'],
)