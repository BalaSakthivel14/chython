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
    'name': 'Staudinger Cycloaddition',
    'description': 'Combining the amine, aldehyde and chloroacetyl chloride to 2-azetidinone derivatives',
    'templates': [
        {
            'A': [
                # Ar-NH2
                '[N;D1;x0;z1:1][C;a;M]',
                # Alk-NH2
                '[N;D1;x0;z1:1][C;x1;z1;M]'
            ],
            'B': [
                # R-CHO
                '[C;a;M][C;D2;x1;z2:2]=[O;D1:3]'
            ],
            'C': [
                # Cl-C-COCl
                '[Cl;D1;x0;z1;M][C;D2;x1;z1:4][C;x2;z2:5](=[O;M])[Cl;D1:6]'
            ],
            'product': '[A:1]1[A:2][A:4][A:5]1',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:2][A:3]',
                'C': 7
            }
        }
    ],
    'alerts': []
}
