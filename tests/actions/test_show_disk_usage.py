from pro_filer.actions.main_actions import show_disk_usage  # NOQA

import pytest


@pytest.fixture
def setup(tmp_path):
    output_path = tmp_path / "test.py"
    output_path.write_text("extension test")
    result = str(output_path)

    return result


def test_show_disk_usage(setup, capsys):
    result = setup
    context = {"all_files": result}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == "no_extension_result"
