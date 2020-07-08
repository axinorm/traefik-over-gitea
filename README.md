# Traefik over gitea

## Generate docker compose file

Install jinja2

```sh
virtualenv .venv
source .venv/bin/activate
pip install jinja2
```

Set environment variables

```sh
export TOG_SRV_OS=linux
export TOG_SRV_ARCH=arm
export TOG_URL_TRAEFIK=admin.example.com
export TOG_URL_GITEA=git.example.com
```

Generate file

```python
python3 generate_compose_file.py
```