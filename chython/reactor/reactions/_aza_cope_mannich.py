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
    'name' : 'Aza-Cope Mannich Reaction',
    'description': 'Converts an alkyne-tethered piperidine into fused tricyclic amines via 3-aza-Cope/Mannich cyclization',
    'templates' : [
        {
            'A': [
                # Alk#Alk-Alk-N
                '[C;x0,x1;z2:1]=[C;x1;z2:2]([O;M])[C;x1;z1:3][N;z1:4][C;x1;z1;M][C;x0;z1;M][C;z3:5]#[C;z3:6]',
                # Ar-N
                '[C;x0,x1;z2:1]=[C;x1;z2:2]([O;M])[C;x1;z1:3][N;z1:4][C;x1;z1;M][C;a;M]:[C;a;M][C;z3:5]#[C;z3:6]',
                # Alk#Alk-Alk-Alk-N
                '[C;x0,x1;z2:1]=[C;x1;z2:2]([O;M])[C;x1;z1:3][N;z1:4][C;z1;M][C;z1;M][C;z1;M][C;z3:5]#[C;z3:6]'
            ],
            'product': '[A:1]1=[A:2][A:3][A:5]([A:4])[A:6]1',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:6]'
            }
        }
    ],
    'alerts': []
}
