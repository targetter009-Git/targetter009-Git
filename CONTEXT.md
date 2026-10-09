# 記憶の目論見書 (CONTEXT.md)
*指向哲学 (Oriented-Philosophia) プロジェクト文脈継承ドキュメント*

## 1. コア理念・現在地
- **発信者:** 松田智（飲茶坊さとし / マジムンさとし）
- **理念:** 光（完成品）をそのまま見せるのではなく、光の影（対話・プロセス）が物語る声を聴き、自らの位置を知る（RyuboStyle）。
- **開発状況:** 
  - 対話ログ・物語台本（第1〜3層）の蓄積フロー構築済み。
  - 音声・画像自動生成パイプライン動作確認済み。
  - 現在は `built.py` による自動ポータル投影（第4層）を自動化中。

---

## 2. 対話のあゆみ（自動更新エリア）
<!-- AUTO-GENERATED-SUMMARY:START -->
- **Unknown Date:** <img src="assets/scene01.gif" width="768" alt="デモ動画">
- **2026-10-09-AM:** ---
- **2026-10-08-AM:** 飲茶坊さとしの指向哲学（Oriented-Philosophia）対話録
<!-- AUTO-GENERATED-SUMMARY:END -->

---

## 2026-10-09 対話あゆみ・動画制作アーキテクチャの決定

### 1. 担当AI切り替え時の文脈継承と設計思想
- 担当AIが変更された場合でも、本プロジェクトの設計思想（原稿からフィルムへの昇華、`.trash/` への安全退避、マルチメディア連携）をブレずに継続すること。
- 不要ファイルや過去のアセットをプログラム（`built.py` など）で自動削除（`os.remove`）することは厳禁とし、必ず `.trash/` フォルダ（TrashBox）へ安全退避（`shutil.move`）させること。

### 2. 16:9シネマティック動画制作の基本構造（4章×3コマ＝12カット）
- **ストーリー構成:** 物語は「起・承・転・結」の全4章（4動画）で展開する。
- **1章（1動画）の構成:** 16:9 横長アイキャッチ画像 × 3コマ ＋ 対応するシナリオテキスト ＋ 音声トラック（.mp3）。
- **全アセット数:** 計12カット（16:9画像 12枚、音声、動画 .mp4）。

### 3. リポジトリ間の役割分担と構成
1. **`targetter009-Git/targetter009-Git`（原稿庫）**
   - マスター原稿 `README.2026.10.09.AM.md` および本記憶帳 `CONTEXT.md` を管理。
   - `update-context.yml` ワークフローにより対話のあゆみを自動記憶。
2. **`targetter009-Git/ryubo-style`（映写機・アセット生成エンジン）**
   - **`documents/`**: 昇華された `Film.2026.10.09.AM.A.md`（対話深層）および `Film.2026.10.09.AM.B.md`（戯曲ボイスドラマ）を配置。
   - **`generate_movies.py`**: 12コマの画像と音声を結合して `.mp4` 動画を出力する処理エンジン本体。
   - **`.github/workflows/`**: 
     - `generate-images.yml`（12コマ画像生成）
     - `generate-audio.yml`（音声生成）
     - `generate-movies.yml`（動画結合・出力）
   - **`scripts/built.py`**: 古いフィルムを `.trash/` へ安全退避させ、12カット絵コンテ構造を読み込んで `index.html`（ポータル）へ投射する映写機。
  
---

## 2026-10-09 動画生成パイプラインとGitHub Actions構造の確定

### 1. 動画生成の自動化パイプライン（4つのYAMLワークフロー）
`ryubo-style` リポジトリの `.github/workflows/` 配下に配置された4つのYAMLファイルが連携し、原稿から最終ポータル更新までを全自動で実行するバトンリレー構造を確立。

1. **`generate-images.yml`**
   - **意義:** 台本（`Film.*.md`）の更新を検知し、`generate_images.py` を起動。起承転結（4章×3コマ＝12コマ）の16:9静止画アセットを `assets/images/` へ自動出力・保存する。
2. **`generate-audio.yml`**
   - **意义:** 台本（`Film.*.md`）の更新を検知し、`generate_speech.py` を起動。劇中ボイス（Pattern A/B）の音声トラック（.mp3）を `assets/audios/` へ自動出力・保存する。
