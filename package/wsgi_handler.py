from aws_lambda_wsgi import environ as make_environ, start_response, encode_response
from app import app

def lambda_handler(event, context):
    env = make_environ(event, context)

    # Patch missing keys to prevent Flask KeyError
    if 'wsgi.url_scheme' not in env:
        env['wsgi.url_scheme'] = 'https'

    # Optional: fallback host (Flask will crash without it sometimes)
    if 'HTTP_HOST' not in env:
        env['HTTP_HOST'] = 'example.com'

    status = []
    headers = []

    def start_response(status_code, header_list):
        status.append(status_code)
        headers.extend(header_list)

    result = app(env, start_response)
    return encode_response(result)