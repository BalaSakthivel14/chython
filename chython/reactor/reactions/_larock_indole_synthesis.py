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
    'name': 'Larock indole synthesis',
    'description': 'Aromatic Aldehyde, Aromiatic primary amine and 2-naphthol or 8-hydroxyquinoline to produce an α-aminobenzylphenol',
    'templates': [
        {
            'A': [
                # Iodoaniline 
                '[I;D1:1][C;a:2]:[C;a:3][N;D1,D2;z1:4]'
            ],
            'B': [
                # C#C
                '[C;D2;z3:5]#[C;D2;z3:6]'
            ],
            'product': '[A:2]1[A:3][A:4][A:5]=[A:6]1',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:4]',
                'B': '[A:5][A:6]'
            }
        }
    ],
    'alerts': ['[N;D2;x1;z1][Cl,Br,I;D1]']
}
