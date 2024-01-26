from blinker import Namespace

my_signals = Namespace()
user_logged_in = my_signals.signal('user_logged_in')


@user_logged_in.connect
def print_user_name(sender):
    # This line is executed when the signal is received.
    print(f"{sender} has logged in!")

@user_logged_in.connect
def print_use_hello(sender):
    # This line is executed when the signal is received.
    print(f"{sender} is saying hello!")

