def check_scope():
    def do_local():  # effect only inside function
        test = "local test"

    def do_non_local():  # effect on the test=default which make it change to test non local test
        nonlocal test
        test = "non local test"

    def do_global():  # effect outside of function check_scope
        global test
        test = "global test"

    test = "default"
    do_local()

    print("test values after do local:" + test)
    do_non_local()
    print("test values after do non local:" + test)
    do_global()
    print("test values after global test:" + test)


check_scope()
print("test values after main:" + test)
