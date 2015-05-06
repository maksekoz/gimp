#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import shutil
from subprocess import call
from gimpfu import *

def layers2pdf(Image, Draw, OutDir, OutFile, Type):
    outFullPath = OutDir + '/' + OutFile
    tmpDir = "/tmp/layers2pdf"

    if not os.path.exists(tmpDir): os.makedirs(tmpDir)

    if (Type == 0): 
        ext = '.pdf'
    elif (Type == 1): 
        ext = '.jpg'
    elif (Type == 2): 
        ext = '.png'
    else: 
        return

    convertOutArgs = [
        '-colorspace', 'Gray',
        '-units', 'PixelsPerInch',
        '-density', '300x300',
        '-compress', 'Zip',
        '-alpha', 'off',
    ]

    for layer in Image.layers:
        fullpath = tmpDir + '/' + layer.name + ext
        filename = os.path.basename(fullpath)

        pdb.plug_in_unsharp_mask(Image, layer, 2.0, 0.50, 0)
    
        if (Type == 0):
            pdb.file_pdf_save(Image, layer, 
                fullpath, 
                filename, 
                True, False, False)
            continue
        elif (Type == 1):
            pdb.file_jpeg_save(Image, layer,
                    fullpath,
                    filename,
                    0.85, 0.01, 1, 1, '', 0, 1, 0, 1)
        elif (Type == 2):
            pdb.file_png_save2(Image, layer,
                    fullpath,
                    filename,
                    0, 9, 0, 0, 0, 1, 0, 0, 0)

        call(['convert'] + [fullpath] + convertOutArgs + [fullpath + '.pdf'])
        os.remove(fullpath)

    gs = ("gs " 
          "-dBATCH " 
          "-dNOPAUSE " 
          "-q " 
          "-sDEVICE=pdfwrite " 
          "-sOutputFile=" + outFullPath + " " +
          tmpDir + "/*.pdf"
         )
    call(gs, shell=True)

    shutil.rmtree(tmpDir)

register(
    'python-layers2pdf',
    'Layers-to-PDF',
    'Save layers as single PDF-file',
    'Maksim E. Kozlov <maksim.e.kozlov@gmail.com',
    'GPLv3',
    'May 2015',
    '<Image>/Filters/Batch/Layers to PDF...',
    'RGB* GRAY*',
    [
        (PF_DIRNAME, 'out-dir', 'Output directory', os.getcwd()),
        (PF_STRING, 'out-file', 'Output filename', "out.pdf"),
        (PF_OPTION, 'type', 'Images type', 0, ['None', 'JPEG', 'PNG']),
    ],
    [],
    layers2pdf
)

main()
