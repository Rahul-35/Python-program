#INPUT NUMBER OF EVEN NUMBERS
def print_error_messages():
    print('Invalid number, please enter a positive number')
    exit()
try:
    n=int(input('Amount: '))
except ValueError:
  print_error_messages()
start=0
if n < 0:
        print_error_messages()
for i in range(1,n+1):
        start=start+2
        print(start)

