import os
import numpy as np

def getCalibData(filename):
    '''Returns the calibration matrix and distortion coefficients from .npz file. Filename should be located in the current working directory.
    '''
	# Defines the path of the calibration file and the dictonary used
	calibration_path = os.path.join(os.getcwd(), filename)

	# Load calibration from file
	mtx = None
	dist = None
	with np.load(calibration_path) as X:
		mtx, dist = [X[i] for i in ('mtx', 'dist')]

	print("\nThe file used for the camera calibration :", calibration_path)

	return mtx, dist