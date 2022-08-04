from jwst.stpipe import Step
from jwst import datamodels

pxdq_flags = {"DO_NOT_USE": 1, "SATURATED": 2, "JUMP_DET": 4}


class KPIBadpixStep(Step):
    """Fix bad pixels.

    References for the KI method:
        https://ui.adsabs.harvard.edu/abs/2019MNRAS.486..639K/abstract
        https://ui.adsabs.harvard.edu/abs/2013MNRAS.433.1718I/abstract
    """

    # TODO: Test the default list, could not find an example in pipeline
    spec = """
        plot = boolean(default=True)
        bad_bits = string_list(default=['DO_NOT_USE'])
        method = string(default='medfilt')
    """

    bad_bits_allowed = pxdq_flags.keys()
    methods_allowed = ['medfilt', 'KI']

    def process(self, input):
        """
        Fixes bad pixels in KP data

        Parameters
        ----------
        input: string
            input file name

        Returns
        -------
        result:
            Image to which the bad pixel correction has been applied
        """
        raise NotImplementedError("Bad pixel correction step not implemented yet.")
