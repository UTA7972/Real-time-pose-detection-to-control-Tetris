# Motion Tetris

姿勢推定を利用して、身体の動きで操作するテトリスゲームの試作プロジェクトです。

Webカメラから取得した映像を解析し、Mediapipeによる姿勢推定を用いて、
ユーザーの身体動作をゲーム操作へ変換するインタラクティブなゲームシステムを開発しました。

本プロジェクトはイベント展示用の作品として制作を開始しました。

---

## 🎯 Overview

本プロジェクトでは、通常のキーボード入力ではなく、
身体の動きを利用してテトリスを操作するシステムを実装しました。

リアルタイム姿勢推定によって取得した身体情報を入力として利用し、
画像処理技術をゲーム操作へ応用することを目的としています。

---

## 🛠 Technology Stack

- **Programming Language**
  - Python

- **GUI Framework**
  - Tkinter

- **Computer Vision**
  - MediaPipe
  - OpenCV

- **Development Environment**
  - VSCode

---

## ⚙️ System Architecture

処理の流れ：
Web Camera
↓
Image Acquisition
↓
Pose Estimation (MediaPipe)
↓
Body Landmark Analysis
↓
Motion Recognition
↓
Tetris Control



---

## 🎮 Features

- Webカメラによるリアルタイム映像取得
- MediaPipeを利用した人体姿勢推定
- 姿勢情報を利用したゲーム操作
- PythonによるGUIベースのテトリス実装

---

## 🧩 Tetris Implementation

テトリス部分は既存の簡易実装を参考にし、
自身のプロジェクト向けに改変しました。

以下のゲーム処理を実装しています：

- ブロック生成
- ブロック移動
- 衝突判定
- ライン処理

---

## 🚧 Current Status

現在はプロトタイプ段階です。

基本的なゲーム機能および姿勢推定処理は実装済みですが、
イベント用途の変更により開発を停止しました。

今後の改善案：

- 姿勢認識精度の向上
- 操作方法の最適化
- UI改善
- 入力遅延の削減

---

## 📚 Purpose

イベント展示用作品として、
コンピュータビジョン技術を利用した新しいゲーム操作方法の実現を目的として制作しました。

---

## 👤 Author

Rakutaro Sorahata
