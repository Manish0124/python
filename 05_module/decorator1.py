
def debug(func):
    def wraper(*args,**kwargs):
        
        args_value = ', '.join(str(args) for arg in args)

        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        
        print(f" calling: {func.__name__} with args {args_value} and kwars {kwargs_value} ")
        return func(*args,**kwargs)
    
    return wraper    


@debug
def greet(name , greet = "hello"):
    print(f"{greet}, {name}")


greet( "manish")