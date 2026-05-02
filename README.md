{# Моё Flask-приложение} - Было использовано для Д/З.

## Лабораторная работа по работе с docker

Работа посвящена изучению технологии работы с контейнерами

## Задание лабораторной работы

Настраиваем наше окружение для дальнейшей работы:
```bash
$ export GITHUB_USERNAME=<имя_пользователя>
$ export GIST_TOKEN=<сохраненный_токен>
$ alias edit=<nano|vi|vim|subl>
```

Клонируем данные прошлой работы в эту:
```sh
$ git clone https://github.com/${GITHUB_USERNAME}/lab06 projects/lab_docker
$ cd projects/lab_docker
$ git remote remove origin
$ git remote add origin https://github.com/${GITHUB_USERNAME}/lab_docker
```

Производим установку `Docker`:
```sh
# Debian
$ sudo apt-get update
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
> Но появилась некоторые проблемы после второй команды...

<details><summary>Ошибки после второй команды</summary>
  
```sh
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)      
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)       
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)...Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 3562 (unattended-upgr)       
Reading package lists... Done                                                                                       
Building dependency tree... Done
Reading state information... Done
Package docker-ce is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

Package docker-ce-cli is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'docker-ce' has no installation candidate
E: Package 'docker-ce-cli' has no installation candidate
E: Unable to locate package containerd.io
E: Couldn't find any package by glob 'containerd.io'
E: Unable to locate package docker-buildx-plugin
E: Unable to locate package docker-compose-plugin
```
</details>


> Поэтому пришлось пойти иным путём, где сначала я останавливаю автоматические обновления через `sudo systemctl stop unattended-upgrades`. Потом удаляю блокировочные файлы с помощью `sudo rm /var/lib/dpkg/lock-frontend /var/lib/dpkg/lock /var/cache/apt/archives/lock 2>/dev/null`. Затем также обновляю списки пакетов через `sudo apt update`. Устанавливаю команду `curl` через `sudo apt install -y curl`, чтобы вскоре смог скачать скрипт установки `Docker` через `curl -fsSL https://get.docker.com -o get-docker.sh`. Теперь следует произвести запуск установки `Docker` через `sudo sh get-docker.sh`.

<details><summary>Вывод скачивания</summary>
  
```sh
# Executing docker install script, commit: 2687d91ddeb3bd6aeae37a90947761efdee87030
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install ca-certificates curl >/dev/null
+ sh -c install -m 0755 -d /etc/apt/keyrings
+ sh -c curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" -o /etc/apt/keyrings/docker.asc
+ sh -c chmod a+r /etc/apt/keyrings/docker.asc
+ sh -c echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu noble stable" > /etc/apt/sources.list.d/docker.list
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras docker-buildx-plugin docker-model-plugin >/dev/null
Using systemd to manage Docker service
+ sh -c systemctl enable --now docker.service 2>/dev/null
INFO: Docker daemon enabled and started

+ sh -c docker version
Client: Docker Engine - Community
 Version:           29.4.2
 API version:       1.54
 Go version:        go1.26.2
 Git commit:        055a478
 Built:             Fri May  1 10:24:01 2026
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          29.4.2
  API version:      1.54 (minimum version 1.40)
  Go version:       go1.26.2
  Git commit:       d329809
  Built:            Fri May  1 10:24:01 2026
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.2.3
  GitCommit:        77c84241c7cbdd9b4eca2591793e3d4f4317c590
 runc:
  Version:          1.3.5
  GitCommit:        v1.3.5-0-g488fc13e
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

================================================================================

To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.


To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the 'Docker daemon attack surface'
         documentation for details: https://docs.docker.com/go/attack-surface/

================================================================================
```
</details>

