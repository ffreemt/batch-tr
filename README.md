# batch_tr
<!--- batch-tr  batch_tr  batch_tr batch_tr --->
[![tests](https://github.com/ffreemt/batch-tr/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/batch_tr.svg)](https://badge.fury.io/py/batch_tr)

batch translate (10000 chars)

<!-- snippets-mat\deepl-translate-memo.txt -->

## Use It

```python
from batch_tr.batch_tr import batch_tr

res = batch_tr("very long text " * 10000)
print(res)
# to chinese/zh

print(batch_tr("test me", to_lang="de"))

# long list
res = batch_tr(("very long text \n" * 10000).splitlines())
# equally long list of translated text
# known to work for to_lang="zh" (default)
print(res)
```