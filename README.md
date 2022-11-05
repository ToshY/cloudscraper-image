# 🖼️ Cloudscraper for images

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/ToshY/cloudscraper-image?sort=semver)
![Docker Hub repository](https://img.shields.io/badge/Docker%20Hub-t0shy%2Fcloudscraper--image-blue)
[![Pylint](https://github.com/ToshY/cloudscraper-image/actions/workflows/pylint.yml/badge.svg)](https://github.com/ToshY/cloudscraper-image/actions/workflows/pylint.yml/badge.svg)
[![Pip Audit](https://github.com/ToshY/cloudscraper-image/actions/workflows/security.yml/badge.svg)](https://github.com/ToshY/cloudscraper-image/actions/workflows/security.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)

A tiny [Falcon](https://github.com/falconry/falcon) app for requesting images
with [cloudscraper](https://github.com/VeNoMouS/cloudscraper) and returning the image data as a base64 string.

## Setup

You can choose to either follow the Docker route or plain (Python) route.

### 🐋 Docker

#### Pull or build

```shell
docker pull t0shy/cloudscraper-image:latest
# or
docker build -t t0shy/cloudscraper-image:latest --no-cache .
```

### 🐍 Plain

Install the requirements with `pip`.

```shell
pip install -r requirements.txt
```

## Run webserver

### 🐋 Docker

```shell
docker run -dit --name cloudscraper t0shy/cloudscraper-image:latest
```

> Note: You can remove the container after usage:
> ```shell
> docker rm -f cloudscraper
> ```

### 🐍 Plain

```shell
python setup.py
```

## 📨 Request

### 🐋 Docker

```shell
curl http://<container-ip>:8000/image?url=<encoded-url>
```

> Note: You can get the IP address of the container by running the following command:
> ```shell
> docker inspect --format "{{ .NetworkSettings.IPAddress }}" cloudscraper
> ```

### 🐍 Plain

```shell
curl http://127.0.0.1:8000/image?url=<encoded-url>
```

## 📬 Response

The response will be a base64 string. To test/verify if this data is correct, you can use tools
like [Base64.guru](https://base64.guru/converter/decode/image) to convert it back to an image.

## 🛠️ Contribute

To simplify development, a [`Taskfile.yml`](./Taskfile.yml) is included. While the usage is optional, Task simplifies
the
setup for your development environment. Installation guide for Task can be found
at [taskfile.dev/installation](https://taskfile.dev/installation/).

### Pre-commit

Setting up `pre-commit` code style & quality checks for local development.

```shell
pre-commit install
```

### Create container

```shell
task up
```

### Quality & Code Style

```shell
task check
```

### Code Style fix

```shell
task fix
```
