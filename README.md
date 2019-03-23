# Login

ログイン機能を Microservices 手法で開発、各構成を docker のコンテナにし、本番にデプロイ。
参考：http://docs.docker.jp/v1.10/swarm/swarm_at_scale/01-about.html

#構成：

- frontend:

  - vue.js(docker 化)

- webserver:

  - Nginx (docker 化)

- backend:

  - python-flask (docker 化)

- db:
  - mysql (docker 化)
