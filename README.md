# アプリ概要
PDF, XML を 画像に変換し、SS用のアノテーションするまでのスクリプト群。
1. PDF, XML を png に変換
2. アノテーションツールを起動
3. アノテーションデータを、各種形式に変換


# 1. PDF, XML を png に変換
## Install
```
$ brew install poppler
$ pip install -r requirement.txt
```
https://shotanuki.com/pythonでpdfを画像に変換する/


## 変換
```
python3 to_img.py
```
- オプション
  - `--source_type`
    - `pdf`, `xml` or ...
    - 初期値は `pdf`
  - `--source_dir`
    - pdf, xmlファイルのある場所のパスを指定できる。
    - 初期値は `datas/`
  - `--out_dir`
    - 変換後の画像の出力先のパス
    - 初期値は `datas/out`


# 2. アノテーション する。
[annotator/README.md](annotator/README.md) を参考に。