> Чтобы пользователь, то есть я, смог пользоваться `Docker`, нужно добавить его в группу через `sudo usermod -aG docker $USER`, следом активируя все изменения с помощью `newgrp docker`. Наконец можно всё проверить, для начала запустив `docker --version`, получая:
```sh
Docker version 29.4.2, build 055a478
```
> И чтобы уже наверняка используем `docker run hello-world`:
```sh
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:f9078146db2e05e794366b1bfe584a14ea6317f44027d10ef7dad65279026885
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
> Теперь можно приступать к выполнению следующих частей лабораторной работы.


Создаём необходимые для работы файлы:
```sh
$ cat >> main.py <<EOF
print("Hello, Docker!")
EOF
```
```sh
$ cat >> requirements.txt <<EOF
flask
requests
EOF
```
```sh
$ cat >> Dockerfile <<EOF
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
EOF
```

Осуществляем сборку и запуск:
```sh
$ docker build -t lab-docker .
$ docker run --rm -it lab-docker
```
Где после первой команды получаем:
```sh
[+] Building 128.5s (11/11) FINISHED                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                              0.1s
 => => transferring dockerfile: 251B                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                1.9s
 => [internal] load .dockerignore                                                                                 0.1s
 => => transferring context: 2B                                                                                   0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13c  7.0s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13c  0.1s
 => => sha256:ea56f685404adf81680322f152d2cfec62115b30dda481c2c450078315beb508 251B / 251B                        0.4s
 => => sha256:fc74430849022d13b0d44b8969a953f842f59c6e9d1a0c2c83d710affa286c08 13.88MB / 13.88MB                  2.4s
 => => sha256:b3ec39b36ae8c03a3e09854de4ec4aa08381dfed84a9daa075048c2e3df3881d 1.29MB / 1.29MB                    1.0s
 => => sha256:38513bd7256313495cdd83b3b0915a633cfa475dc2a07072ab2c8d191020ca5d 29.78MB / 29.78MB                  5.1s
 => => extracting sha256:38513bd7256313495cdd83b3b0915a633cfa475dc2a07072ab2c8d191020ca5d                         0.8s
 => => extracting sha256:b3ec39b36ae8c03a3e09854de4ec4aa08381dfed84a9daa075048c2e3df3881d                         0.1s
 => => extracting sha256:fc74430849022d13b0d44b8969a953f842f59c6e9d1a0c2c83d710affa286c08                         0.6s
 => => extracting sha256:ea56f685404adf81680322f152d2cfec62115b30dda481c2c450078315beb508                         0.1s
 => [internal] load build context                                                                                 0.2s
 => => transferring context: 525.25kB                                                                             0.1s
 => [2/6] WORKDIR /app                                                                                            0.2s
 => [3/6] RUN apt-get update && apt-get install -y     build-essential                                           86.9s
 => [4/6] COPY requirements.txt .                                                                                 0.2s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                      6.6s 
 => [6/6] COPY . .                                                                                                0.3s 
 => exporting to image                                                                                           24.9s 
 => => exporting layers                                                                                          20.8s 
 => => exporting manifest sha256:48082c58b253bf2861cab607dcd4d496df9a9183f6a335091c6109aac2e2ac0e                 0.0s 
 => => exporting config sha256:fb8efaa4e280e559d46390e9d33c001239035f9e31418047ce2df4781c17c3c9                   0.0s 
 => => exporting attestation manifest sha256:58c0e53949d0198cbfe76138b8a7d4b7e9a61ceb8494b0003940bc2de5d2d0c9     0.0s 
 => => exporting manifest list sha256:2f61ebac0f4a0bc0d035422b7644529d4a5dd0ad170ce1403fb11c31eb6f4f39            0.1s
 => => naming to docker.io/library/lab-docker:latest                                                              0.0s
 => => unpacking to docker.io/library/lab-docker:latest                                                           3.8s
```
А после второй команды:
```sh
Hello, Docker!
```

### Docker compose

Создаём ещё один файл, который уже запустит несколько контейнеров одновременно:
```sh
$ cat >> docker-compose.yml <<EOF
ersion: '3.8'

