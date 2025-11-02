readme_ja = Path("README_ja.md")

readme_ja_contents = """\

# Apo Blog - 本番デプロイ構成（Django + Gunicorn + Nginx + HTTPS）

Vultr 上に独自ドメイン（apo-cyber.com）でホストされた Django ブログプロジェクトです。

---

## ✅ 構成要素

- Django + Gunicorn + systemd
- Nginx でリバースプロキシ
- PostgreSQL（データベース復元済み）
- ドメイン： [apo-cyber.com](https://apo-cyber.com)
- HTTPS 対応（Let’s Encrypt）
- 静的ファイル対応（collectstatic 済み）
- `.env` による環境変数管理

---

## 🛠 セットアップ手順

### 1. パッケージインストール

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql git -y
```

---

### 2. プロジェクトクローン & 仮想環境構築

```bash
git clone git@github.com:apo-cyber/apo-blog.git
cd apo-blog
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. `.env` ファイル作成（例）

```env
SECRET_KEY="ここに生成したキー"
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,apo-cyber.com,www.apo-cyber.com
DB_NAME=apoblog
DB_USER=apobloguser
DB_PASSWORD=あなたのDBパスワード
DB_HOST=127.0.0.1
DB_PORT=5432
```

---

### 4. データベースマイグレーションと管理者作成

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

### 5. Gunicorn + systemd 設定

```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=apouser
Group=www-data
WorkingDirectory=/home/apouser/apo-blog
ExecStart=/home/apouser/apo-blog/venv/bin/gunicorn \\
          --access-logfile - \\
          --workers 3 \\
          --bind unix:/run/gunicorn.sock \\
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reexec
sudo systemctl enable gunicorn.socket
sudo systemctl start gunicorn.socket
```

---

### 6. Nginx 設定

```nginx
server {
    listen 80;
    server_name apo-cyber.com www.apo-cyber.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/apouser/apo-blog;
    }

    location /media/ {
        root /home/apouser/apo-blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/apo-blog /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

### 7. HTTPS 化（Let's Encrypt）

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d apo-cyber.com -d www.apo-cyber.com
```

---

### 8. 静的ファイルの収集

```bash
python manage.py collectstatic
```

---

## ✅ アクセス URL

- 🔒 https://apo-cyber.com
- 🔒 https://www.apo-cyber.com

---

## 🎉 お疲れ様でした！

この README_ja.md は、プロジェクトの構成・復元・本番公開に必要な情報を一通り網羅しています。
"""

readme_ja.write_text(readme_ja_contents)
"README_ja.md を作成しました！"
