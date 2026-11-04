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
    'name': 'Yonemitsu Condensation',
    'description': 'Indole,  aldehyde, and 1,3-dicarbonyl to produce heterocyclic derivatives',
    'templates': [
        {
            'A': [
                # Indole
                '[N;h1;a;r5;M](:[C;D3;a;r6;M]):[C;a;r5;M]:[C;D2;a;r5:1]',
            ],
            'B': [
                # Ar-CHO
                '[C;a;M][C;D2;x1;z2:2]=[O:3]',
                # Alk-CHO
                '[C;x0;z1;M][C;D2;x1;z2:2]=[O:3]',
            ],
            'C': [
                # RCO-C-COOR
                '[O;M]=[C;x1;z2;M][C;D2;x0;z1:4][C;x2;z2;M](=[O;M])[O;x0;z1;M]',
                # RCOO-C-COOR
                '[O;x0;z1;M][C;x2;z2;M](=[O;M])[C;D2;x0;z1:4][C;x2;z2;M](=[O;M])[O;x0;z1;M]'
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
