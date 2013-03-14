#!/usr/bin/env python

def main():
    indata = check_args()
    start = 2
    stop = 500000
    print '\nFactorizing values between:', start, 'and', stop
    if indata.mode == 's' or indata.mode == 'all':
        serial_mode(start, stop)
    if indata.mode == 'm' or indata.mode == 'all':
        multi_mode(start, stop)
    if indata.mode == 'i' or indata.mode == 'all':
        i_mode(start, stop)
   
def multi_mode(start, stop):
    print 'going multi'
    from multiprocessing import Pool
    pool = Pool(processes=4)
    result = pool.map(factorize, xrange(start, stop +1), chunksize = 100)
    print uniq_counter(result)
    
def serial_mode(start, stop):
    print 'going serial'
    uniq_dict = {}
    result = map(factorize, xrange(start, stop +1))
    print uniq_counter(result)

def i_mode(start, stop):
    from IPython.parallel import Client
    print 'going into i mode'
    c = Client()
    d = c[:]
    result = d.map(factorize, xrange(start, stop +1))
    print uniq_counter(result)
   
def uniq_counter(factor_list):
    uniq_dict = {}
    for factors in factor_list:
        uniqs = []
        for x in factors:         
            if x not in uniqs:
                uniqs.append(x)
            else:
                continue
        if len(uniqs) not in uniq_dict:
            uniq_dict[len(uniqs)] = 1
        else:
            uniq_dict[len(uniqs)] += 1
    return uniq_dict

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def check_args():
    import argparse
    parser = argparse.ArgumentParser(description='Tha Factorizer, now in serial, multi and ipython mode!')
    parser.add_argument('-mode',dest='mode',metavar='X',type=str,required=True,default='s',help='script can be run in serial(s), multi(m) or ipython mode, or you can rum them all(all)')
    indata = parser.parse_args()
    return indata

if __name__ == "__main__":
    main()