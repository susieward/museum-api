from main import main_bp
from flask import render_template, request
from api import ApiService
import requests

resources = ['object', 'person', 'exhibition', 'publication', 'gallery', 'spectrum', 'classification', 'century', 'color', 'culture', 'group', 'medium', 'period', 'place', 'technique', 'worktype', 'activity', 'site', 'video', 'image', 'audio', 'annotation']

def view_function(template, view_args):
    view_args.append()
    return render_template(template, )

@main_bp.route('/')
def index():
    return render_template('index.html', resources = resources)

@main_bp.route('/search')
def search():
    return render_template('search.html', resources = resources)

@main_bp.route('/api/search/<keyword>', methods=['GET'])
@main_bp.route('/api/search/<keyword>/<int:size>', methods=['GET'])
@main_bp.route('/api/search/<keyword>/<int:size>/<int:page>', methods=['GET'])
def load_search(keyword, size = None, page = None):
    data = ApiService().find_by_keyword(keyword, size, page)
    return data

#@main_bp.route('/search/<resource>/<query>', methods=['GET'])
#@main_bp.route('/search/<resource>/<query>/<int:size>', methods=['GET'])
#def get_search(resource, query, size = None):
#    data = ApiService().search(resource, query, size)
#    return render_template('page.html', data = data)

@main_bp.route('/experimental/<params>', methods=['GET'])
def experimental(params = None):
    if params:
        resource = f'experimental/{params}'
        data = ApiService().list(resource, size = None)
        return data
    else:
        data = ApiService().list('experimental/object', size = None)
        return data

@main_bp.route('/list/<resource>', methods=['GET'])
@main_bp.route('/list/<resource>/<int:size>', methods=['GET'])
def list_resource(resource, size = None):
    data = ApiService().list(resource, size)
    return render_template('page.html', data = data, resource = resource, resources = resources)

@main_bp.route('/find/<resource>/<id>', methods=['GET'])
def get_resource(resource, id):
    data = ApiService().get(resource, id)
    return render_template('result.html', data = data, resource = resource, id = id, resources = resources)

@main_bp.route('/api/images/<keyword>', methods=['GET'])
@main_bp.route('/api/images/<keyword>/<int:size>', methods=['GET'])
def get_images(keyword, size = None):
    data = ApiService().find_images_by_keyword(keyword, size)
    return data

@main_bp.route('/colors', methods=['GET'])
@main_bp.route('/colors/<int:size>', methods=['GET'])
def colors(size = None):
    data = ApiService().list('color', size)
    colors = format_color_data(data)
    return render_template('colors.html', colors = colors)

def format_color_data(data):
    colors = []
    for record in data['records']:
        color = { 'name': record['name'], 'hex': record['hex'] }
        colors.append(color)
    return colors
