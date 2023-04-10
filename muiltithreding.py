# Thread : A light weighted process..

import threading

import time
a=[2,3,4,5]

def square_val(a):
    for ele in a:
        time.sleep(0.2)
        print(ele**2)

def cube_val(a):
    for ele in a:
        time.sleep(0.3)
        print(ele**3)


t_before = time.time()
# square_val(a)

# cube_val(a)

t1 = threading.Thread(target=square_val,args=(a,))

t2 = threading.Thread(target=cube_val,args=(a,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Time taken",time.time()-t_before)