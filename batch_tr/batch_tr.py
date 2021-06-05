"""Machine translate via pythonpy."""
# snippets-mat\deepl-translate-memo.txt
from typing import List, Tuple, Union
import os
import re
import textwrap
import logzero
from logzero import logger
from translatepy import Translator

loglevel = os.environ.get("loglevel")
if loglevel is not None:
    try:
        loglevel = int(loglevel)
    except Exception as e:
        logger.error("%s, setting loglevel to 20", e)
        loglevel = 20
logzero.loglevel(loglevel or 20)
google_tr = Translator(
    use_google=True,
    use_yandex=False,
    use_bing=False,
    use_reverso=False,
    use_deepl=False,
).translate


# fmt: off
def batch_tr(
        text: Union[str, List[str], Tuple[str]],
        to_lang: str = "zh",
        from_lang: str = "auto",
        maxlen: int = 10000,
        delim: str = "εσ",  # Σσ εσ
) -> Union[str, List[str]]:
    # fmt: on
    """Batch translate via pythonpy.

    Args:
        text: string of list of string to translate
        to_lang: destination lang, default to "en"
        from_lang: source lang, default to "auto"
        maxlen: max length
        delim: for combining and splitting
    Returns:
        Translated text (maintain para info)

    Note 1: text better strip() before feeding to batch_tr, the extra new lines at the end my cause some problem.

    Note 2: to_lang="en", not quite working yet
    """
    if to_lang not in ["zh", "chinese"]:
        logger.debug("to_lang: %s", to_lang)
        logger.warning(" Only tested for to_lang='zh', to_lang='en' not quite work.")

    try:
        to_lang = to_lang.lower()
    except Exception as e:
        logger.error(e)
        to_lang = "zh"
    if to_lang.lower() in [
        "zh",
        "zhong",
        "中",
        "中文",
    ]:
        to_lang = "chinese"

    # halve maxlen for chinese text
    # TODO: may need more sophisticated method
    if isinstance(text, str):
        # important: remove " '
        text = text.replace('"', '').replace("'", "")
        if len(re.findall(r"[一-龟]", text)) > len(text) // 2:
            maxlen = maxlen // 2
    else:
        if len(re.findall(r"[一-龟]", " ".join(text))) > len(text) // 2:
            maxlen = maxlen // 2

    if isinstance(text, str):
        logger.debug(" text is tring")

        if not text.strip():
            return ""

        # break down to maxlen
        res = []
        for seg in textwrap.wrap(text, maxlen):
            try:
                _ = google_tr(seg, to_lang)
            except Exception as e:
                logger.error(e)
                raise

            try:
                _ = _.result
            except Exception as e:
                logger.error(e)
                raise
            res.append(_)

        # return res.result
        return " ".join(res)

    # ### text is a list
    # ### combine, then split ###
    len_ = len(text)  # for checking later on

    # str_ = f"\n{delim}\n".join(text)
    str_ = f" {delim} ".join(text)
    res_ = batch_tr(str_, to_lang, from_lang)

    # split and strip rf"[{delim}[{delim}]"
    # res = [elm.strip(" ") for elm in str(res_).split(delim)]
    # res = [elm.strip(" ") for elm in re.split(delim, str(res_), flags=re.I)]
    # delim1 = rf"[{delim}][{delim}]"
    res = [elm.strip(" ") for elm in re.split(delim, str(res_), flags=re.I)]

    if len_ != len(res):
        logger.warning("Attention: before len: %s != after len %s", len_, len(res))
        logger.info("We proceed nevetheless.")

    return res
