import pytest
from simple.CS50.FILEIO.file import check_arg_len, count_loc

def test_few_arg():
    with pytest.raises(SystemExit):
        check_arg_len([''])
    with pytest.raises(SystemExit):
        check_arg_len(['hello.py'])

def test_many_arg():
    with pytest.raises(SystemExit):
        check_arg_len(['john', 'matthew', 'arroyo'])
    with pytest.raises(SystemExit):
        check_arg_len(['john', 'matthew', 'arroyo', 'john'])

def test_non_python_files():
    with pytest.raises(SystemExit):
        count_loc("hello.txt")
    with pytest.raises(SystemExit):
        count_loc("hello.px")

def test_loc():
    assert count_loc("test_code.py") == 16
    assert count_loc("file.py") == 28
