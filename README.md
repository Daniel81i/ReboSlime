<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="./assets/round_reboslime.png" style="border-radius: 100px;" width="200" height="200" alt="ReboSlime">
</p>


<div align="center">

# ReboSlime

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
<div>SlimeVR Server で ReboCap を使用する</div>
<div style="margin-bottom: 12px">Use ReboCap in SlimeVR Server</div>

<!-- prettier-ignore-end -->

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/colasama/reboslime/master/LICENSE">
    <img src="https://img.shields.io/github/license/colasama/reboslime" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.10.x-blue?logo=python&logoColor=edb641" alt="python">
</p>

### このリポジトリは https://github.com/colasama/ReboSlime からforkされたソースを更新したものです

## 使用説明

- `Releases` から実行ファイルをダウンロードしてください。最新の `v0.4.2` は Rebocap v40 以降のバージョンに対応しています。もし以前の VMT と連携するバージョンを使いたい場合は、 `v0.31` をダウンロードしてください。
- SlimeVR サーバーを起動します。
- ReboCap クライアントを開き、動作 **动作校准1**。
- `run.bat` または `reboslime.exe` を実行します。
- これで SlimeVR にトラッカーが表示されるはずです。その後は通常の SlimeVR の使い方に従ってください。

## 開発関連

- 本プロジェクトは `Poetry` を使用して依存関係を管理しています。Python 3.10.x をインストールした後、  `pip install poetry` を実行してください。
- `poetry install` で依存関係をインストールし、 `poetry run python reboslime.py` を実行すればプログラムを起動できます。

## パッケージング関連

- 本プロジェクトを実行ファイルとしてパッケージ化する場合は、 `pyinstaller` をインストールした後、以下のコマンドを実行してください。

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py
  ```

- パッケージ化が完了したら、 `config.json` を実行ファイルと同じディレクトリに置いてください。

## 注意事項

- ReboCap - クライアントの仕様上、現在は元の VR の使用方法と同様に、胸・腰・脚の 8 点装着 が必須です。また、最低でもこの 8 点を装着しないと正常に動作しません。現在は 6 / 8 / 10 / 12 / 15 点から選択できます。
  - 6 点：胸 + 腰 + 大腿 + 下腿
  - 8 点：胸 + 腰 + 大腿 + 下腿 + 足
  - 10 点：胸 + 腰 + 大腿 + 下腿 + 足 + 上腕
  - 12 点：胸 + 腰 + 大腿 + 下腿 + 足 + 上腕 + 前腕
  - 15 点：全身
- **注意**：どの構成を選んでも「0 番ノード」が出現します。未割り当てにするか、または腰（ヒップ）に割り当てることを推奨します。

## ToDo

- [x] 装着点数の選択機能を実装。
- [ ] 15 点モードで頭部ノードが使用できない問題の解決。

## 謝辞

- https://github.com/lmore377/moslime - SlimeVR のネットワーク通信部分は、このプロジェクト構造を大きく参考にしています。
