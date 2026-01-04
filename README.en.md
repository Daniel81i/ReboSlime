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
- Changed the default number of tracking points to 15.
- added settings for the default number of tracking points at startup, and the timeout duration for tracking‑point input. These values can be modified in `config.json`.
- Added the necessary configuration for building with `Poetry` on GitHub, assuming GitHub-based builds and releases.

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
  After installing Python 3.12.x, run `pip install poetry`.
- Install dependencies with `poetry install`, then start the program with:  
  `poetry run python reboslime.py`.

## Packaging

- To package this project into an executable, install `pyinstaller` and run:

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py
  ```

- After packaging is complete, place `config.json` in the same directory as the executable.

## Notes

- Due to the specifications of the ReboCap client, at least the same setup as the original VR usage is required: 8 mounting points (chest, waist, and legs) are mandatory. The application will not function correctly unless at least these 8 points are used. Currently, you can choose from 6 / 8 / 10 / 12 / 15 points.
  - 6 points: chest + waist + thighs + lower legs
  - 8 points: chest + waist + thighs + lower legs + feet
  - 10 points: chest + waist + thighs + lower legs + feet + upper arms
  - 12 points: chest + waist + thighs + lower legs + feet + upper arms + forearms
  - 15 points: full body
- **Note**: Regardless of the configuration you choose, a “Node 0” will appear. It is recommended to leave it unassigned or assign it to the waist (hips).

## ToDo

- [x] Implemented tracking point count selection.
- [ ] Fix the issue where the head node cannot be used in 15-point mode.

## Acknowledgements

- https://github.com/lmore377/moslime — The SlimeVR network communication part of this project is heavily based on the structure of this project.
