import datetime

def my_scheduled_job():
    a = str(datetime.datetime.now())
    f = open("/home/acquaint/Desktop/test.txt",'a')
    f.write(str(datetime.datetime.now())+"\n") # need to pass only strings while working
                                                # with files
    f.close()
    