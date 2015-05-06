#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def adjust_layers(Image, Draw, LowLevel, HighLevel, Gamma):

    maxWidth = 0
    maxHeight = 0
    
    for layer in Image.layers:
        curWidth = pdb.gimp_drawable_width(layer)
        curHeight = pdb.gimp_drawable_height(layer)
        if (maxWidth < curWidth):
            maxWidth = curWidth
        if (maxHeight < curHeight):
            maxHeight = curHeight

    for layer in Image.layers:
        if (layer.visible == True):
            pdb.gimp_levels(layer, HISTOGRAM_VALUE, 
                    LowLevel, HighLevel, Gamma, 0, 255 )
        pdb.gimp_layer_resize(layer, maxWidth, maxHeight, 0, 0)
        pdb.gimp_layer_flatten(layer)

register(
    'python-adjust-layers',
    'Adjust layers',
    'Adjust layers in batch mode',
    'Maksim E. Kozlov <maksim.e.kozlov@gmail.com',
    'GPLv3',
    'May 2015',
    '<Image>/Filters/Batch/Adjust layers...',
    'RGB* GRAY*',
    [
        (PF_SPINNER, 'low-level', 'Lowest input', 0, (0, 255, 1)),
        (PF_SPINNER, 'high-level', 'Highest input', 255, (0, 255, 1)),
        (PF_SPINNER, 'gamma', 'Gamma', 1.0, (0.1, 10.0, 0.1)),
    ],
    [],
    adjust_layers
)

main()
