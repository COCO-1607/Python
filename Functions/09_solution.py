# generate a function that yields even numbers up to a specified limit.

def even_generator(limit):
    """Yield even numbers up to the specified limit."""
    for num in range(2, limit + 1, 2):
        yield num

for num in even_generator(10):
    print(num)