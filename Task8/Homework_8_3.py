"""Честно списала, вроде разобралась, но тяжело"""


def type_logger():
    def logger(func):
        def decor(*argv, **kwargs):
            all_args = list(argv) + list(kwargs.values())
            print(", ".join([f"{x}:{type(x)}" for x in all_args]))

            for i in all_args:
                argument = func(all_args[i])
                print(f"{func.__name__}({all_args[i]}:{type(argument)})")

            one_arg = func(all_args[0])
            return one_arg
        return decor
    return logger


@type_logger()
def calc_cube(x):
    return x ** 3


if __name__ == "__main__":
    a = calc_cube(5, 6, 7, 8, 9, 1, 2, 3, val1=4, val2=5)
    print(a)
