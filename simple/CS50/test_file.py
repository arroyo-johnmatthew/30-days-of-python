import pytest
from file import checkArgLen, checkFileNature

def test_few_arg():
    with pytest.raises(SystemExit):
        checkArgLen([''])
    with pytest.raises(SystemExit):
        checkArgLen(['hello.py'])

def test_many_arg():
    with pytest.raises(SystemExit):
        checkArgLen(['john', 'matthew', 'arroyo'])
    with pytest.raises(SystemExit):
        checkArgLen(['john', 'matthew', 'arroyo', 'john'])

def test_non_python_file():
    with pytest.raises(SystemExit):
        checkFileNature('test.txt')
    with pytest.raises(SystemExit):
        checkFileNature('test.px')

def test_non_existent_file():
    with pytest.raises(SystemExit):
        checkFileNature('test_files.py')