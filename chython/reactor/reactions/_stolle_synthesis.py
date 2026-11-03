# -*- coding: utf-8 -*-
#
#  Copyright 2022-2024 Ramil Nugmanov <nougmanoff@protonmail.com>
#  Copyright 2023 Timur Gimadiev <timur.gimadiev@gmail.com>
#  Copyright 2025 Balasubramaniyan Sakthivel <sakthivelbala.s@gmail.com>
#  This file is part of chython.
#
#  chython is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#

template = {
    'name': 'Stolle synthesis',
    'description': 'Formation of oxidoles from anilines and oxalyl chloride',
    'templates': [
        {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a:2]:[C;D2;a:3]',
                # Alk-NH-Ar
                '[C;z1;x1;M][N;D2;x0;z1:1][C;a:2]:[C;D2;a:3]'
            ],
            'B': [
                # Cl-C-COCl
                '[Cl;D1;x0;z1:4][C;x1,x2;z1,z2:5][C;x2;z2:6](=[O;M])[Cl;D1:7]'
            ],
            'product': '[A:1]1[A:2][A:3]-[A:5][A:6]1',
            'alerts': [],
            'ufe': {
                'A': ['A:1'],
                'B': '[A:3][A:6]',
            }
        }
    ],
    'alerts': []
}
