from pro_filer.actions.main_actions import show_disk_usage  # NOQA

from unittest.mock import Mock


def test_show_disk_usage_success(monkeypatch, capsys, setup):
    mock_function = "pro_filer.actions.main_actions._get_printable_file_path"
    mock_result = Mock(return_value="test.py")
    monkeypatch.setattr(mock_function, mock_result)

    no_extension, with_extension_2 = setup
    context = {"all_files": [no_extension, with_extension_2]}
    show_disk_usage(context)

    captured = capsys.readouterr()
    expected_output = f"""'test.py':{''.ljust(60)} 17 (54%)
'test.py':{''.ljust(60)} 14 (45%)
Total size: 31\n"""

    assert captured.out == expected_output
