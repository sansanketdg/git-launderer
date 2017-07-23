# import sys
import schedule
import time
#
# if len(sys.argv) == 1:
#     print("Only 1 argument")
# elif len(sys.argv) == 2:
#     print("Only 2 argument")
# else:
#     print("More than 2 arguments")

def job_1():
    print("I'm 1 min job - working...")

def job_10():
    print("I'm 10 min job - working...")

def job_1_hour():
    print("I'm 1 hour job - working...")

def job_10_30_job():
    print("I'm 10:30 job - working...")

schedule.every(1).minutes.do(job_1)
schedule.every(10).minutes.do(job_10)
schedule.every().hour.do(job_1_hour)
schedule.every().day.at("10:30").do(job_10_30_job)

while 1:
    schedule.run_pending()
    time.sleep(1)