import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test_cube.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    # TODO: we should have some meaningful tests here ...
    assert len(entry_archive.data.steps) == 80 # noqa: PLR2004
