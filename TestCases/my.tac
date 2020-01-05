FUNCTION<Fibonacci.get>:
    _T1 = 2
    _T2 = 0
    _T3 = (_T1 == _T2)
    _T4 = (_T0 < _T1)
    if (_T4 == 0) branch _L1
    _T6 = 1
    _T5 = _T6
    _T8 = 2
    _T9 = 0
    _T10 = (_T8 == _T9)
    _T11 = (_T5 + _T8)
    _T7 = _T11
    _T13 = 0
    _T14 = (_T7 == _T13)
    _T15 = (_T5 * _T7)
    _T12 = _T15
    _T16 = 1
    return _T16
_L1:
    _T17 = 1
    _T18 = 0
    _T19 = (_T17 == _T18)
    _T20 = (_T0 - _T17)
    parm _T20
    _T21 = call FUNCTION<Fibonacci.get>
    _T22 = 2
    _T23 = 0
    _T24 = (_T22 == _T23)
    _T25 = (_T0 - _T22)
    parm _T25
    _T26 = call FUNCTION<Fibonacci.get>
    _T27 = 0
    _T28 = (_T26 == _T27)
    _T29 = (_T21 + _T26)
    return _T29

main:
    _T1 = 1
    _T0 = _T1
    _T3 = 3
    parm _T3
    _T4 = call FUNCTION<Fibonacci.get>
    _T2 = _T4
    parm _T2
    call _PrintInt
    return