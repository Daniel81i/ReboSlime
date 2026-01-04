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

- 本项目使用 `Poetry` 管理依赖。安装 Python 3.12.x 后，请执行 `pip install poetry`。
- 使用 `poetry install` 安装依赖，然后通过 `poetry run python reboslime.py` 启动程序。

## 打包相关

- 若需要将本项目打包为可执行文件，请在安装 `pyinstaller` 后执行以下命令：

  ```bash
  pyinstaller -F -i .\assets\reboslime.ico reboslime.py
  ```

- 打包完成后，请将 `config.json` 放置在与可执行文件相同的目录中。

## 注意事项

- 由于 ReboCap 客户端的规格限制，目前与原始 VR 使用方式相同，**必须佩戴胸部、腰部和腿部共 8 个追踪点**。如果未至少佩戴这 8 个追踪点，程序将无法正常运行。目前可选择 6 / 8 / 10 / 12 / 15 个追踪点。
  - 6 点：胸部 + 腰部 + 大腿 + 小腿
  - 8 点：胸部 + 腰部 + 大腿 + 小腿 + 脚
  - 10 点：胸部 + 腰部 + 大腿 + 小腿 + 脚 + 上臂
  - 12 点：胸部 + 腰部 + 大腿 + 小腿 + 脚 + 上臂 + 前臂
  - 15 点：全身
- **注意**：无论选择哪种配置，都会出现“0 号节点”。建议将其设为未分配，或分配到腰部（臀部）。

## ToDo

- [x] 已实现追踪点数量选择功能。
- [ ] 解决在 15 点模式下无法使用头部节点的问题。

## 致谢

- https://github.com/lmore377/moslime —— 本项目中 SlimeVR 的网络通信部分在很大程度上参考了该项目的结构。
