from app import create_app
from app.utils.resp_format import Success

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)