# standard library imports
import sys
import os
from os import path

# third party
import numpy as np
import cclib

# local application imports
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from .base_lot import Lot

# standard library imports
import sys
import os
from os import path

# third party
import numpy as np
import cclib

# local application imports
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from .base_lot import Lot

class Gaussian(Lot):

    def write_input_file(self, geom, multiplicity):

        if self.lot_inp_file is None:
            # Default Gaussian setting
            inpstring = '#N pm6 scf(xqc) NoSymmetry force\n'
        else:
            # Add header part of Gaussian
            inpstring = ''
            with open(self.lot_inp_file) as lot_inp:
                lot_inp_lines = lot_inp.readlines()
            for line in lot_inp_lines:
                inpstring += line
        # Write title
        inpstring += 'test\n\n'
        # Write chg multiplicity
        inpstring += f'{self.charge} {multiplicity}\n'
        # Write geometry
        for coord in geom:
            for i in coord:
                inpstring += str(i)+' '
            inpstring += '\n'
        inpstring += '\n'
        print (inpstring)
        # Use working directory
        tempfile_directory = os.path.join(self.working_directory,'force.com')
        tempfile = open(tempfile_directory,'w')
        tempfile.write(inpstring)
        tempfile.close()
        return tempfile_directory

    def run(self, geom, multiplicity, ad_idx, runtype='gradient'):

        # Write input file
        command = 'g09'
        filename = 'force'
        directory = self.write_input_file(geom, multiplicity)
        cmd = f'{command} {directory}'
        current_directory = os.getcwd()
        os.system(f'cd {self.working_directory}')
        os.system(cmd)
        os.system(f'cd {current_directory}')
        # parse output
        self.parse(multiplicity)
        print ('force calculation done')
        return

    def parse(self, multiplicity):
        file_directory = os.path.join(self.working_directory,'force.log')
        p = cclib.parser.Gaussian(file_directory)
        data = p.parse()
        energies = data.scfenergies # eV unit
        grads = data.grads
        coords = data.atomcoords
        energy = energies[0] * 0.036749326681 # eV -> Hartree
        gradient = -grads[0] # Hartree/Bohr
        print (energy)
        self._Energies[(multiplicity, 0)] = self.Energy(energy, 'Hartree')
        self._Gradients[(multiplicity, 0)] = self.Gradient(gradient, 'Hartree/Bohr')



