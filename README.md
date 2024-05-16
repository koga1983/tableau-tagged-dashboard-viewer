# 🏷️ Tableau Tagged Dashboard Viewer

このプロジェクトは、**Tableau Server Client (TSC)** を使用して、特定のタグでフィルタリングされたTableauダッシュボードを表示し、操作できるStreamlitアプリケーションです。

## 📋 必要条件

- Tableau Server または Tableau Online のアカウント
- API トークン
- Python 3.6以上
- Tableau Server Client ライブラリ
- Streamlit ライブラリ

## 🚀 インストール

1. リポジトリをクローンします:

    ```bash
    git clone https://github.com/koga1983/tableau-tagged-dashboard-viewer.git
    cd tableau-tagged-dashboard-viewer
    ```

2. 必要な Python パッケージをインストールします:

    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ 使用方法

1. `.streamlit/secrets.toml` ファイルを作成し、以下の情報を入力します:

    ```toml
    [tableau]
    token_name = "YOUR_TOKEN_NAME"
    personal_access_token = "YOUR_PERSONAL_ACCESS_TOKEN"
    site_id = "YOUR_SITE_ID"
    server_url = "YOUR_SERVER_URL"
    ```

2. アプリケーションを実行します:

    ```bash
    streamlit run app.py
    ```

アプリケーションが起動したら、タグを選択してフィルタリングされたダッシュボードを表示します。

## ⚙️ 機能

- **ダッシュボードの表示**: 特定のタグでフィルタリングされたTableauダッシュボードを表示します。
- **高さの調整**: 埋め込まれたダッシュボードの高さを調整できます。
- **キャッシュ**: データをキャッシュして、パフォーマンスを向上させます。

## 📜 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。[LICENSE](./LICENSE)

---

## 📚 詳細情報

- **Tableau Server Client ドキュメント**: [Tableau Server Client Library](https://tableau.github.io/server-client-python/docs/)
- **Tableau REST API ドキュメント**: [Tableau REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm)

## 💡 注意事項

このアプリケーションを実行する際には、適切なAPIトークンとアクセス権限が必要です。APIトークンの管理には十分注意してください。

---

### 🌟 **スターを付けてください！** 🌟

このリポジトリが役に立った場合は、スターを付けてください。あなたのサポートが私たちの励みになります！

[![GitHub Stars](https://img.shields.io/github/stars/koga1983/tableau-tagged-dashboard-viewer?style=social)](https://github.com/your-username/tableau-dashboard-portal/stargazers)
