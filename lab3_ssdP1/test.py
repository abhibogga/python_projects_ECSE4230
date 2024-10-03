from time import perf_counter



size = 10

'''start = perf_counter()
for i in range(size)
  time.sleep(1)
end = perf_coutner()'''


start = perf_counter()
for i in range(size)
  for j in range(1890958): 
    pass
end = perf_coutner()

print((end-start)/size)
