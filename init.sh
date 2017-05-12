sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
#mkdir /home/box/etc
#cp /home/box/web/etc/hello.py /home/box/etc/hello.py
#cp /home/box/web/etc/ask.py /home/box/etc/ask.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
git config --global user.email "struk@yandex.ru"
git config --global user.name "struk77"
sudo ./ask/manage.py makemigrations
sudo ./ask/manage.py migrate
sudo /etc/init.d/nginx restart
sudo apt-get update
sudo apt-get -y install lynx mc 
sudo gunicorn -c /home/box/web/etc/ask.py ask.wsgi:application --pythonpath='/home/box/web/ask/' &
#sudo /etc/init.d/mysql start
