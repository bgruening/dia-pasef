#!/usr/bin/env python
from __future__ import print_function

def setCompressionOptions(opt, accuracy=-1)
    """
    Adds suitable compression options for an object of type
    pyopenms.PeakFileOptions
        - compresses mass / time arrays with numpress linear
        - compresses intensity with slof (log integer)
        - compresses ion mobility with slof (log integer)
    """

    # Mass / time
    cfg = pyopenms.NumpressConfig()
    cfg.estimate_fixed_point = True
    cfg.numpressErrorTolerance = -1.0 # skip check, faster
    cfg.setCompression(b"linear");
    cfg.linear_fp_mass_acc = accuracy; # set the desired m/z or RT accuracy
    opt.setNumpressConfigurationMassTime(cfg)

    # Intensity
    cfg = pyopenms.NumpressConfig()
    cfg.estimate_fixed_point = True
    cfg.numpressErrorTolerance = -1.0 # skip check, faster
    cfg.setCompression(b"slof");
    opt.setNumpressConfigurationIntensity(cfg)
    opt.setCompression(True) # zlib compression

    # Now also try to compress float data arrays (this is not enabled in all
    # versions of pyOpenMS).
    try:
        cfg = pyopenms.NumpressConfig()
        cfg.estimate_fixed_point = True
        cfg.numpressErrorTolerance = -1.0 # skip check, faster
        cfg.setCompression(b"slof");
        opt.setNumpressConfigurationFloatDataArray(cfg)
    except Exception:
        pass
