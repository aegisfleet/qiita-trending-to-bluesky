# Qiita Trending to Bluesky

Qiita Trending to Blueskyは、[Qiita](https://qiita.com/)におけるトレンド記事を自動的に要約し、Blueskyに投稿するアプリケーションです。  
このアプリケーションは、技術者コミュニティにおける最新のトレンドや話題を迅速にキャッチアップするために開発されました。

## 特徴

- Qiitaのトレンド記事を検出
- 記事の内容を要約
- 要約をBlueskyに自動投稿

このリポジトリで実行された結果はBlueskyの [デイリーQiitaトレンド](https://bsky.app/profile/dailyqiitatrends.bsky.social) に投稿されます。

## インストール

このプロジェクトをローカル環境で動かすには、次の手順を実行してください。

```bash
git clone https://github.com/aegisfleet/qiita-trending-to-bluesky.git
cd qiita-trending-to-bluesky
pip install -r requirements.txt
```

## 使用方法

アプリケーションを実行するには、以下のコマンドを使用します。

```text
python main.py <BlueSkyのユーザーハンドル> <BlueSkyのパスワード> <GeminiのAPIキー>
```

## 技術要素

このアプリケーションは以下の技術を使用しています。

- Python: メインのプログラミング言語
- beautifulsoup4: HTMLの解析
- requests: HTTPリクエスト
- google-generativeai: Gemini
- atproto: BlueskyのAPIクライアント

また、開発には以下を使用しています。

- [Gemini](https://ai.google.dev/gemini-api?hl=ja): Googleの生成AI API
- [リートン](https://wrtn.jp/): コード生成やテキスト生成に利用しているAIサービス
- [AWS CodeWhisperer](https://aws.amazon.com/jp/codewhisperer/): コード生成に使用しているAIツール

## 関連記事

- [Webスクレイピング×生成AI×SNSで新しい価値が生まれる？すべて無料でBOTを作った話](https://note.com/aegisfleet/n/nc8362f717cd9)

## 関連BOT

| カテゴリ | 名称 | 投稿時間 |
|---|---|---|
| リポジトリの内容を要約 | [デイリーGitHubトレンド](https://bsky.app/profile/dailygithubtrends.bsky.social) | 毎日20時 |
| リポジトリの内容を要約 | [デイリーHuggingFaceトレンド](https://bsky.app/profile/huggingfacetrends.bsky.social) | 毎日19時 |
| 記事の内容を要約 | [デイリーQiitaトレンド](https://bsky.app/profile/dailyqiitatrends.bsky.social) | 毎日7時 |
| 記事の内容を要約 | [デイリーZennトレンド](https://bsky.app/profile/dailyzenntrends.bsky.social) | 毎日6時/18時 |
| 記事の内容を要約 | [デイリーAIトレンド](https://bsky.app/profile/dailygenaitrends.bsky.social) | 毎日13時/16時 |
| 指標値のまとめと記事の要約 | [デイリーマーケットトレンド](https://bsky.app/profile/dailymarkettrends.bsky.social) | 6時/12時/15時/20時 |

## マスコット

リートンで生成したマスコット画像。  
名前はまだ無い。

<img src="images\mascot.png" width="50%">
