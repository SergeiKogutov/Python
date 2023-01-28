import model


def create():
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}> spravochnick: {} </p>\n'\
        .format(style, model.print_spravochnick())
    html += '</body>\n</html>'

    with open('spravochnick.html', 'w') as page:
        page.write(html)

    return html
