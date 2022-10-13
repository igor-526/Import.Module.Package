from application.salary import *
from application.db.people import *
import datetime
import time
from progress.bar import *
if __name__ == '__main__':
    print(calculate_salary(5, 60))
    print(get_employees())
    print(datetime.datetime.now().strftime('%d.%m.%Y'))
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]

    bar = IncrementalBar('Countdown', max=len(mylist))
    for item in mylist:
        bar.next()
        print(bar.progress)
        time.sleep(0.3)

    bar.finish()

