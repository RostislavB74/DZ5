def get_data():
    for num in range(5):
        yield num
# #можна замінити на:
# def get_data():
#     yield from range(5): (edited)
