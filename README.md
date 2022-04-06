# flask_app_template

poetry + flask + semantic-uiのボイラープレートです。

ディレクトリ構成はざっくりこんな感じ。

```bash
.
├── src
│   └── flask_app_template
├── static
│   └── app.js
├── templates
│   ├── b_header.html
│   ├── hello.html
│   ├── index.html
│   └── layout.html
├── tests
│   ├── __pycache__
│   ├── __init__.py
│   └── test_flask_app_template.py
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── poetry.lock
├── pyproject.toml
└── pytest.ini
```

通常のpoetryと違うのは以下のディレクトリ。

- template(flaskのtemplateディレクトリ)
- static(jsやcss、画像等を置く場所)

加えてルートディレクトリに`app.py`を置いています。

## 起動方法

```bash
poetry install # 初回のみ
poetry shell
python app.py
```

## 使い方

### ブラウザ表示部分

templateディレクトリ

- layout.html
  - 全ページ共通のhtml(headやヘッダー等)
- b_header.html
  - layoutからヘッダー(headタグではなくパーツ部分)を抜き出したもの
- index.html
- hello.html
  - ページ固有のhtml

staticディレクトリ

- app.js
  - ブラウザで読み込むjs
- style.css
  - ブラウザで読み込むcss

### データ作成部分

- app.py
  - 主にルーティングを行う
  - 簡単な値を渡す
  - 複雑なデータはsrcディレクトリで作りimportする

```python
from flask import Flask
from flask import render_template
from src.flask_app_template import settings, df

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", **settings)


@app.route("/hello")
def hello():
    settings["name"] = "jiro"
    settings["table1"] = df.to_html(classes="ui striped table", index=False)
    return render_template("hello.html", **settings)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
```

- srcディレクトリ
  - app.pyを見通しよく保つ為にsrcディレクトリで値や関数を作成する
  - サイトのtitleは`settings.site_title`として設定する

[Semantic UI入門 よく使うコンポーネント - Qiita](https://qiita.com/sandabu/items/336fe312acbec98d21e3)
