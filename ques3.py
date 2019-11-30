try:
    n = input()
    print ('Press Ctrl+C )
except KeyboardInterrupt:
    print ('KeyboardInterrupt')
except EOFError:
    print('End Of File')
except ValueError:
    print('Value Error Occured')
else:
    print ('No exception occurred')
