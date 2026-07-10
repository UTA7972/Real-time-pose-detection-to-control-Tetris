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
