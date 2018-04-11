"""Module for flask server run."""
from base_run import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
