## 🌟 プロジェクト概要
一般のお客様向けの直感的な予約インターフェースと、従業員向けの高度な管理機能を備えています。

---

## To-dos
- Improve the logic for making reservations (need to add login: attemped to add the logic yet password was not needed in seed.py)
- Fix the logic for making reservations from staff page (staff selection is not needed)

---

## 🛠 テックスタック (Tech Stack)

### Backend
- **Language:** Python 3.x
- **Framework:** Flask
- **ORM:** SQLAlchemy 2.0 (Type-hinting 対応)
- **Architecture:** Clean Architecture (Domain / Usecase / Interface / Infrastructure)
- **Auth:** Flask-Login, MSAL (Microsoft Authentication Library)

### Frontend
- **Engine:** Jinja2 (Server Side Rendering)
- **Styling:** Tailwind CSS
- **Interactivity:** Alpine.js / HTMX (予定)

### Quality & DevOps
- **Testing:** pytest
- **Analysis:** coverage.py
- **Environment:** venv (Python Virtual Environment)

---

## 📋 機能一覧

### 01. 予約システム (Customer Facing)
お客様がストレスなくスムーズに予約を完了できるインターフェースを提供します。
- **情報閲覧:** 店舗情報、在籍スタッフ、施術メニューの確認。
- **スマート予約:** スタッフ指名、メニュー選択、空き時間枠のリアルタイム指定。

### 02. 従業員管理システム (Internal Management)
#### 🔐 管理者権限 (Admin)
組織全体の運営リソースを完全にコントロールします。
- **メニュー管理:** サービス内容の追加・削除・編集。
- **スタッフ管理:** 従業員情報の登録・権限設定。
- **予約・売上管理:** 全予約データの閲覧・編集・キャンセル対応。

#### 👤 従業員権限 (Staff)
日々の業務とスケジュールを効率的に管理します。
- **シフト管理:** 自身の出勤・休憩時間のセルフ設定。
- **スケジュール確認:** 全体の予約状況をカレンダー形式で把握（※顧客個人情報は非表示）。

### 03. マイページ (Customer Account)
リピート率を向上させるためのパーソナライズ機能です。
- **来店履歴:** 過去の施術内容や担当者の振り返り。
- **プロフィール管理:** 連絡先や個人情報の変更。
- **特典:** 利用可能なクーポンの確認と適用。

---

## 🏗 ディレクトリ構造
```text
app/
├─domain/          # エンティティ・ビジネスルール
├─usecase/         # アプリケーション固有のロジック
├─interface/       # コントローラー・ルート定義
├─infrastructure/  # DB操作・外部API実装
├─static/          # CSS / JS / Image
└─templates/       # Jinja2 HTMLテンプレート