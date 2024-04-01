from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(tmp_path):
    output_path = tmp_path / "valid.py"
    output_path.write_text("extension test")
    no_extension = str(output_path)

    output_path_2 = tmp_path / "valid2.py"
    output_path_2.write_text("extension test aaa")
    with_extension = str(output_path_2)

    context = {
        "all_files": [
            no_extension,
            with_extension,
        ]
    }
    result = find_duplicate_files(context)
    assert result == []


def test_find_duplicate_files_same_files(tmp_path):
    output_path = tmp_path / "valid.py"
    output_path.write_text("extension test")
    no_extension = str(output_path)

    output_path_2 = tmp_path / "valid.py"
    output_path_2.write_text("extension test 2 ")
    with_extension = str(output_path_2)

    output_path_3 = tmp_path / "valid.py"
    output_path_3.write_text("extension test3 ")
    aaaaaa = str(output_path_3)

    context = {"all_files": [no_extension, with_extension, aaaaaa]}

    assert find_duplicate_files(context) == [
        (no_extension, with_extension),
        (no_extension, aaaaaa),
        (with_extension, aaaaaa),
    ]


def test_find_duplicate_files_invalid_file():
    context = {
        "all_files": [
            "./tests/invalid.py",
            "./tests/actions/invalid.py",
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
