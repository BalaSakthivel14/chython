# -*- coding: utf-8 -*-
#
#  Copyright 2022-2024 Ramil Nugmanov <nougmanoff@protonmail.com>
#  Copyright 2023 Timur Gimadiev <timur.gimadiev@gmail.com>
#  Copyright 2025 Balasubramaniyan Sakthivel <timur.gimadiev@gmail.com>
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
    'name' : 'Diels Alder Reaction',
    'description': 'Conjugated diene and a dienophile react to form the cyclohexene ring',
    'templates' : [
        #Alkene Template
        {
            'A':  [
                #Reactant A Dienes
                #C=C-C=C
                '[C;D1;x0;z2:3]=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D1,D2;x0,x1;z2:6]',
                #C=C-C(Het-atom)=C
                '[C;D1;x0;z2:3]=[C;D2;x0;z2:4][C;D3;x1;z2:5]=[C;D1;x0;z2:6]',
                #C=C-C(Alk)=C
                '[C;D1;x0;z2:3]=[C;D2;x0;z2:4][C;D3;x0;z2:5]=[C;D1;x0;z2:6]',
                #cyclopentadien
                '[C;D2;x0;z2:3]1=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2;x0;z2:6][C;z1;x0;M]1',
                #Furon
                '[C;D2,D3;x1;z2:3]1=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2,D3;x1,x2;z2:6][O;D2;x0;z1;M]1',
                #C=C(C)-C(C)=C
                '[C;D1;x0;z2:3]=[C;D3;x0;z2:4][C;D3;x0;z2:5]=[C;D1;x0;z2:6]',
                #Cyclohexa-1,3-diene,cyclohexa_1_3_dienol
                '[C;D2,D3;x0,x1;z2:3]=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2;x0;z2:6]',
                #bicyclohexane 1,1 diene,#vinylcyclohexene
                '[C;D2;x0;z2:3]=[C;D3;x0;z2:4][C;D2,D3;x0;z2:5]=[C;D1,D2;x0;z2:6]'
               
            ],
            'B':  [
                #C=C
                '[C;D1;x0;z2:1]=[C;D1;x0;z2:2]',
                #C=C-COOH
                '[C;D1;x0;z2:1]=[C;D2;x0;z2:2]',
                #C-C=C-C
                '[C;D2;x0;z2:1]=[C;D2;x0;z2:2]',
                #Het-C=C-Het
                '[C;D2;x1;z2:1]=[C;D2,D3;x1,x2;z2:2]'
            ],
          
            'product': '[A:1]1[A:2][A:3][A:4]=[A:5][A:6]1',   
            'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][A:6]'
            }
            },
            #Akyne Template
                {
            'A': [
                #Reactant A Dienes
                #C=C-C=C
                '[C;D1;x0;z2:3]=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D1,D2;x0,x1;z2:6]',
                #C=C-C(Het-atom)=C
                '[C;D1;x0;z2:3]=[C;D2;x0;z2:4][C;D3;x1;z2:5]=[C;D1;x0;z2:6]',
                #cyclopentadien
                '[C;D2;x0;z2:3]1=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2;x0;z2:6][C;z1;x0;M]1',
                #Furon
                '[C;D2,D3;x1;z2:3]1=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2,D3;x1,x2;z2:6][O;D2;x0;z1;M]1',
                #C=C(C)-C(C)=C
                '[C;D1;x0;z2:3]=[C;D3;x0;z2:4][C;D3;x0;z2:5]=[C;D1;x0;z2:6]',
                #Cyclohexa-1,3-diene,cyclohexa_1_3_dienol
                '[C;D2,D3;x0,x1;z2:3]=[C;D2;x0;z2:4][C;D2;x0;z2:5]=[C;D2;x0;z2:6]',
                #bicyclohexane 1,1 diene,#vinylcyclohexene
                '[C;D2;x0;z2:3]=[C;D3;x0;z2:4][C;D2,D3;x0;z2:5]=[C;D1,D2;x0;z2:6]'
              
            ],
            'B': [
                #CC#CC, dinitril 
                '[C;D2;x0;z3:1]#[C;D2;x0;z3:2]'
            ],
          'product': '[A:1]1=[A:2][A:3][A:4]=[A:5][A:6]1',
           'alerts': [],
            'ufe': {
                'A': '[A:1][A:2]',
                'B': '[A:3][A:6]'
            }
        }
    ],

    'alerts': []
}