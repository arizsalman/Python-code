"""
**kwargs Keyword Arguments
Multiple argument ko dictionary me accept ya  convert karta he 
"""
def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}= {v}')


show_info(name="Ariz", age=23, city="Karachi")
