import model


def create():
    spravochnick = model.print_spravochnick()
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    for i in spravochnick:
        html += '  <p {}> {} </p>\n'\
            .format(style, i)
    html += '</body>\n</html>'

    with open('spravochnick.html', 'w') as page:
        page.write(html)

    return html
