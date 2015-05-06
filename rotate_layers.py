#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def rotate_layers(Image, Draw, pages, angle):
    layers = []
    count = 0
    if (pages == 0):
        layers = Image.layers
    elif (pages == 1):
        for layer in Image.layers:
            if (count % 2):
                layers.append(layer)
            count += 1
    elif (pages == 2):
        for layer in Image.layers:
            if not(count % 2):
                layers.append(layer)
            count += 1
        
    for layer in layers:
        pdb.plug_in_rotate(Image, layer, angle + 1, 0)

register(
    'python-rotate-layers',
    'Rotate layers',
    'Rotate layers in batch mode',
    'Maksim E. Kozlov <maksim.e.kozlov@gmail.com',
    'GPLv3',
    'May 2015',
    '<Image>/Filters/Batch/Rotate layers...',
    'RGB* GRAY*',
    [
        (PF_OPTION, 'pages', 'Pages', 0, ['All', 'Even', 'Odd']),
        (PF_OPTION, 'angle', 'Angle', 0, ['90', '180', '270']),
    ],
    [],
    rotate_layers
)

main()
