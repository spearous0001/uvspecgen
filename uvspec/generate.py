# Generate UV-Vis spectra from Gaussian09 TDHF/TDDFT log files. 
# Copyright (C) 2013  Gaussian Toolkit
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""UV-Vis spectrum generation from Gaussian09 TDHF/TDDFT log files.

This program uses the uvspec Python module for generating UV-Vis spectra
from Gaussian09 TDHF/TDDFT log files.  Alternatively, the uvspec module can
be imported into your own programs for use of the AbsorptionSpectrum class.

"""
from uvspec.config import settings
from uvspec.spectrum import AbsorptionSpectrum, join_spectra


def main():
    if settings.join:
        spectrum = join_spectra(settings.logfile, settings.parameters)
    else:
        spectrum = AbsorptionSpectrum(settings.logfile[0],
                                      settings.parameters,
                                      settings.outfile)
    
    spectrum.create_outfile(settings.output, settings.nometa)
    
    if settings.plot:
        spectrum.plot_spectrum()
