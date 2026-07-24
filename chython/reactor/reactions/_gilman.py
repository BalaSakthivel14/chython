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
    'name': 'Gilman Reaction',
    'description': 'α,β-unsaturated carbonyl, acid chlorides and epoxy compounds reaction with Gilman reagents to form C-C bonds',
    'templates': [
        # α, β-unsaturated carbonyl
        {
            'A': [
                # α,β-unsaturated ketones
                '[O;D1;x0;z2;M]=[C;D3;x1,x2;z2;M][C;D2;x0;z2:1]=[C;D1,D2;x0;z2:2]'
            ],
            'B':[
                # Gilman Reagent
                '[C;x1;z1,z2:3][Cu-:4].[Li+:5]',
                '[C;a:3][Cu-:4].[Li+:5]'
             ],
            'product': '[A:1][A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3]'
            }
        },
        # Acid chlorides
        {
            'A': [
                # Acid chloride-Alk
                '[Cl;D1:1][C;D3;x2;z2:2]([C;x0;z1;M])=[O;M]',
                # Acid chloride-Ar
                '[Cl;D1:1][C;D3;x2;z2:2]([C;a;M])=[O;M]',
            ],
            'B':[
                # Gilman Reagent
                '[C;x1;z1,z2:3][Cu-:4].[Li+:5]',
                '[C;a:3][Cu-:4].[Li+:5]'
             ],
            'product': '[A:2]-[A:3]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3]'
            }
        },
        # Epoxide
        {
            'A': [
                # Epoxide
                '[O;D2;z1;x0:1]1[C;z1;x1;r3:2][C;z1;x1;r3:3]1'
            ],
            'B':[
                # Gilman Reagent
                '[C;x1;z1,z2:4][Cu-:5].[Li+:6]',
                '[C;a:4][Cu-:5].[Li+:6]'
             ],
            'product': '[A:3]([A:1])[A:2]-[A:4]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3]'
            }
        }
    ],
    'alerts' : []
}
