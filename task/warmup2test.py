from task.warmup2 import one_line


def test_function_works_case():
    assert one_line('Hello world') == {'upperCase': 1,
                                       'lowerCase': 9}
