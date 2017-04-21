sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
cp /home/box/web/etc/hello.py /home/box/etc/hello.py
sudo .ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py
