# Motion Tetris

人体・手指ジェスチャー認識を利用して操作するテトリスゲームの試作プロジェクトです。

Webカメラから取得した映像をMediaPipeで解析し、ユーザーの手の形や指の方向を認識することで、
キーボードを使用せず身体動作によるゲーム操作を実現しました。

本プロジェクトはイベント展示用の作品として開発を開始しました。

---

## 🎯 Overview

本プロジェクトでは、カメラ入力から取得したジェスチャーをゲーム入力へ変換する
インタラクティブなゲームシステムを開発しました。

通常の入力デバイスではなく、自然な身体動作によってテトリスを操作することを目的としています。

---

## 🛠 Technology Stack

- Python
- Tkinter
- MediaPipe
- OpenCV

---

## ⚙️ System Architecture

処理の流れ：
Web Camera
↓
Image Acquisition
↓
Hand / Gesture Recognition (MediaPipe)
↓
Gesture Classification
↓
Input Conversion
↓
Tetris Control


---

## 🎮 Gesture Control

| Game Action | Gesture | Description |
|---|---|---|
| MOVE_LEFT | left | 人差し指を左方向へ向ける |
| MOVE_RIGHT | right | 人差し指を右方向へ向ける |
| MOVE_DOWN | down / under | 親指を下に向ける（Thumbs Down） |
| ROTATE | rotate | 5本の指を広げる（Open Hand） |
| NEUTRAL | face | ジェスチャーなし状態 |

---

## 🧩 Tetris Implementation

テトリス部分は既存の簡易実装を参考にし、
本プロジェクト向けに改変しました。

実装内容：

- ブロック生成
- ブロック移動
- 回転処理
- 衝突判定
- ライン削除処理

---

## 🚧 Current Status

現在はプロトタイプ段階です。

基本的なジェスチャー認識およびゲーム操作機能は実装済みですが、
イベント用途の変更により開発を停止しました。

今後の改善案：

- ジェスチャー認識精度の向上
- 誤認識の低減
- 操作レスポンスの改善
- UI改善

---

## 📚 Development Background

イベント展示用作品として、
コンピュータビジョン技術をゲーム操作へ応用することを目的として制作しました。

---

## 👤 Author

Rakutaro Sorahata
