import snappy
from snappy import ProductIO, HashMap, GPF, jpy,ProgressMonitor
import os

JPY = snappy.jpy
imageIO = JPY.get_type('javax.imageio.ImageIO')
File = JPY.get_type('java.io.File')

def tiffCreation(file):
    product = ProductIO.readProduct(file)
    JPY = snappy.jpy
    imageIO = JPY.get_type('javax.imageio.ImageIO')
    File = JPY.get_type('java.io.File')
    intensityBands = ['Intensity_VH'] 
    for band in intensityBands:
        imgBand = product.getBand(band)
        image = imgBand.createColorIndexedImage(ProgressMonitor.NULL)
        name = File(band +'.tif')
        imageIO.write(image, 'tif', name)
        return ("Processed band:" + band) , name

def landMask(file):
    p = ProductIO.readProduct(file)
    
    HashMap = jpy.get_type('java.util.HashMap')
    params = HashMap()

    band = 'Intensity_VH'
    params.put('sourceBands',band)
    params.put('landMask', False)
    land_sea_mask_product = GPF.createProduct('Land-Sea-Mask', params, p) 

    imgBand = land_sea_mask_product.getBand(band)
    image = imgBand.createColorIndexedImage(ProgressMonitor.NULL)
    name = File('landMask.tif')
    imageIO.write(image, 'tif', name)
    
    return ("Processed band:" + str(name)) , str(name)

def seaMask(file):
    p = ProductIO.readProduct(file)
    
    HashMap = jpy.get_type('java.util.HashMap')
    params = HashMap()

    band = 'Intensity_VH'
    params.put('sourceBands',band)
    params.put('landMask', False)
    land_sea_mask_product = GPF.createProduct('Land-Sea-Mask', params, p) 

    params = HashMap()
    params.put('sourceBands','Intensity_VV')
    params.put('landMask', True)
    land_sea_mask_product = GPF.createProduct('Land-Sea-Mask', params, p)

    imgBand = land_sea_mask_product.getBand(band)
    image = imgBand.createColorIndexedImage(ProgressMonitor.NULL)
    name = File('seaMask.tif')
    imageIO.write(image, 'tif', name)
    return ("Processed band:" + str(name)), str(name)