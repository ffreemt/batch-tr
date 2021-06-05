"""Test batch_tr."""
from batch_tr import __version__
from batch_tr import batch_tr


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    assert batch_tr("a")
