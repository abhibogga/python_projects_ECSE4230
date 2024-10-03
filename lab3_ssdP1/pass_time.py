from time import perf_counter

sum = 0
sample = 1000000

for i in range(sample):
    start = perf_counter()
    for j in range(1):
        pass
    end = perf_counter()
    sum += end-start

avg = sum/sample
print(avg)


sum = 0
        sample = 1000000

        for i in range(sample):
            start = perf_counter()
            for j in range(1):
                pass
            end = perf_counter()
            sum += end-start

        avg = sum/sample
        print(avg)