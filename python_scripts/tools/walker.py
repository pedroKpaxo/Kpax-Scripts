"""
A module for walking directories, get files and folders inside a directory.
"""

import os
import pathlib
from typing import Tuple

from .searcher import Searcher

FileTag = Tuple[str, pathlib.Path]


def get_folders(path: str) -> list[pathlib.Path]:
    """
    Get all folders insithe the given path.

    Args:
        path (str): A string describing the path

    Returns:
        list[pathlib.Path]: A list of folder paths in the parent path
    """
    root_directory = pathlib.Path(path)
    folders = [path for path in root_directory.glob('*/')
               if path.is_dir() is True]
    return folders


def get_files(path: str) -> list[pathlib.Path]:
    """
    Get all folders insithe the given path.

    Args:
        path (str): A string describing the path

    Returns:
        list[pathlib.Path]: A list of folder paths in the parent path
    """
    root_directory = pathlib.Path(path)
    files = [path for path in root_directory.glob('*/')
             if path.is_file() is True]
    return files


def get_file_tags(dir_path: str, extensions: list[str]) -> list[FileTag]:
    """
    Gets all folders inside a directory, and then loops in each folder
    looking for files of a given extension, appending then to a list.
    It sorts the list by file size before returning it.

    Args:
        string_path (str): A path to the directory to be scanned
        extensions (list[str]): A list of strings representing the extensons

    Returns:
        list[FileTag]: A list of tuples[str, Path]
    """
    # NOTE Asserting the variables
    assert isinstance(dir_path, str) is True, 'Please a path string'  # noqa
    assert isinstance(extensions, list) is True, 'Please provide a list of strings'  # noqa

    # - Creating the extension sets.
    extensions = set(extensions)
    # - Getting the folder list
    folders = get_folders(dir_path)
    # - Creating the result list
    initial_tuples: list[FileTag] = []

    for folder in folders:
        dlis_files = Searcher.search_extensions(folder, extensions)
        for file in dlis_files:
            tuple_file_well = (folder.name, file)
            initial_tuples.append(tuple_file_well)
    initial_tuples = sorted(initial_tuples, key=lambda x: os.stat(x[1]).st_size)  # noqa

    return initial_tuples
