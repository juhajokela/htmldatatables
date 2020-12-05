# htmldatatables

## Installation

### CLI

`pip install git+https://github.com/juhajokela/htmldatatables.git`

### requirements.txt

`git+https://github.com/juhajokela/htmldatatables.git`

## Usage

```python
from htmldatatables import render_table

data = [{'key':'value', 'number': 123}, {'key':'another value', 'number': 1337}]

render_table(data)
render_table(data, datatables=True)
```
