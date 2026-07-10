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

テトリス部分は公開されている実装例を参考にしながら本プロジェクト向けに改変しました。

実装内容：

- ブロック生成
- ブロック移動
- 回転処理
- 衝突判定
- ライン削除処理

---

## 🚧 Current Status

現在はプロトタイプ段階で、tetris-go.pyというのがメインファイルです。

基本的なジェスチャー認識およびゲーム操作機能は実装済みですが、
実装予定だったイベントで企画が中止されたため完成に至っておりません。

今後の改善案：
今後はジェスチャー判定モデルの改良、判定からの操作処理の改善をする必要があります。モデルに関しては、用意したデータセットに対してモデルが大きすぎたせいで学習が安定せず過学習を起こしたようなので、学習ステップパラメータの縮小もしくは学習モデルそのものの縮小が必要です。判定からの操作処理では、目に見えてラグが生じている問題を解決する必要があります。現状問題を分析中です。

---

## 📚 Development Background

イベント展示用作品として、
コンピュータビジョン技術をゲーム操作へ応用することを目的として制作しました。

---

## 👤 Author

UTA7972(S.K)
