VTABLE<Fibonacci>:
    NULL
    "Fibonacci"
    FUNCTION<Fibonacci.get>

VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<STATIC>:
    NULL
    "STATIC"

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

main:
    _T1 = 0
    _T0 = _T1
    _T3 = call FUNCTION<Fibonacci.new>
    _T2 = _T3
_L2:
    _T4 = 10
    _T7 = (_T0 < _T4)
    if (_T7 == 0) branch _L1
    _T8 = *(_T2 + 0)
    _T9 = *(_T8 + 8)
    parm _T2
    parm _T0
    _T10 = call _T9
    parm _T10
    call _PrintInt
    _T11 = "\n"
    parm _T11
    call _PrintString
    _T12 = 1
    _T15 = (_T0 + _T12)
    _T0 = _T15
    branch _L2
_L1:
    return

FUNCTION<Fibonacci.get>:
    _T2 = 2
    _T5 = (_T1 < _T2)
    if (_T5 == 0) branch _L3
    _T6 = 1
    return _T6
_L3:
    _T7 = 1
    _T10 = (_T1 - _T7)
    _T11 = *(_T0 + 0)
    _T12 = *(_T11 + 8)
    parm _T0
    parm _T10
    _T13 = call _T12
    _T14 = 2
    _T17 = (_T1 - _T14)
    _T18 = *(_T0 + 0)
    _T19 = *(_T18 + 8)
    parm _T0
    parm _T17
    _T20 = call _T19
    _T23 = (_T13 + _T20)
    return _T23

