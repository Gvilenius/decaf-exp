FUNCTION<Fibonacci.get>:
    _T1 = 2
    _T4 = (_T0 < _T1)
    if (_T4 == 0) branch _L1
    _T16 = 1
    return _T16
_L1:
    _T17 = 1
    _T20 = (_T0 - _T17)
    parm _T20
    _T21 = call FUNCTION<Fibonacci.get>
    _T22 = 2
    _T25 = (_T0 - _T22)
    parm _T25
    _T26 = call FUNCTION<Fibonacci.get>
    _T29 = (_T21 + _T26)
    return _T29

main:
    call _ReadInteger
    _T5 = 3
    parm _T5
    call FUNCTION<Fibonacci.get>
    return