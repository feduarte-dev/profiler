from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            (
                "Found 3 files and 2 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"  # NOQA
                "First 5 directories: ['src', 'src/utils']\n"
            ),
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                    "src/utils/__init__2.py",
                    "src/utils/__init__3.py",
                    "src/utils/__init__4.py",
                ],
                "all_dirs": [
                    "src",
                    "src/utils",
                    "src/utils2",
                    "src/utils3",
                    "src/utils4",
                    "src/utils5",
                ],
            },
            (
                "Found 6 files and 6 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/__init__2.py', 'src/utils/__init__3.py']\n"  # NOQA
                "First 5 directories: ['src', 'src/utils', 'src/utils2', 'src/utils3', 'src/utils4']\n"  # NOQA
            ),
        ),
    ],
)
def test_show_preview_sucess(context, expected_result, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result
