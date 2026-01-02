<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="./assets/round_reboslime.png" style="border-radius: 100px;" width="200" height="200" alt="ReboSlime">
</p>


<div align="center">

# ReboSlime

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
<div>在 SlimeVR Server 中使用 ReboCap</div>
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

- 下载 `Releases` 中的可执行文件，最新 `v0.4.2` 已适配 Rebocap v40 及以后的版本，如果想要使用之前与 VMT 相配合的程序，请下载 `v0.31` 版本。
- 打开 SlimeVR 服务端。
- 打开 ReboCap 客户端，点击 **动作校准1**。
- 运行 `run.bat` 或者 `reboslime.exe`。
- 现在应该能在 SlimeVR 中看到追踪器了！之后按照 SlimeVR 的用法来就可以了。

## 開発関連

- 本项目使用 `Poetry` 进行依赖管理，请安装 3.10.x 版本的 Python 后运行 `pip install poetry`。
- 使用 `poetry install` 安装依赖，然后运行 `poetry run python reboslime.py` 即可运行程序。

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
