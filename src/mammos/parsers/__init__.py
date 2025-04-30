from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        # from cube.parsers.cubeparser import CubeParser
        from mammos.parsers.cubeparser import CubeParser

        return CubeParser(**self.dict())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re='.*dat',
)


class UUParserEntryPoint(ParserEntryPoint):
  def load(self):
    from mammos.parsers.uuparser import UUParser

    return UUParser(**self.dict())


uuparser_entry_point = UUParserEntryPoint(
  name='UUParser',
  description='New parser entry point configuration.',
  mainfile_name_re='.*cif',
)


class IFWParserEntryPoint(ParserEntryPoint):
  def load(self):
    from cube.parsers.ifwparser import IFWParser

    return IFWParser(**self.dict())


ifwparser_entry_point = IFWParserEntryPoint(
  name='IFWParser',
  description='New parser entry point configuration.',
  mainfile_name_re='.*json',
)