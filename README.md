# Geneplore AI's API

**NOTICE: Archived due to the depreciation of the Geneplore API as of July 1, 2024.**

A Python client for the Geneplore API. See https://docs.geneplore.com for more information.

## Installation

`pip install geneplore_api`

## Usage

```python
from geneplore_api import api_sync as api

api.api_key = "YOUR_API_KEY"

print(api.Chat.GetModels())
```
