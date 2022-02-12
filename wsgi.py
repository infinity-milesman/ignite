import os

from application import init_app

config_name = os.environ.get('FLASK_CONFIG','development')

app = init_app(config_name)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8089)