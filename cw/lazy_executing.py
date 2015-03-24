def make_lazy(f, *args, **kwargs):
    return lambda: f(*args, **kwargs)
