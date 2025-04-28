from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        # from cube.parsers.cubeparser import CubeParser
        from cube.parsers.cubeparser import CubeParser

        return CubeParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*dat',
)


class UUParserEntryPoint(ParserEntryPoint):
  def load(self):
    from cube.parsers.uuparser import UUParser

    return UUParser(**self.dict())


uuparser_entry_point = UUParserEntryPoint(
  name='UUParser',
  description='New parser entry point configuration.',
  mainfile_name_re=r'.*cif',
)
