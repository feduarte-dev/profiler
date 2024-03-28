"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=lambda x: x.count("/"))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        new_file_name = file_name
        new_search_term = search_term

        if not case_sensitive:
            new_file_name = file_name.lower()
            new_search_term = search_term.lower()

        if new_search_term in new_file_name:
            found_files.append(path)

    return found_files


teste = {
    "all_files": [
        "/path/to/file.sql",
        "/path/to/file.txt",
        "/path/to/file2.txt",
        "/path/to/FILE.txt",
        "/path/to/FILE2.TXT",
        "/path-to/file.txt",
    ]
}

print(find_file_by_name(teste, "FILE", False))
