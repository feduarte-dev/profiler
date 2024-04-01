from pro_filer.actions.main_actions import show_preview  # NOQA

context = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"],
}

result = (
    "Found 3 files and 2 directories\n"
    "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"  # NOQA
    "First 5 directories: ['src', 'src/utils']\n"
)

context2 = {
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
}

result2 = (
    "Found 6 files and 6 directories\n"
    "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/__init__2.py', 'src/utils/__init__3.py']\n"  # NOQA
    "First 5 directories: ['src', 'src/utils', 'src/utils2', 'src/utils3', 'src/utils4']\n"  # NOQA
)
# << usar parametrize


def test_show_preview_sucess(capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == result


def test_show_preview_more_than_five_files(capsys):
    show_preview(context2)
    captured = capsys.readouterr()
    assert captured.out == result2
