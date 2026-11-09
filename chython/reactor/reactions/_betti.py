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
    'name': 'Betti reaction',
    'description': 'Aromatic Aldehyde, Aromiatic primary amine and 2-naphthol or 8-hydroxyquinoline to produce an α-aminobenzylphenol',
    'templates': [
        {
            'A': [
                # 2_Naphthol
                '[O;D1;M][C;a;M]:[C;D2;a:1]:[C;D3;a;r6;M](:[C;a;r6;M]):[C;D3;a;r6;M](:[C;a;r6;M]):[C;a;r6;M]',
                # 8_hydroxy_quinoline
                '[C;D2;a:1]:[C;a;M]([O;D1;M]):[C;D3;a;r6;M](:[N;a;r6;M]):[C;D3;a;r6;M](:[C;a;r6;M]):[C;a;r6;M]'
            ],
            'B': [
                # Ar-CHO
                '[C;a;M][C;D2;x1;z2:2]=[O:3]'
            ],
            'C': [
                # Ar-NH2
                '[N;D1;x0;z1:4][C;a;M]'
            ],
            'product': '[A:1][A:2][A:4]',
            'alerts': [],
            'ufe': {
                'A': 1,
                'B': '[A:2][A:3]',
                'C': 4
            }
        }
    ],
    'alerts': []
}