3. **`generate-movies.yml`**
   - **意義:** 画像・音声アセットの更新を検知し、`ffmpeg` 環境下で `generate_movies.py` を起動。12コマ画像と音声を結合し、完成動画（.mp4）を `assets/videos/` へ自動生成・保存する。
4. **`build.yml`**
   - **意義:** すべてのアセットおよびスクリプト（`scripts/built.py`）の更新を受け、最終工程として `index.html`（シアターポータル）を再構築して公開・投射する。

### 2. ルート直下実行スクリプトの統一
ワークフローから呼び出される以下の3つの実働Pythonスクリプトを `ryubo-style` のルート直下に配置・一括管理する。
- `generate_images.py`（12コマ16:9画像生成）
- `generate_speech.py`（音声トラック生成）
- `generate_movies.py`（16:9動画結合生成）

### 3. ファイル退避・整理ルール
- 旧バージョンのファイル（`Film.2026.10.08.AM.md` 等）は、直接削除・滅失させるのではなく、`built.py` や手動操作によって必ず `.trash/` フォルダへ移動・保持させ、思考のあゆみと安全性を担保すること。

---

## 2026-10-09 画像・音声・動画の完全自動生成パイプラインの確立

### 1. マルチメディア全自動生成スクリプト群の導入
`ryubo-style` リポジトリのルート直下に以下の実働スクリプトおよび依存定義を配置し、高度なマルチメディア自動生成を実現。
- **`requirements.txt`**: `gtts`（音声合成）, `requests`（画像取得）, `Pillow`（画像処理）, `moviepy`（動画結合）の各外部ライブラリを指定。
- **`generate_images.py`**: 台本内容をもとにプロンプト（指示文）を自動構築し、API経由で16:9シネマティック画像を自動調達・保存。
- **`generate_speech.py`**: シナリオテキストを解析し、gTTSを用いて自然な日本語音声トラック（.mp3）を自動合成。
- **`generate_movies.py`**: 生成された12コマの画像（各15秒）と音声トラックを MoviePy を用いて結合し、音声付き完成動画（.mp4）をレンダリング。

### 2. GitHub Actions ワークフローの刷新
`.github/workflows/` 配下の各 YAML 設定ファイル（`generate-images.yml`, `generate-audio.yml`, `generate-movies.yml`, `build.yml`）に `requirements.txt` の自動インストール処理を組み込み、クラウド上での一連の全自動バトンリレーを完全に安定化。

### 3. シアターポータルへの自動投旗
最終工程の `build.yml`（スクリプト `scripts/built.py`）により、生成された全アセット（画像・音声・動画）を束ねた最新のポータル画面（`index.html`）が GitHub Pages（targetter009.com）へ自動デプロイ・公開される仕組みを維持。

---

## 2026-10-09 マルチメディア生成プロセスの「マネージャー方式（manager.py）」への一本化

### 1. 統括マネージャー `manager.py` の導入とエラーハンドリング
個別スクリプトの乱立や手動修正によるミスコーディングを防ぐため、画像生成・音声合成・動画結合の全プロセスを安全に統括・例外処理（エラートラップ）する司令塔として **`manager.py`** をルート直下に導入。
- 各ステップ（Image Generation, Speech Generation, Movie Generation）を順次安全に呼び出し、万が一エラーが発生した際もトレースを容易化。

### 2. GitHub Actions ワークフローの集約と整理
- 旧来の個別ワークフロー（`generate-images.yml`, `generate-audio.yml`, `generate-movies.yml`）は整理の上で `.trash/` へ安全に退避。
- 代わりに、`manager.py` をワンストップで実行・コミットする統合ワークフロー **`manager-workflow.yml`** へ刷新。

### 3. シアターポータル投射（Build Theater Web Portal）との連携維持
- 生成された全マルチメディアアセットは最終工程の `build.yml`（スクリプト `scripts/built.py`）へ引き渡され、従来通りポータル画面（`index.html`）を構築して GitHub Pages へ自動公開。
- `pages-build-deployment` は GitHub Pages の公式デプロイ基板として引き続き自動稼働。

---


