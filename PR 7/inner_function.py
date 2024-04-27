def outer_func(who):
    who = who

    def inner_func():
        print(f"Hello, {who}")
    inner_func()


outer_func("Omi!")
