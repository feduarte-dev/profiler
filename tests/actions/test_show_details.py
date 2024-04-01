from pro_filer.actions.main_actions import show_details  # NOQA

import pytest


@pytest.fixture
def setup(tmp_path):
    output_path = tmp_path / "test"
    output_path.write_text(
        "no extension test"
    )  # Só funciona se eu escrevo algum conteudo
    no_extension = str(output_path)

    output_path_2 = tmp_path / "test.py"
    output_path_2.write_text("extension test")
    with_extension = str(output_path_2)

    return no_extension, with_extension


no_extension_result = """File name: test
File size in bytes: 17
File type: file
File extension: [no extension]
Last modified date: 2024-04-01\n"""
# usar uma fstring para atualizar a data dinamicamente OU usar assert in para ver se strings imutaveis estao no retorno
# OU mockar a funcao fromtimestamp

with_extension_result = """File name: test.py
File size in bytes: 14
File type: file
File extension: .py
Last modified date: 2024-04-01\n"""


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
