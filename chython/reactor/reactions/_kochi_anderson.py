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
    'name': 'Kochi–Anderson Reaction',
    'description' : 'C–H alkylation of quinones via radical decarboxylation of carboxylic acids',
    'templates' : [
        {
            'A':  [
                # Quinones
                '[O;M]=[C;D3;z2;x1;r6;M][C;D2;z2;x0;r6:1]=[C;D3;z2;x0;r6;M][C;D3;z2;x1;r6;M]=[O;M]'
            ],
            'B':  [
                # Alk-C(=O)O
                '[C;z1;x0,x1:2][C;x2;z2:3]([O;D1;x0;z1:4])=[O:5]'
            ],
            'product': '[A:1]-[A:2]',
            'alerts' : [],
                'ufe' : {
                    'A': 1,
                    'B': '[A:3]'
                }
            }
        ],
        'alerts' : []
}