services:
  app:
    build: . 
    container_name: lab_docker
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DB_HOST=${DB_HOST}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_NAME=${DB_NAME}

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${DB_ROOT_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
EOF
```

После следует создать специальный `.env` файл, где будут храниться наши переменные для `docker-compose.yml`, не забывая также добавить этот файл в `.gitignore` для безопасности. Теперь производим запуск всех контейнеров: 
```sh
$ docker compose up --build
```

<details><summary>Итоговый вывод</summary>
  
```sh
WARN[0000] /home/user1/bashkirgreg/workspace/projects/lab_docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 1.8s (13/13) FINISHED                                                                                     
 => [internal] load local bake definitions                                                                        0.0s
 => => reading from stdin 552B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                              0.1s
 => => transferring dockerfile: 251B                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                0.8s
 => [internal] load .dockerignore                                                                                 0.1s
 => => transferring context: 2B                                                                                   0.0s
 => [1/6] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13c  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13c  0.1s
 => [internal] load build context                                                                                 0.2s
 => => transferring context: 526.20kB                                                                             0.1s
 => CACHED [2/6] WORKDIR /app                                                                                     0.0s
 => CACHED [3/6] RUN apt-get update && apt-get install -y     build-essential                                     0.0s
 => CACHED [4/6] COPY requirements.txt .                                                                          0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt                                               0.0s
 => [6/6] COPY . .                                                                                                0.1s
 => exporting to image                                                                                            0.4s
 => => exporting layers                                                                                           0.2s
 => => exporting manifest sha256:bfae2b7cc5c96e473f58cb970232b1b70bf096aa716dea96da2c598a5f4443c3                 0.0s
 => => exporting config sha256:5619abe7c8853c77859b0fad6fa7858ae0b2cc5eb46b24ee9f357ee78c109871                   0.0s
 => => exporting attestation manifest sha256:6a501c2d88279d0247a05920080a42b4d9ef456dd8ed543fbcdee1245415b5f8     0.0s
 => => exporting manifest list sha256:57a85afa0502d9ad96b69af058907c97ecf150a7c2c84f7b99d699ada117a567            0.0s
 => => naming to docker.io/library/lab_docker-app:latest                                                          0.0s
 => => unpacking to docker.io/library/lab_docker-app:latest                                                       0.0s
 => resolving provenance for metadata file                                                                        0.0s
[+] up 5/5
 ✔ Image lab_docker-app       Built                                                                                1.9s
 ✔ Network lab_docker_default Created                                                                              0.1s
 ✔ Volume lab_docker_db_data  Created                                                                              0.0s
 ✔ Container mysql_db         Created                                                                              0.2s
 ✔ Container lab_docker       Created                                                                              0.1s
Attaching to lab_docker, mysql_db
Container mysql_db Waiting 
mysql_db  | 2026-05-02 09:15:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-05-02 09:15:17+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_db  | 2026-05-02 09:15:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-05-02 09:15:18+00:00 [Note] [Entrypoint]: Initializing database files
mysql_db  | 2026-05-02T09:15:18.097259Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-05-02T09:15:18.111801Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.46) initializing of server in progress as process 78
mysql_db  | 2026-05-02T09:15:18.161217Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-05-02T09:15:19.365888Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-05-02T09:15:21.237364Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql_db  | 2026-05-02 09:15:24+00:00 [Note] [Entrypoint]: Database files initialized
mysql_db  | 2026-05-02 09:15:24+00:00 [Note] [Entrypoint]: Starting temporary server
mysql_db  | 2026-05-02T09:15:25.009365Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-05-02T09:15:25.010615Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 118
mysql_db  | 2026-05-02T09:15:25.055661Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-05-02T09:15:25.708162Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-05-02T09:15:26.157663Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db  | 2026-05-02T09:15:26.161402Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db  | 2026-05-02T09:15:26.171579Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db  | 2026-05-02T09:15:26.225353Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql_db  | 2026-05-02T09:15:26.226184Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql_db  | 2026-05-02 09:15:26+00:00 [Note] [Entrypoint]: Temporary server started.
mysql_db  | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leapseconds' as time zone. Skipping it.
Container mysql_db Healthy 
lab_docker  | Hello, Docker!
lab_docker exited with code 0
mysql_db    | Warning: Unable to load '/usr/share/zoneinfo/tzdata.zi' as time zone. Skipping it.
mysql_db    | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql_db    | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql_db    | 2026-05-02 09:15:31+00:00 [Note] [Entrypoint]: Creating database mydb
mysql_db    | 2026-05-02 09:15:31+00:00 [Note] [Entrypoint]: Creating user myuser
mysql_db    | 2026-05-02 09:15:31+00:00 [Note] [Entrypoint]: Giving user myuser access to schema mydb
mysql_db    | 
mysql_db    | 2026-05-02 09:15:31+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql_db    | 2026-05-02T09:15:31.557389Z 14 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.46).
mysql_db    | 2026-05-02T09:15:34.993262Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.46)  MySQL Community Server - GPL.
mysql_db    | 2026-05-02 09:15:35+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql_db    | 
mysql_db    | 2026-05-02 09:15:35+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql_db    | 
mysql_db    | 2026-05-02T09:15:35.838841Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db    | 2026-05-02T09:15:35.839934Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 1
mysql_db    | 2026-05-02T09:15:35.863425Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db    | 2026-05-02T09:15:36.528606Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db    | 2026-05-02T09:15:36.791607Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db    | 2026-05-02T09:15:36.795595Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db    | 2026-05-02T09:15:36.801559Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db    | 2026-05-02T09:15:36.827842Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
mysql_db    | 2026-05-02T09:15:36.828011Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
```

</details>

Теперь для надёжности останавливаем весь процесс через `docker compose down`:
```sh
WARN[0000] /home/user1/bashkirgreg/workspace/projects/lab_docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] down 3/3
 ✔ Container lab_docker       Removed                                                                              0.0s
 ✔ Container mysql_db         Removed                                                                              1.3s
 ✔ Network lab_docker_default Removed                                                                              0.3s
