from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date

no_extension_result = f"""File name: test
File size in bytes: 17
File type: file
File extension: [no extension]
Last modified date: {date.today()}
"""

with_extension_result = f"""File name: test.py
File size in bytes: 14
File type: file
File extension: .py
Last modified date: {date.today()}
"""


def test_show_details_success(capsys, setup):
    no_extension, with_extension = setup

    context = {"base_path": no_extension}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == no_extension_result

    context = {"base_path": with_extension}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == with_extension_result


def test_show_details_does_not_exist(capsys):
    context = {"base_path": "/invalid/path"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'path' does not exist\n"
