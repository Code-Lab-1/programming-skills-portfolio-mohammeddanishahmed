def make_shirt(size='medium', message='sir usman is great!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='large')
make_shirt('small', 'i love loops.')