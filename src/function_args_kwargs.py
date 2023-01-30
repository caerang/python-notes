def print_args(*args):
    """
    몇 개의 인자를 받을 지 알 수 없을 때 사용한다.
    인자를 튜플로 넘겨 받는다.
    """
    print(type(args))
    print('args = ', args)
    for param in args:
        print(param)


def print_kwargs(**kwargs):
    """
    인자를 사전 형태로 넘겨 받을 때 사용한다.
    """
    print(type(kwargs))
    print(f'kwargs = {kwargs}')
    print(f'kwargs.keys() = {kwargs.keys()}')
    print(f'kwargs.values() = {kwargs.values()}')

    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')


if __name__ == '__main__':
    print_args('Team', 'Seoul', 'Korea')
    print_kwargs(Top='Top', Left=["Left", "Right", 1, 0.2], Right=1.2, Bottom=10)
