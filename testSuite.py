import time
import subprocess
import os
import sys
from random import seed
from random import randint

MIN_SLEEP_IN_SECONDS = 1
MAX_SLEEP_IN_SECONDS = 60
operations = []

operations.append([['curl', '-s', '-X', 'POST', 'http://127.0.0.1:5000/add/effective-bassoon', '-d', 'https://github.com/joaopccosta/effective-bassoon.git'],['curl', '-s', 'http://127.0.0.1:5000/list/effective-bassoon'],['curl', '-s', 'http://127.0.0.1:5000/json/effective-bassoon']])
operations.append([['curl', '-s', '-X', 'POST', 'http://127.0.0.1:5000/add/Apollo-11', '-d', 'https://github.com/chrislgarry/Apollo-11.git'],['curl', '-s', 'http://127.0.0.1:5000/list/Apollo-11'],['curl', '-s', 'http://127.0.0.1:5000/json/Apollo-11']])
operations.append([['curl', '-s', '-X', 'POST', 'http://127.0.0.1:5000/add/spark', '-d', 'https://github.com/apache/spark.git'],['curl', '-s', 'http://127.0.0.1:5000/list/spark'],['curl', '-s', 'http://127.0.0.1:5000/json/spark']])
FNULL = open(os.devnull, 'w')
seed(1)
operationCount = 0
totalOperationsCount = int(sys.argv[1])
print(f" Performing {totalOperationsCount} operations...")
while operationCount < totalOperationsCount:
    randomRepository = operations[randint(0, len(operations) - 1)]
    randomOperation = randomRepository[randint(0, len(randomRepository)-1)]
    print(f"Running {randomOperation}")
    subprocess.run(randomOperation, stdout=FNULL)
    sleep = randint(MIN_SLEEP_IN_SECONDS, MAX_SLEEP_IN_SECONDS)
    print(f"Sleeping for {sleep}s...")
    time.sleep(sleep)
    operationCount += 1

print("DONE!")