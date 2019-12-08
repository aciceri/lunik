from jinja2 import Template as jinjaTemplate
from htmlmin import minify
from shutil import copy, rmtree
from os import mkdir
from PIL import Image
import config


try:
    rmtree(config.generated_path)
except FileNotFoundError:
    pass

mkdir(config.generated_path)

with open(f'{config.assets_path}/template.jinja2', 'r') as template_file,\
     open(f'{config.generated_path}/index.html', 'w') as html_file:
    template = jinjaTemplate(template_file.read())
    html_file.write(minify(template.render(config.values)))

with open(f'{config.assets_path}/style.css', 'r') as css_file,\
     open(f'{config.generated_path}/style.css', 'w') as css_minified_file:
    css_minified_file.write(minify(css_file.read()))


for f in ('soviet.woff',
          'soviet.woff2',
          'particles.min.js',
          'particles.json',
          'moon.svg',
          'moon.ico'):
    copy(f'{config.assets_path}/{f}', config.generated_path)

for movie in config.movies:
    filename = movie['image'].split('.')[:-1][0]
    src = Image.open(f'{config.images_path}/{movie["image"]}')
    src.resize((config.img_width, int(config.img_width * src.height / src.width)))\
        .save(f'{config.generated_path}/{filename}.jpg')
