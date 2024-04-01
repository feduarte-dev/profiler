from pro_filer.actions.main_actions import show_disk_usage  # NOQA

from unittest.mock import Mock


# nao consegui usar o mesmo padrao de show details, onde faço a fixture usando tmp_path
def test_show_disk_usage_success(monkeypatch, tmp_path, capsys):
    output_path = tmp_path / "test.py"
    output_path.write_text("test 1")
    output_path = str(output_path)

    output_path_2 = tmp_path / "test2.py"
    output_path_2.write_text("aaaaaaaaaaaaaaa")
    output_path_2 = str(output_path_2)

    mock_function = "pro_filer.actions.main_actions._get_printable_file_path"
    mock_result = Mock(return_value="test.py")
    monkeypatch.setattr(mock_function, mock_result)

    context = {"all_files": [output_path, output_path_2]}
    show_disk_usage(context)

    captured = capsys.readouterr()
    # pq eu precisei diminuir a distancia dos textos? na funcao ta ljust 70
    expected_output = f"""'test.py':{''.ljust(60)} 15 (71%)
'test.py':{''.ljust(60)} 6 (28%)
Total size: 21\n"""

    assert captured.out == expected_output
