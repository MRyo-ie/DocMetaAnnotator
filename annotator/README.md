# annotationツールについて
## labelme
### 詳しくは
https://github.com/wkentaro/labelme
https://qiita.com/kouki_outstand/items/7b7597f271beca0051e5
https://qiita.com/okubo999/items/a862dcbfe7b4812192b4

### 特徴
- GUI annotation ソフト。
  - Web版じゃない。
- PyQt で作られているので、macOS から Ubuntu、 Windows まで、
  幅広く対応している。
- UI は、
  - 日本語非対応 だが、
  - シンプルで使いやすい。
  - annotation が必要なレベルの人なら、迷わず操作できるはず(笑)
- polygon レベルで annotation できる。
- 矩形、円、線、点 にも変更可能。
  - 画像上を右クリックで、選べるメニューが出てくる。

### Install
詳しくは、本家 [GitHub](https://github.com/wkentaro/labelme) 参照。

Dockr イメージもあるらしい？
#### macOS
pyqt5 で動くらしい？ python2/3 どっちもOK
```
brew install pyqt
pip install labelme
```

#### ubuntu18.04
```
sudo apt-get install labelme
```

### 起動
```
$ labelme
```
- 読み込み
  - 左側上のフォルダアイコン
- アノテーション開始
  - 左側下の、polygon 〜 って書いてあるアイコン を押すと、
    Polygon の点が打てるようになる。
  - 矩形、円、線、点 に切り替えたい場合は、画像の上で右クリック。
    - Rectangle：矩形（長方形）
    - circle：円
    - ...
  - 矩形、円などは、始点と終点で１回づつクリックする感じ。
- 保存
  - ⌘+S
  - 保存するダイアログが出る。
  - ここで保存されるのは、点の情報がまとめられた Json ファイル。

### 結果の確認
```
$ labelme_draw_json　path/to/〜.json
```

### 結果の出力
#### labelme による変換
```
$ labelme_json_to_dataset　path/to/〜.json  -o 【出力先dir】
```

#### SS モデル用に最適化するスクリプト
labelme の出力を 合体したり、リネームしたりして、
ESPNet の学習用データにするスクリプト
```

```

