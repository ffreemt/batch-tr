"""Test batch_tr to_lang="zh"."""
from pathlib import Path
from batch_tr import batch_tr
from logzero import logger

CDIR = Path(__file__).parent
logger.info("CDIR: %s", CDIR)
FILEPATH = Path(CDIR) / "0test_en.txt"


def test_batch_tr_zh():
    """Test batch_tr to_lang="zh"."""
    # assert 0

    paras_en = Path(FILEPATH).read_text("utf8").strip().splitlines()

    paras_tr = batch_tr(paras_en)

    assert len(paras_tr) == len(paras_en)
