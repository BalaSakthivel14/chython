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
    'name': 'Robinson Annulation',
    'description': 'Cyclohexanone reaction with Methyl vinyl ketone to six membered α,β-unsaturated ketone',
    'templates': [
        {
            'A': [
                # Methyl vinyl ketone
                '[C;z2;x0:1]=[C;z2;x0:2][C;z2;x1;M](=[O;M])[C;z1;x0:3]'
            ],
            'B':[
                # Hexane 1,3 dione
                '[O;D1;x0;z2:4]=[C;D3;x1;z2;r4,r5,r6,r7,r8:5][C;D3;z1;x0:6]([C;z1;M])[C;z2;x1;M]=[O;M]',
                # Cyclohexanone
                '[O;D1;x0;z2:4]=[C;D3;x1;z2;r4,r5,r6,r7,r8:5]([C;D2;z1;x0;M])[C;D2,D3;z1;x0:6]',
                # Benzofuran
                '[O;D1;x0;z2:4]=[C;D3;x1;z2;r4,r5,r6,r7,r8:5]([C;a;M])[C;D3;z1:6]'
            ],
            'product': '[A:2][A:1]-[A:6][A:5]=[A:3]',
            'alerts': [],
            'ufe' : {
                'A': '[A:1][A:2][A:3]',
                'B': '[A:4][A:5][A:6]'
            }
        }
    ],
    'alerts': []
}
