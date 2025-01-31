from inspect import getmodule


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getmodule(obj)
    }

if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)