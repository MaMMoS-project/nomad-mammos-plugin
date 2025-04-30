import logging

from nomad.datamodel import EntryArchive

from mammos.parsers.cubeparser import CubeParser
from mammos.schema_packages.cube import Cube


def test_parse_file():
    parser = CubeParser()
    archive = EntryArchive()
    parser.parse('tests/data/cube.dat', archive, logging.getLogger())

    assert isinstance(archive.data,Cube)
