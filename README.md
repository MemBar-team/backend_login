# login_api

ログイン機能を  Docker 化されたマイクロサービス・アプリケーション手法で開発、各構成を docker のコンテナにし、本番にデプロイ。

参考：http://docs.docker.jp/v1.10/swarm/swarm_at_scale/01-about.html

#構成：
- webserver:

  - Nginx (docker 化)

- frontend:

  - vue.js (docker 化)

- backend:

  - python-flask (docker 化)
     - pythone : 3.7.2
     - flask : 1.0.2
     - SQLAlchemy 1.3.1
     - Flask-HTTPAuth 3.2.4
    
- db:
  - mysql (docker 化)
