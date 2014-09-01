from app import app
host = "158.119.175.221"
port = 5000
# if __name__ == '__main__':
#     app.run(host='158.119.175.221', debug=True)

from flask import Flask

if __name__ == '__main__':
    # Relevant documents:
    # http://werkzeug.pocoo.org/docs/middlewares/
    # http://flask.pocoo.org/docs/patterns/appdispatch/
    from werkzeug.serving import run_simple
    from werkzeug.wsgi import DispatcherMiddleware
    # Load a dummy app at the root URL to give 404 errors.
    # Serve app at APPLICATION_ROOT for localhost development.
    app.config['DEBUG'] = True
    application = DispatcherMiddleware(Flask('dummy_app'), {
        app.config['APPLICATION_ROOT'] : app,
    })
    run_simple(host, port, application, use_reloader=True)