```

## Домашнее задание

В репозитории приведен код web-приложения, которое сохраняет в БД введенную информацию о задаче - ее имя.

## Часть I. Docker

1. Добавьте в код Dockerfile, который позволит запустить web-приложение с исходным кодом в каталоге app/ через docker.
2. Выполните запуск контейнера с этим приложением.
3. Скопируйте из консоли в каталог /home/ контейнера файл README.md.
4. Подключитесь к терминалу контейнера с приложением в интерактивном режиме. Проверьте, что скопированный файл находится в нужном каталоге.
5. Выйдите из интерактивного режима.
6. Остановите контейнер с приложением.


## Часть II. Docker compose
1. Создайте файл docker-compose.yml таким образом, чтобы совместно с описанным в части 1 контейнером работала бы база данных mysql. Файл инициализации БД в каталоге db/init.sql. Также пропишите порт подключения к приложению. Например 5000.
2. Запустите связку web-приложение - БД.
3. Проверьте подключение к приложению через браузер. Сделайте снимок экрана.
4. Проверьте работу приложения через браузер.


## Выполнение первой части:

1)Через стандартный `cat` переношу все файлы в свою директорию, а также создаю новый `Dockerfile` для всего этого:
```sh
FROM python:3.11-alpine

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

2)Производим сборку через `docker build -t flask-app .`, а затем запуск через `docker run -d --name flask_container -p 5000:5000 flask-app`:

<details><summary>Сборка</summary>

