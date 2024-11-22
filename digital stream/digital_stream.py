import random, shutil, sys, time

min_stream = 6
max_stream = 14
pause = 0.1
stream_chars = [0,1]

density = 0.02

width = shutil.get_terminal_size()[0]

width-=1

print("digital stream", "by sololiqht")
print("press CTRL+C to exit")

time.sleep(2)

try:
    columns= [0]*width
    while True:
        for i in range(width):
            if columns[i] == 0:
                if random.random() <= density:
                    columns[i] = random.randint(min_stream,max_stream)

            if columns[i] > 0:
                print(random.choice(stream_chars), end='')
                columns[i]-=1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(pause)
except KeyboardInterrupt:
    sys.exit
