import os

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser

from mammos.schema_packages.ifw_schema import IFWData


class IFWParser(MatchingParser):
  def is_mainfile(
    self,
    filename: str,
    mime: str,
    buffer: bytes,
    decoded_buffer: str,
    compression: str = None,
  ):
    print(f'filename {filename}, mime {mime}, compression {compression}')

    if os.path.basename(filename) != "VSM_M(H).json":
      return False

    return True
  

  def parse(
      self,
      mainfile: str,
      archive: EntryArchive,
      logger=None,
      child_archives: dict[str, EntryArchive] = None,
    ) -> None:
      print(f'mainfile {mainfile}, archive {archive}, child_archives {child_archives}')
      logger.info('IFWParser called')

      baseDir = os.path.dirname(mainfile)
      idx = baseDir.rfind('raw/')
      if idx == -1:
        archiveBaseDir = baseDir
      else:
        archiveBaseDir = baseDir[idx + 4:]

      # data_dir_GS = baseDir + "/GS/"
      # archiveData_dir_GS = archiveBaseDir + "/GS/"
      # data_dir_MC = baseDir + "/MC"

      # xyz_dirs = [dirdir for dirdir in os.listdir(data_dir_GS) if len(dirdir) == 1]

      # print(f'data_dir_GS {data_dir_GS} data_dir_MC {data_dir_MC}'
      #        f' xyz_dirs {xyz_dirs} idx{idx}')

      # # Reading file into lines; all folders are equivalent according to 
      # # UU-colleagues, so we can use the first one
      # file_Name_Ms = archiveBaseDir + "/GS/" + f"{xyz_dirs[0]}/out_last"
      # print(f'file_Name_Ms {file_Name_Ms}')

      # fx = archiveData_dir_GS + "x/out_MF_x" if 'x' in xyz_dirs else None
      # fy = archiveData_dir_GS + "y/out_MF_y" if 'y' in xyz_dirs else None
      # fz = archiveData_dir_GS + "z/out_MF_z" if 'z' in xyz_dirs else None
      # fol = f"{archiveData_dir_GS}{xyz_dirs[0]}/out_last"

      # # entry = Cube(data_file=file)
      # groundState = GroundState(out_MF_x=fx,out_MF_y=fy,out_MF_z=fz)
      # # groundState.normalize(archive=archive,logger=logger)
      # entry = UUData(groundState=groundState,out_last_file=fol)
      
      
      MoH = f"{archiveBaseDir}/VSM_M(H).json"
      print(f'MoH {MoH}')

      entry = IFWData(M_of_H_file=MoH)
      
      archive.data = entry
