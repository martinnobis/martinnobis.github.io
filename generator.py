import os

import jinja2

OUTPUT_DIR = 'public'

def main():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        autoescape=jinja2.select_autoescape()
    )

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for template_filename in os.listdir("templates"):
        if 'base' in template_filename:
            # you don't render the base template
            continue
        template = env.get_template(template_filename)

        rendered_filename = template_filename.strip(".j2")

        with open(f'{OUTPUT_DIR}/{rendered_filename}', 'w') as f:
            f.write(template.render())

if __name__ == '__main__':
    main()
