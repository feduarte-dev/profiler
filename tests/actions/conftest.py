import pytest


@pytest.fixture
def setup(tmp_path):
    output_path = tmp_path / "test"
    output_path.write_text("no extension test")
    no_extension = str(output_path)

    output_path_2 = tmp_path / "test.py"
    output_path_2.write_text("extension test")
    with_extension = str(output_path_2)

    return no_extension, with_extension
