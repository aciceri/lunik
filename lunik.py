#!/usr/bin/env python3

from jinja2 import Template
from htmlmin import minify
from shutil import copy, rmtree
from boto3 import client
from os import mkdir
from pathlib import Path
from mimetypes import guess_type
import config

rmtree(config.generated_path)
mkdir(config.generated_path)

with open(f'{config.assets_path}/template.jinja2', 'r') as template_file:
    template = Template(template_file.read())

with open(f'{config.generated_path}/index.html', 'w') as html_file:
    html_file.write(minify(template.render(config.values)))

with open(f'{config.assets_path}/style.css', 'r') as css_file,\
     open(f'{config.generated_path}/style.css', 'w') as css_minified_file:
    css_minified_file.write(minify(css_file.read()))
    
for f in ('soviet.woff',
          'soviet.woff2',
          'particles.min.js',
          'particles.json',
          'moon.svg'):
    copy(f'{config.assets_path}/{f}', config.generated_path)

for movie in config.movies:
    copy(f'{config.images_path}/{movie["image"]}', config.generated_path)

aws_client = client('s3', aws_access_key_id=config.aws_access_key_id, aws_secret_access_key=config.aws_secret_access_key)

print(f'Uploading files in {config.generated_path} to "{config.aws_bucket_name}" aws bucket')
for f in Path(config.generated_path).rglob('*'):
    print(str(f))
    mimetype, _ = guess_type(f)
    args = {'ACL': 'public-read'}
    if mimetype:
        args['ContentType'] = mimetype
    aws_client.upload_file(str(f), config.aws_bucket_name, f.name, ExtraArgs=args)
