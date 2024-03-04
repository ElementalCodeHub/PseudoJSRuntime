from utils import console,Promise
import time
def async_operation(resolve, reject):
    time.sleep(1)
    operation_successful = True
    if operation_successful:
        resolve('Promise resolved successfully')
    else:
        reject('Promise rejected with an error')

promise1 = Promise(async_operation)

# Handling the Promise
promise1.then(print).catch(print)

