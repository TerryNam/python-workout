def run_timing():
    number_of_runs = 0
    total_time = 0
    

    while True:
        timing = input('Enter 10km run time:').strip() #input 까지 ()로 감싸서, timimg value때문에 print문에서 오류 발생 

        if not timing:
            break

        number_of_runs +=1
        total_time += float(timing)

    print(f'Average of 10km run is {total_time/number_of_runs}mins')

run_timing()


       
       