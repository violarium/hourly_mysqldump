#!/usr/bin/env python

import os
import sys
import datetime

if len(sys.argv) != 4:
    print "Should be 3 arguments: user, password, destination folder"
    sys.exit(1)

now = datetime.datetime.now()

os.system("/usr/bin/mysqldump --events -u{0} -p{1} --all-databases > {2}/mysqldump_{3}.sql".format(sys.argv[1], sys.argv[2], sys.argv[3], now.strftime("%H")))
