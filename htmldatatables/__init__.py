import os
from collections.abc import Iterable


DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEMPLATES = os.path.join(DIRECTORY, 'templates')


def load_template(path):
    with open(os.path.join(TEMPLATES, path)) as f:
        return f.read()


def render_html(template, table):
    return template.replace('{{table}}', table)


def generate_html_table(data):

    def generate_header_row(obj):
        cells = ''.join(f'<th>{x}</th>' for x in obj.keys())
        return f'<thead><tr>{cells}</tr></thead>'

    def generate_data_row(obj):
        cells = ''.join(f'<td>{x}</td>' for x in obj.values())
        return f'<tr>{cells}</tr>'

    assert isinstance(data, Iterable), 'data is not iterable'
    obj = next(iter(data))
    assert isinstance(obj, dict), 'data object is not dictionary'

    table = '<table id="table" class="display">'
    table += generate_header_row(obj)
    table += '<tbody>'
    for obj in data:
        table += generate_data_row(obj)
    table += '</tbody>'
    return table + '</table>'


HTMLTABLE = load_template('htmltable.html')
DATATABLES = load_template('datatables.html')


def render_table(data, datatables=False):
    html_table = generate_html_table(data)
    if not datatables:
        return render_html(HTMLTABLE, html_table)
    return render_html(DATATABLES, html_table)
