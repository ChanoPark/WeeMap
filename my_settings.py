"""#로컬에서 사용할 때!!
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'capstone',
        'USER' : 'root',
        'PASSWORD' : '451200',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}
"""   #AWS 배포용
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'capstone',
        'USER' : 'admin',
        'PASSWORD' : '77229680',
        'HOST' : 'capstone-db.ctghf43fhth2.ap-northeast-2.rds.amazonaws.com',
        'PORT' : '3306',
        'OPTIONS' : {
            'init_command' : 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

SECRET_KEY = 'django-insecure-=0=f$aunail)fq3u(8l=4+dcrvlzt6+59u-sbm#)ej^#i2=1cw'
