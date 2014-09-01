Requires following python steps

  * virtualenv env
  * env/bin/pip install Flask Flask-HTTPAuth

Add the following to apache2.conf

```apache
<VirtualHost *:80>
    ServerName flask_app.local
    WSGIDaemonProcess flask_app user=anthony group=anthony threads=5
    WSGIScriptAlias / /var/www/flask_app/flask_app.wsgi
    WSGIPassAuthorization On

    <Directory /var/www/myapp>
        WSGIProcessGroup flask_app
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```