```sh
[+] Building 16.2s (10/10) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                              0.1s
 => => transferring dockerfile: 210B                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.11-alpine                                             2.0s
 => [internal] load .dockerignore                                                                                 0.0s
 => => transferring context: 2B                                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.11-alpine@sha256:8b5bfdb1fd2d78aa94e21c4d61be52487693f54be7f1021647751  3.8s
 => => resolve docker.io/library/python:3.11-alpine@sha256:8b5bfdb1fd2d78aa94e21c4d61be52487693f54be7f1021647751  0.1s
 => => sha256:fd8e41ac72776720a5ce79d8a0c66e75ae8d3d836cb15cc6ae0682b0b7999a11 248B / 248B                        0.3s
 => => sha256:ea923c2ed79ed2d7163aacc54686501cb3339215671be89b50b62814aeffb95c 16.02MB / 16.02MB                  2.5s
 => => sha256:5c671a5c7ab3e0fe7526f4ff0a233b54727a1f407035f414a73138d2b0886733 455.65kB / 455.65kB                1.0s
 => => sha256:6a0ac1617861a677b045b7ff88545213ec31c0ff08763195a70a4a5adda577bb 3.86MB / 3.86MB                    1.7s
 => => extracting sha256:6a0ac1617861a677b045b7ff88545213ec31c0ff08763195a70a4a5adda577bb                         0.5s
 => => extracting sha256:5c671a5c7ab3e0fe7526f4ff0a233b54727a1f407035f414a73138d2b0886733                         0.4s
 => => extracting sha256:ea923c2ed79ed2d7163aacc54686501cb3339215671be89b50b62814aeffb95c                         0.8s
 => => extracting sha256:fd8e41ac72776720a5ce79d8a0c66e75ae8d3d836cb15cc6ae0682b0b7999a11                         0.1s
 => [internal] load build context                                                                                 0.0s
 => => transferring context: 1.97kB                                                                               0.0s
 => [2/5] WORKDIR /app                                                                                            0.2s
 => [3/5] COPY app/requirements.txt .                                                                             0.2s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                      7.1s
 => [5/5] COPY app/ .                                                                                             0.2s 
 => exporting to image                                                                                            2.2s 
 => => exporting layers                                                                                           1.6s 
 => => exporting manifest sha256:9e8f480662ff3e8f9aab6db907fa53ef36d4ada0a389ec74b19abb645f25b0c6                 0.0s 
 => => exporting config sha256:741b9d566c59b8f684948f2b8bcce25880971c75c712108a5a5413fbedddbd91                   0.0s 
 => => exporting attestation manifest sha256:4991773a3bfc3782019174a87e24fed29d059cab9536bebd7cc114d9aa3cd7fa     0.0s 
 => => exporting manifest list sha256:0b9ed570ad5d081577e8685bf46ea76687010b66e06b3b597c392affed4c1512            0.0s
 => => naming to docker.io/library/flask-app:latest                                                               0.0s
 => => unpacking to docker.io/library/flask-app:latest                                                            0.4s
```

</details>

```sh
6a7238c23aee743da8a73154eb56631dabb1b3374cbeba7c6173283db70950f0
```

3)Удаляем старый `README.md` с отчётом прошлой работы, потом пишем `echo "# Моё Flask-приложение" > README.md` и `docker cp README.md flask_container:/home/`, получая:
```sh
Successfully copied 36B (transferred 2.05kB) to flask_container:/home/
```

4)Подключаемся к терминалу контейнера через `docker exec -it flask_container /bin/sh` и начинаем вводить команды для проверки, получая:
```sh
/app # ls -la /home/
total 12
drwxr-xr-x    1 root     root          4096 May  2 10:45 .
drwxr-xr-x    1 root     root          4096 May  2 10:45 ..
-rw-rw-r--    1 1000     982             36 May  2 10:45 README.md
/app # cat /home/README.md
# Моё Flask-приложение
/app # ls -la /app/
total 28
drwxr-xr-x    1 root     root          4096 May  2 10:28 .
drwxr-xr-x    1 root     root          4096 May  2 10:45 ..
drwxr-xr-x    2 root     root          4096 May  2 10:28 __pycache__
-rw-rw-r--    1 root     root           573 May  2 10:06 app.py
-rw-rw-r--    1 root     root           845 May  2 10:03 models.py
-rw-rw-r--    1 root     root            29 May  2 10:04 requirements.txt
drwxrwxr-x    2 root     root          4096 May  2 10:15 templates
/app # exit
```

5)Выходим оттуда через `exit`.

6)Останавливаем контейнер через `docker stop flask_container`, получая `flask_container`. На всякий случай проверяем через `docker ps`, наблюдая терминал, состоящий всего из одной строки `CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES`, что говорит нам о том, что работающих контейнеров нет.


