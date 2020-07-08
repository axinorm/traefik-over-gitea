#!/usr/bin/python
import jinja2
import os

OS = os.getenv('TOG_SRV_OS')
ARCH = os.getenv('TOG_SRV_ARCH')
URL_TRAEFIK = os.getenv('TOG_URL_TRAEFIK')
URL_GITEA = os.getenv('TOG_URL_GITEA')
TEMPLATE_FILE = "docker-compose.yml.j2"

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(
  os=OS, 
  arch=ARCH, 
  url_traefik=URL_TRAEFIK, 
  url_gitea=URL_GITEA
)

file = open("./docker-compose.yml", "w+")
file.write(outputText)
file.close()