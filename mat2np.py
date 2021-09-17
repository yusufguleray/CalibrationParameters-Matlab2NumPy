import scipy.io as sio
import numpy as np
import sys, os

def mat2np(path2mat, filename):

    matlab_file = sio.loadmat(path2mat)

    for k, v in matlab_file.items():
        if isinstance(v, np.ndarray):
            key = k
            break

    struct = matlab_file[key]
    mtx = struct['IntrinsicMatrix'][0][0].T
    dist = struct['RadialDistortion'][0][0].squeeze()
    if dist.shape[0] != 3 : raise IndexError('Number of radial distortion parameters are not 3. Make sure 3 parameters are used for Radial Distortion in MATLAB.')
    dist = np.append(dist, struct['TangentialDistortion'][0][0].squeeze())
    print('Calibration matrix =\n', mtx, '\nDistortion Coefficients (OpenCV style) :\n', dist)

    np.savez_compressed(filename, mtx=mtx, dist=dist)

if __name__ == "__main__":

    try: path2mat = sys.argv[1]
    except IndexError: path2mat = input('\nPlease enter the name of the .mat file that contains camera parameters:\n') 
    path2mat = os.path.join(os.getcwd(), path2mat)

    try: filename = sys.argv[2]
    except IndexError: filename = input('\nWhat should be the name of the numpy file to be save?\n') 
    filename = os.path.join(os.getcwd(), filename)

    mat2np(path2mat, filename)