## Выполнение второй части:

1)Создаём новый `docker-compose.yml`, проверяя заодно все переменные из нашей давней папки `.env` для надёжности:
```sh
services:
  web:
    build: .
    container_name: flask_app
    ports:
      - "5000:5000"
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DB_HOST=${DB_HOST}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_NAME=${DB_NAME}

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_HOST: '%'
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
      - ./db:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-p${DB_ROOT_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

2)Сначала удаляем старые данные через `docker compose down -v`, а только затем запускаем всё через `docker compose up --build`.
<details><summary>Итоговая сборка</summary>

```sh
[+] Building 1.8s (12/12) FINISHED                                                                                     
 => [internal] load local bake definitions                                                                        0.0s
 => => reading from stdin 552B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                              0.0s
 => => transferring dockerfile: 210B                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.11-alpine                                             0.9s
 => [internal] load .dockerignore                                                                                 0.0s
 => => transferring context: 2B                                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.11-alpine@sha256:8b5bfdb1fd2d78aa94e21c4d61be52487693f54be7f1021647751  0.1s
 => => resolve docker.io/library/python:3.11-alpine@sha256:8b5bfdb1fd2d78aa94e21c4d61be52487693f54be7f1021647751  0.1s
 => [internal] load build context                                                                                 0.1s
 => => transferring context: 204B                                                                                 0.0s
 => CACHED [2/5] WORKDIR /app                                                                                     0.0s
 => CACHED [3/5] COPY app/requirements.txt .                                                                      0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                               0.0s
 => CACHED [5/5] COPY app/ .                                                                                      0.0s
 => exporting to image                                                                                            0.3s
 => => exporting layers                                                                                           0.0s
 => => exporting manifest sha256:586409bcf495c7901ee3d70a7f2b84ead0a256d0cd37267668f490a415cd77ac                 0.0s
 => => exporting config sha256:18d9a8156d5beff33dbb307dece1820a4ac657b52748eceafc42914d3189929f                   0.0s
 => => exporting attestation manifest sha256:8750a2546de8e434dd6e37f19e32bb9b2599b7d7707a49423975946ee0e4b087     0.1s
 => => exporting manifest list sha256:3ac19e9fa8f90800ea75c881bf3091115ef37e09ed68b8d08c8536467243bffd            0.0s
 => => naming to docker.io/library/lab_docker-web:latest                                                          0.0s
 => => unpacking to docker.io/library/lab_docker-web:latest                                                       0.1s
 => resolving provenance for metadata file                                                                        0.1s
[+] up 5/5
 ✔ Image lab_docker-web       Built                                                                                1.8s
 ✔ Network lab_docker_default Created                                                                              0.2s
 ✔ Volume lab_docker_db_data  Created                                                                              0.0s
 ✔ Container mysql_db         Created                                                                              0.2s
 ✔ Container flask_app        Created                                                                              0.2s
