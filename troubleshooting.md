
# Installation

## Method 1

``` sh
$ sudo pip install opticspy
```

## Method 2

Download opticspy source file from [https://pypi.python.org/pypi/opticspy](https://pypi.python.org/pypi/opticspy) then
``` sh
$ python2.7 setup.py install
```

# Possible bugs

## Error when import unwrap
Opticspy use an [unwrap module](https://pypi.python.org/pypi/unwrap) for
unwraping phase. It works well.

You may get following error:
``` sh
[Errno 2] No such file or directory: '/Library/Python/2.7/site-packages/unwrap/__pycache__/_cffi__x8956f820xc1fce120.c'
```

Solution: Create a `__pycache__` folder in your python package directory
`/Library/Python/2.7/site-packages/unwrap/`
