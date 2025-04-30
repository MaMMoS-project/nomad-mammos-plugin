from typing import (
  TYPE_CHECKING,
)

import json

from nomad.datamodel.data import (
  ArchiveSection,
  EntryData,
)
from nomad.metainfo import (
  Package,
  Quantity,
  Section,
  SubSection,
)
from nomad.units import ureg

from .mammos_ontology import MagnetocrystallineAnisotropyConstantK1, SpontaneousMagneticPolarisation, MaximumEnergyProduct

if TYPE_CHECKING:
  from nomad.datamodel.datamodel import (
      EntryArchive,
  )
  from structlog.stdlib import (
      BoundLogger,
  )

m_package = Package(name='Schema for IFW data')
m_package.__init_metainfo__()



class IFWData(EntryData, ArchiveSection):
  m_def = Section()

  BHmax = SubSection(
    section_def=MaximumEnergyProduct,
    repeats = False,
  )


  M_of_H_file = Quantity(
    type=str,
    description='The \'VSM_M(H)\' file.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )

  def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
    '''
    The normalizer for the `IFW data`.

    Args:
        archive (EntryArchive): The archive containing the section that is being
        normalized.
        logger (BoundLogger): A structlog logger.
    '''
    super().normalize(archive, logger)

    if self.M_of_H_file is not None:
        print(f'Normalizing IFW data: {self.M_of_H_file}')
        #print(f'archive.m_context.raw_file(self.M_of_H_file):  {archive.m_context.raw_file(self.M_of_H_file)}')
        with archive.m_context.raw_file(self.M_of_H_file) as file:
            print(f'file: {file}')  
            #print(f'file.read(): {file.read()}')  
            content = json.load(file)
            # content = json.loads(file.read())
            
        self.BHmax = MaximumEnergyProduct()
        self.BHmax.MaximumEnergyProduct = \
            ureg.Quantity(float(content['BHmax in kJ/m^3'][0]), 'kJ/m^3')
