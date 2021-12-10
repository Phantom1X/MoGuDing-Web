from app.cron.cron import cronMethod
from config import flaskConfig
from app.db.db import db
 
if __name__ == '__main__':
    #flaskConfig.scheduler.add_job(func=cronMethod.refreshJobs, trigger='cron', second='*/5', id='refresh')
    cronMethod.setJobs()
    flaskConfig.scheduler.start()

    # 启动网站
    flaskConfig.app.run(debug = flaskConfig.DEBUG, use_reloader=False)
