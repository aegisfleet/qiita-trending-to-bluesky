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

```
python main.py <ユーザーハンドル> <パスワード>
```

## 技術要素

このアプリケーションは以下の技術を使用しています。

- Python: メインのプログラミング言語
- BeautifulSoup: HTMLの解析
- requests: HTTPリクエスト
- g4f: GPTのクライアントライブラリ
- atproto: BlueskyのAPIクライアント

また、開発には以下を使用しています。

- [gpt4free](https://github.com/xtekky/gpt4free): 生成AIを無料で利用するためのライブラリ
- [リートン](https://wrtn.jp/): コード生成やテキスト生成に利用しているAIサービス
- [AWS CodeWhisperer](https://aws.amazon.com/jp/codewhisperer/): コード生成に使用しているAIツール

## マスコット

リートンで生成したマスコット画像。  
名前はまだ無い。

<img src="images\mascot.png" width="50%">