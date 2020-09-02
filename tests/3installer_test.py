# -*- coding: utf-8 -*-
"""Tests for basic CLI function."""
# third-party imports
import pytest

# first-party imports
import sh

# module imports
from . import print_docstring
from . import working_directory

# global constants
azulejo = sh.Command("azulejo")


@print_docstring()
def test_installer(tmp_path):
    """Test basic cli function."""
    with working_directory(tmp_path):
        try:
            output = azulejo(["install"])
        except sh.ErrorReturnCode as errors:
            print(errors)
            pytest.fail("Installer test failed")
        assert "muscle" in output
        assert "usearch" in output


@print_docstring()
def test_build(tmp_path):
    """Test building dependencies."""
    with working_directory(tmp_path):
        try:
            output = azulejo(["-q", "install", "-f", "-y", "all"])
        except sh.ErrorReturnCode as errors:
            print(errors)
            pytest.fail(errors)
        output = azulejo(["install"])
        assert "muscle version at recommended" in output
        assert "usearch version at recommended" in output
