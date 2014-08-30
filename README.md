Add the following to apache2.conf

```apache
<VirtualHost *:80>
	ServerName myapp.local
    WSGIDaemonProcess myapp user=anthony group=anthony threads=5
    WSGIScriptAlias / /var/www/myapp/myapp.wsgi

    <Directory /var/www/myapp>
        WSGIProcessGroup myapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```