Attaching to flask_app, mysql_db
Container mysql_db Waiting 
mysql_db  | 2026-05-02 11:29:22+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-05-02 11:29:23+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_db  | 2026-05-02 11:29:23+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.46-1.el9 started.
mysql_db  | 2026-05-02 11:29:23+00:00 [Note] [Entrypoint]: Initializing database files
mysql_db  | 2026-05-02T11:29:23.484499Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-05-02T11:29:23.484580Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.46) initializing of server in progress as process 78
mysql_db  | 2026-05-02T11:29:23.496534Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-05-02T11:29:24.542668Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-05-02T11:29:25.992680Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql_db  | 2026-05-02 11:29:29+00:00 [Note] [Entrypoint]: Database files initialized
mysql_db  | 2026-05-02 11:29:29+00:00 [Note] [Entrypoint]: Starting temporary server
mysql_db  | 2026-05-02T11:29:30.031798Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db  | 2026-05-02T11:29:30.032974Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 118
mysql_db  | 2026-05-02T11:29:30.087534Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db  | 2026-05-02T11:29:30.899095Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db  | 2026-05-02T11:29:31.325387Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db  | 2026-05-02T11:29:31.328921Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db  | 2026-05-02T11:29:31.333588Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db  | 2026-05-02T11:29:31.374541Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
mysql_db  | 2026-05-02T11:29:31.387746Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
mysql_db  | 2026-05-02 11:29:31+00:00 [Note] [Entrypoint]: Temporary server started.
mysql_db  | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
mysql_db  | Warning: Unable to load '/usr/share/zoneinfo/leapseconds' as time zone. Skipping it.
Container mysql_db Healthy 
flask_app  |  * Serving Flask app 'app'
flask_app  |  * Debug mode: off
flask_app  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
flask_app  |  * Running on all addresses (0.0.0.0)
flask_app  |  * Running on http://127.0.0.1:5000
flask_app  |  * Running on http://172.18.0.3:5000
flask_app  | Press CTRL+C to quit
mysql_db   | Warning: Unable to load '/usr/share/zoneinfo/tzdata.zi' as time zone. Skipping it.
mysql_db   | Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
mysql_db   | Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
mysql_db   | 2026-05-02 11:29:36+00:00 [Note] [Entrypoint]: Creating database mydb
mysql_db   | 2026-05-02 11:29:36+00:00 [Note] [Entrypoint]: Creating user myuser
mysql_db   | 2026-05-02 11:29:36+00:00 [Note] [Entrypoint]: Giving user myuser access to schema mydb
mysql_db   | 
mysql_db   | 2026-05-02 11:29:36+00:00 [Note] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
mysql_db   | 
mysql_db   | 
mysql_db   | 2026-05-02 11:29:37+00:00 [Note] [Entrypoint]: Stopping temporary server
mysql_db   | 2026-05-02T11:29:37.074629Z 15 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.46).
mysql_db   | 2026-05-02T11:29:41.051964Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.46)  MySQL Community Server - GPL.
mysql_db   | 2026-05-02 11:29:41+00:00 [Note] [Entrypoint]: Temporary server stopped
mysql_db   | 
mysql_db   | 2026-05-02 11:29:41+00:00 [Note] [Entrypoint]: MySQL init process done. Ready for start up.
mysql_db   | 
mysql_db   | 2026-05-02T11:29:41.369921Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_db   | 2026-05-02T11:29:41.370882Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.46) starting as process 1
mysql_db   | 2026-05-02T11:29:41.388562Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_db   | 2026-05-02T11:29:42.035982Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_db   | 2026-05-02T11:29:42.408472Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_db   | 2026-05-02T11:29:42.410818Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_db   | 2026-05-02T11:29:42.424876Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_db   | 2026-05-02T11:29:42.464071Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
mysql_db   | 2026-05-02T11:29:42.476654Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.46'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
```

</details>

3)Проверяем статус через `docker ps`, получая:
```sh
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                   PORTS                                                    NAMES
effc73edfbd6   lab_docker-web   "python app.py"          8 minutes ago   Up 8 minutes             0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp              flask_app
541b7c82b939   mysql:8.0        "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes (healthy)   0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp, 33060/tcp   mysql_db
```

4)Осуществляем отправку `HTTP` запроса к приложению через `curl http://localhost:5000`, получая:
```sh
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>MVC App</title>
</head>
<body>
    <h1>Список из Базы Данных</h1>
    <ul>
        
            <li>Пример 1</li>
        
            <li>Пример 2</li>
        
    </ul>
</body>
</html>
```

5)Копируем ссылку `http://localhost:5000` из терминала и переходим по ней, наблюдая сайт с нашими данными:

<img width="560" height="209" alt="image" src="https://github.com/user-attachments/assets/8bde5d0d-981d-4858-96f4-73ec0d9d89d0" />

6)Останаливаем контейнеры командой `docker compose down` и ради интереса ещё раз пишем `curl http://localhost:500`:

<img width="606" height="277" alt="image" src="https://github.com/user-attachments/assets/d83239ee-a668-4320-b194-c543bd958a6a" />

7)Отправляем все наши файлы на `GitHub` с помощью стандартных команд `Git`.
