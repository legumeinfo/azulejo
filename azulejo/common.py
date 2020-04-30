# -*- coding: utf-8 -*-
"""
Constants and functions in common across modules
"""
# standard library imports
from pathlib import Path

# third-party imports
import poetry_version

NAME = "azulejo"
VERSION = "".join(poetry_version.extract(source_file=__file__))
STATFILE_SUFFIX = f"-{NAME}_stats.tsv"
ANYFILE_SUFFIX = f"-{NAME}_ids-any.tsv"
ALLFILE_SUFFIX = f"-{NAME}_ids-all.tsv"
CLUSTFILE_SUFFIX = f"-{NAME}_clusts.tsv"
SEQ_FILE_TYPE = "fasta"


def get_paths_from_file(f, must_exist=True):
    inpath = Path(f).expanduser().resolve()
    if must_exist and not inpath.exists():
        raise FileNotFoundError(f)
    dirpath = inpath.parent
    return inpath, dirpath
