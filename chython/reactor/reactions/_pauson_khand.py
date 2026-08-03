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

smarts_A = ['[C;x0;z3:1]#[C;x0;z3:2][C;M]' + '[A;M]' * x + '[C;z1;M][C;z2:3]=[C;D1;z2;x0:4]' for x in range(1, 20)]
template = {
    'name': 'Pauson-Khand Reaction',
    'description': 'Intramolecular cycloaddition of an Alkyne,alkene, and carbon monoxide combine into a α,β-cyclopentenone',
    'templates': [
        {
            'A':  # Intramolcular Alkyne and alkene
                smarts_A,

            'B': [
                # C#O
                "[O+;D1:5]#[C-;D1:6]"
            ],
            'product': '[A:1]1=[A:2][A:3][A:4][A:6]1=[A:5]',
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2][A:3][A:4]',
                'B': '[A:5][A:6]'
            }
        }
    ],
    'alerts': []
}
