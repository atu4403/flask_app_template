"""
.. include:: ../../README.md
"""
import pandas as pd

__version__ = "0.1.0"
settings = {
    "site_title": "flask app template",
}

df = pd.DataFrame(
    {
        "name": ["taro", "jiro", "saburo", "shiro"],
        "age": [20, 30, 40, 50],
        "score": [90, 80, 70, 60],
    }
)
