1、使用场景：
    1.web微服务

2、python2.7安装
    sudo pip install --upgrade pip 10.0.1 -> 18.1
    pip --version = 18.1
    pip install tornado

    验证
    error: Cannot uninstall 'six'.
    It is a distutils installed project and thus we cannot accurately determine
    which files belong to it which would lead to only a partial uninstall.
    sudo pip install six --upgrade --ignore-installed six
    sudo pip install --user pyspider  #环境报错
    sudo easy_install -U setuptools
    sudo pip install ipython

3、pip安装
    sudo easy_install pip       //这样会安装在系统自带的python2.7的路径下
    curl https://bootstrap.pypa.io/get-pip.py | python3
    ln -s /Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 /usr/local/bin/pip3

    python3.6安装
    sudo pip3 --default-timeout=100 install -U tornado
    sudo pip3 install ipython

    python3     //python登录方式
    import tornado
    tornado.version -> 5.1.1

    ipython    //ipython登录方式
    import tornado
    tornado.version -> 5.1.1

    pip查看已经安装的包
    pip freeze

4、软链接
    1.查看软链：ls -lih /usr/local/bin/ |grep python3
    2.修改软链接：ln –snf
    3.创建
    find / -name ipython3
    ln -s /Library/Frameworks/Python.framework/Versions/3.6/bin/ipython3 /usr/local/bin/ipython3
    ln -s /usr/local/bin/ipython3 /usr/local/bin/ipython

    sudo ln -nsf  /Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 /usr/local/bin/pip

    sudo ln -nsf /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /usr/local/bin/python

    vim ~/.bash_profile
    #python
    alias python='/usr/local/bin/python'

    source ~/.bash_profile

5、tornado
    http://127.0.0.1:8888           //helloworld
    http://127.0.0.1:8888/500       //500error
    http://127.0.0.1:8887/sleep     //异步