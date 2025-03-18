# open what is needed to open fits files
from astropy.io import fits

import numpy as np  
#importare un modulo in un altro modulo
#import logger
from ..helpers.logger import Logger

class FitsManager:
    """"
    A class to manage fits files, using astropy.io.fits module
    """
    #define the constructor
    def __init__(self,input_file):
        """"
        Constructor of the class, it will open the fits file and store it in the object
        """
        #variabili 
        self.input_file = input_file
        self.hdulist = fits.open(input_file)
    #creare logger   
        self.logger = Logger("FitsManager")
        self.logger("Fits file opened: ")   

    def get_header(self, hdu_index):
        """
        Get the header of the fits file
        """
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            self.logger.error("Invalid HDU index",ValueError)
            raise ValueError("Invalid HDU index")
        return self.hdulist[hdu_index].header
    def get_data(self, hdu_index):
        """
        Get the data of the fits file
        """
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            self.logger.error("Invalid HDU index",ValueError)
            raise ValueError("Invalid HDU index")
        return self.hdulist[hdu_index].data
    def get_hdu_count(self):
        """
        Get the number of HDU in the fits file
        """
      
        return len(self.hdulist)