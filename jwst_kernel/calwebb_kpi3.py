import logging

from jwst.stpipe import Pipeline

from .kpi import kpi_badpix_step

__all__ = ["KPI3Pipeline"]

# Define logging
log = logging.getLogger(__name__)
log.setlevel(logging.DEBUG)

# TODO: Fetch automatically. Can JWST Pipeline already do this?
# http://svo2.cab.inta-csic.es/theory/fps/
wave_nircam = {'F212N': 2.121193}  # micron
weff_nircam = {'F212N': 0.027427}  # micron
wave_niriss = {'F277W': 2.739519,
               'F380M': 3.826384,
               'F430M': 4.282976,
               'F480M': 4.813019}  # micron
weff_niriss = {'F277W': 0.644830,
               'F380M': 0.201962,
               'F430M': 0.203914,
               'F480M': 0.297379}  # micron

# https://jwst-reffiles.stsci.edu/source/data_quality.html
pxdq_flags = {'DO_NOT_USE': 1,
              'SATURATED': 2,
              'JUMP_DET': 4}
# https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-detector-overview
# https://jwst-docs.stsci.edu/jwst-near-infrared-imager-and-slitless-spectrograph/niriss-instrumentation/niriss-detector-overview
pscale = {'NIRCAM_SHORT': 31.,
          'NIRCAM_LONG': 63.,
          'NIRISS': 65.6}  # mas
# https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-detector-overview/nircam-detector-performance
# https://jwst-docs.stsci.edu/jwst-near-infrared-imager-and-slitless-spectrograph/niriss-instrumentation/niriss-detector-overview/niriss-detector-performance
gain = {'NIRCAM_SHORT': 2.05,
        'NIRCAM_LONG': 1.82,
        'NIRISS': 1.61}  # e-/ADU


# TODO: List included steps in docstring
class KPI3Pipeline(Pipeline):
    """
    JWST stage 3 pipeline for kernel-phase imaging.

    KPI3Pipeline: Apply all level-3 calibration steps to a level-2 kernel
    phase exposure.

    ..Notes:: AMI skips ipc, photom, and resample steps in stage 1 & 2
              pipelines. Kernel-phase should also skip these steps.
    """

    class_alias = "calwebb_kpi3"

    spec = """
    """

    # Define aliases to steps
    step_defs = {
        "fix_bad_pixels": kpi_badpix_step.KPIBadpixStep,
        "recenter_frames": None,
        "window_frames": None,
        "extract_kerphase": None,
        "empirical_uncertainties": None,
    }
