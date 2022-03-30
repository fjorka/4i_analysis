# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:25:37 2021

@author: Katarzyna Kedziora
"""

import numpy as np

from skimage.morphology import dilation
from skimage.morphology import disk

def make_rings(image,width = 5,gap = 0):
    
    '''
    This function creates rings but excludes regions that could belong to more than one object.
    
    input:
    image - image of labels
    width - width of the ring
    gap - how many pixels between the object and its ring
    
    output:
    rings - image of the rings (labels preserved)
    '''
    
    selem = disk(width)

    eroded = dilation(image, selem)

    rings = eroded.copy()
    rings[rings==image]=0
    
    # do the same but in oposite direction 
    image_rev = (np.max(image) + 1) - image
    image_rev[image_rev == (np.max(image) + 1)] = 0
    
    eroded = dilation(image_rev, selem)
    eroded = (np.max(image) + 1) - eroded
    eroded[eroded == (np.max(eroded) + 1)] = 0
    
    # combine
    rings[rings!=eroded] = 0
    
    eroded_gap = dilation(image,disk(gap))
    rings[eroded_gap>0]=0
    
    return rings