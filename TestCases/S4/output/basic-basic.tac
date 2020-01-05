VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<STATIC>:
    NULL
    "STATIC"

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
    _T1 = 2
    _T0 = _T1
    _T3 = 3
    _T2 = _T3
    _T5 = 1
    _T4 = _T5
    _T7 = "Hello THU"
    _T6 = _T7
    parm _T0
    call _PrintInt
    _T8 = "\n"
    parm _T8
    call _PrintString
    parm _T2
    call _PrintInt
    _T9 = "\n"
    parm _T9
    call _PrintString
    _T12 = (_T0 + _T2)
    parm _T12
    call _PrintInt
    _T13 = "\n"
    parm _T13
    call _PrintString
    _T16 = (_T0 * _T2)
    parm _T16
    call _PrintInt
    _T17 = "\n"
    parm _T17
    call _PrintString
    parm _T4
    call _PrintBool
    _T18 = "\n"
    parm _T18
    call _PrintString
    parm _T6
    call _PrintString
    _T19 = "\n"
    parm _T19
    call _PrintString
    return

