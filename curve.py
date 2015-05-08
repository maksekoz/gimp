#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def apply_curve(Image, Draw, inCurve):
    curve = map(int, inCurve.split(','))
    for layer in Image.layers:
        if (layer.visible == True):
            pdb.gimp_curves_spline(layer, HISTOGRAM_VALUE,
                    len(curve), curve)


register(
    'python-curve',
    'Apply curve',
    'Apply curve of layers',
    'Maksim E. Kozlov <maksim.e.kozlov@gmail.com',
    'GPLv3',
    'May 2015',
    '<Image>/Filters/Batch/Curve...',
    'RGB* GRAY*',
    [
        (PF_STRING, "curve", "Curve: x0, y0, x1, y1, ...", "0, 0, 255, 255"),
    ],
    [],
    apply_curve,
)

main()
