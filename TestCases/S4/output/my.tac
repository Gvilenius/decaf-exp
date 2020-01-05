VTABLE<Fibonacci>:
    NULL
    "Fibonacci"

VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<STATIC>:
    NULL
    "STATIC"
    FUNCTION<Fibonacci.get>

FUNCTION<Fibonacci.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Fibonacci>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Main.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Main>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<STATIC.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<STATIC>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<LAMBDA.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<LAMBDA>
    *(_T1 + 0) = _T2
    return _T1

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
    _T3 = 3
    parm _T3
    _T4 = call FUNCTION<Fibonacci.get>
    _T2 = _T4
    parm _T2
    call _PrintInt
    return

