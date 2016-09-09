def eval_loop() :
    while True:
        n = raw_input('Input?\n:: ')
        if n == 'done':
            break
        else:
            result = eval(n)
            print result
    print result

eval_loop()
