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
    'name': 'Schiff Base Thiazolidinone Synthesis',
    'description': 'Combining the amine, aldehyde and thioglycolic acid to 4-thiazolidinone derivatives',
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
                # S-C-COOH
                '[S;D1;x0;z1:4][C;D2;x1;z1:5][C;x2;z2:6](=[O;M])[O;D1:7]'
            ],
            'product': '[A:1]1[A:2][A:4][A:5][A:6]1',
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
