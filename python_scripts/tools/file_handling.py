import zipfile
import pathlib
from alive_progress import alive_bar


def zip_pathlist(pathlist: list[pathlib.Path], output_file: str):
    """Zips a list of paths into a zip file."""
    
    output_file = output_file.strip()
    if not '.zip' in output_file:
        output_file = f'{output_file}.zip'

    with zipfile.ZipFile(output_file, 'w') as myzip:
        with alive_bar(len(pathlist), dual_line=True, title='Zipping Files %') as bar:  # noqa
            for path in pathlist:
                myzip.write(path)
                bar()
 