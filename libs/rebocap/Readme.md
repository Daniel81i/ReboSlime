# Python SDK

# current support python version
- python3.7
- python3.7
- python3.8
- python3.9
- python3.10
- python3.11
- python3.12

# example
以下のコマンドを直接実行します。

`python reborncap_ws_sdk_example.py`

# 使い方
```python
import rebocap_ws_sdk

def pose_msg_callback(self: rebocap_ws_sdk.RebocapWsSdk, tran: list, pose24: list, static_index: int, ts: float):
    pass

def exception_close_callback(self: rebocap_ws_sdk.RebocapWsSdk):
    print("exception_close_callback")

# SDK の初期化
# ここで座標系や、回転情報の出力方法（グローバル / ローカル）を選択できます
sdk = rebocap_ws_sdk.RebocapWsSdk(rebocap_ws_sdk.CoordinateType.UECoordinate, use_global_rotation=True)
# 姿勢データ受信時のコールバックを設定
sdk.set_pose_msg_callback(pose_msg_callback)
# 異常切断時のコールバックを設定
sdk.set_exception_close_callback(exception_close_callback)
# 接続開始（ポート番号を指定）
open_ret = sdk.open(7690)
```
# データ構造
- trans:
  - 浮動小数点数3つからなるリスト
  - 現在は 骨盤（Pelvis）の位置情報 を表します
- pose24:
  - 24個の関節それぞれの クォータニオン（回転）
  - Pelvis がルートノードです
  - 関節の構成や位置関係は、以下の SMPL 関節構造を参考にしてください https://blog.csdn.net/weixin_43822395/article/details/124378186

```python
# 関節名一覧
REBOCAP_JOINT_NAMES = [
    "Pelvis",
    "L_Hip",
    "R_Hip",
    "Spine1",
    "L_Knee",
    "R_Knee",
    "Spine2",
    "L_Ankle",
    "R_Ankle",
    "Spine3",
    "L_Foot",
    "R_Foot",
    "Neck",
    "L_Collar",
    "R_Collar",
    "Head",
    "L_Shoulder",
    "R_Shoulder",
    "L_Elbow",
    "R_Elbow",
    "L_Wrist",
    "R_Wrist",
    "L_Hand",
    "R_Hand"
]
```
- static_index
  - int 型の値
  - -1 : 接地しているポイントが検出されていない
  - 0, 1, 2 : 左足・前足部（左 / 中央 / 右）
  - 3, 4, 5 : 左足・かかと（左 / 中央 / 右）
  - 6, 7, 8 : 右足・前足部（左 / 中央 / 右）
  - 9, 10, 11 : 右足・かかと（左 / 中央 / 右）

※ 地面との接触点情報については、現状 単一点の接触判定のみ 実装されています。
