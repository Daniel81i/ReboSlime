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
