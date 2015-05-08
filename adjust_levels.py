#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def adjust_levels(Image, Draw, x, y, w, h, LowLevel, HighLevel, Gamma):

    maxWidth = w
    maxHeight = h

    pdb.gimp_image_select_rectangle(Image, CHANNEL_OP_ADD,
            x, y, maxWidth, maxHeight)

    for layer in Image.layers:
        if (layer.visible == True):
            pdb.gimp_levels(layer, HISTOGRAM_VALUE,
                    LowLevel, HighLevel, Gamma, 0, 255)

register(
    'python-adjust-levels',
    'Adjust levels',
    'Modify levels of layers in the selection',
    'Maksim E. Kozlov <maksim.e.kozlov@gmail.com',
    'GPLv3',
    'May 2015',
    '<Image>/Filters/Batch/Levels...',
    'RGB* GRAY*',
    [
        (PF_FLOAT, 'x', 'X', 0.0),
        (PF_FLOAT, 'y', 'Y', 0.0),
        (PF_FLOAT, 'w', 'Width', 1.0),
        (PF_FLOAT, 'h', 'Height:', 1.0),
        (PF_SPINNER, 'low-level', 'Lowest input', 0, (0, 255, 1)),
        (PF_SPINNER, 'high-level', 'Highest input', 255, (0, 255, 1)),
        (PF_SPINNER, 'gamma', 'Gamma', 1.0, (0.1, 10.0, 0.1)),
    ],
    [],
    adjust_levels,
)

main()
