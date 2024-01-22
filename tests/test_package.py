from __future__ import annotations

import importlib.metadata

import pypwsqc as m


def test_version():
    assert importlib.metadata.version("pypwsqc") == m.__version__
