# Django_CronJob
Here I have created Django cronjob by using django-crontab

# steps to implement Django cronjobs :

1. pip install django-crontab in terminal

2. add it to installed apps in django settings.py:
    INSTALLED_APPS = (
      'django_crontab',
      ...
     )

3. Now create a new method in cron.py which must be in your application folder that should be executed by cron every 5 minutes, f.e. in myapp/cron.py:

4.
    def my_scheduled_job():
      pass    
      #.. logic ..

5.  now add this to your settings.py:
    CRONJOBS = [
    ('*/5 * * * *', 'myapp.cron.my_scheduled_job'),
    ]

6.  you can also define positional and keyword arguments which let you call django management commands:

    CRONJOBS = [
      ('*/5 * * * *', 'myapp.cron.other_scheduled_job', ['arg1', 'arg2'], {'verbose': 0}),
      ('0   4 * * *', 'django.core.management.call_command', ['clearsessions']),
       # format 1
           ('0   0 1 * *', 'myapp.cron.my_scheduled_job', '>> /tmp/scheduled_job.log'),

       # format 2
            ('0   0 1 * *', 'myapp.cron.other_scheduled_job', ['myapp']),
            ('0   0 * * 0', 'django.core.management.call_command', ['dumpdata', 'auth'], {'indent': 4}, '> /home/john/backups/last_sunday_auth_backup.json'),
]
    ]

7. Inally run this command to add all defined jobs from CRONJOBS to crontab (of the user which you are running this command with):

      python manage.py crontab add
      
      - show current active jobs of this project:
          python manage.py crontab show
     
      - removing all defined jobs is straight forward:
          python manage.py crontab remove
