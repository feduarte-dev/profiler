from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files(setup):
    no_extension, with_extension = setup

    context = {
        "all_files": [
            no_extension,
            with_extension,
        ]
    }
    result = find_duplicate_files(context)
    assert result == []


def test_find_duplicate_files_same_files(setup):
    no_extension, _ = setup

    context = {"all_files": [no_extension, no_extension]}

    assert find_duplicate_files(context) == [(no_extension, no_extension)]


def test_find_duplicate_files_invalid_file():
    context = {
        "all_files": [
            "./tests/invalid.py",
            "./tests/actions/invalid.py",
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
