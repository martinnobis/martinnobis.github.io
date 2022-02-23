import os

import jinja2

OUTPUT_DIR = '.'

def main():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        autoescape=jinja2.select_autoescape()
    )

    template = env.get_template("index.html.j2")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(f'{OUTPUT_DIR}/index.html', 'w') as f:
        f.write(template.render())

if __name__ == '__main__':
    main()
