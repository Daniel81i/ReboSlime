<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="./assets/round_reboslime.png" style="border-radius: 100px;" width="200" height="200" alt="ReboSlime">
</p>


<div align="center">

# ReboSlime

**🌐 Languages:**  
[🇯🇵 日本語](README.md) | [🇺🇸 English](README.en.md) | [🇨🇳 简体中文](README.zh.md)


<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
<div>SlimeVR Server で ReboCap を使用する</div>
<div style="margin-bottom: 12px">Use ReboCap in SlimeVR Server</div>

<!-- prettier-ignore-end -->

</div>

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.12.x-blue?logo=python&logoColor=edb641" alt="python">
</p>

## このリポジトリは https://github.com/colasama/ReboSlime からforkされたソースを更新したものです

## fork元からの変更点
- Rebocap SDKのアップデート。
- Python 3.12 でのビルド。
- トラキングポイントの15点をデフォルトとする、起動時のトラッキングポイント入力のタイムアウト時間を設定、これらはconfig.jsonにて設定変更可能です。

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




# English

## This repository is an updated fork of https://github.com/colasama/ReboSlime

## Changes from the original fork
- Updated Rebocap SDK.
- Built with Python 3.12.
- Default tracking point count set to 15.  
  The startup tracking point timeout and other settings can be configured in `config.json`.

## Usage

- Download the executable from the `Releases` page.  
  The latest `v0.4.2` supports Rebocap v40 and later.  
  If you need the version compatible with older VMT integration, download `v0.31`.
- Start the SlimeVR server.
- Open the ReboCap client and perform **Action Calibration 1**.
- Run `run.bat` or `reboslime.exe`.
- The trackers should now appear in SlimeVR. Continue using SlimeVR as usual.

## Development

- This project uses `Poetry` for dependency management.  
  After installing Python 3.10.x, run `pip install poetry`.
- Install dependencies with `poetry install`, then start the program with:  
  `poetry run python reboslime.py`.

## Packaging

- To package this project into an executable, install `pyinstaller` and run:

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py




# 簡体字中国語

## 本仓库是在 https://github.com/colasama/ReboSlime 的基础上 fork 并更新的版本

## 与原仓库的主要区别
- 更新了 Rebocap SDK。
- 使用 Python 3.12 进行构建。
- 默认启用 15 点追踪模式，并可在 `config.json` 中修改启动时的追踪点输入超时时间等设置。

## 使用说明

- 请从 `Releases` 页面下载可执行文件。最新的 `v0.4.2` 版本支持 Rebocap v40 及以上版本。如果需要与旧版 VMT 联动的版本，请下载 `v0.31`。
- 启动 SlimeVR 服务器。
- 打开 ReboCap 客户端，进行 **动作校准1**。
- 运行 `run.bat` 或 `reboslime.exe`。
- 之后 SlimeVR 中应当会显示对应的追踪器，后续按正常的 SlimeVR 使用方式进行即可。

## 开发相关

- 本项目使用 `Poetry` 管理依赖。安装 Python 3.10.x 后，请执行 `pip install poetry`。
- 使用 `poetry install` 安装依赖，然后通过 `poetry run python reboslime.py` 启动程序。

## 打包相关

- 若需要将本项目打包为可执行文件，请在安装 `pyinstaller` 后执行以下命令：

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py

