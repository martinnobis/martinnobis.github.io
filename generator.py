import jinja2

def main():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        autoescape=jinja2.select_autoescape()
    )

    template = env.get_template("index.html.j2")

    with open('public/index.html', 'w') as f:
        f.write(template.render())

if __name__ == '__main__':
    main()
