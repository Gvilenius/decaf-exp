VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<STATIC>:
    NULL
    "STATIC"

VTABLE<Stack>:
    NULL
    "Stack"
    FUNCTION<Stack.Init>
    FUNCTION<Stack.NumElems>
    FUNCTION<Stack.Pop>
    FUNCTION<Stack.Push>

FUNCTION<Main.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Main>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Stack.new>:
    _T0 = 12
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Stack>
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

FUNCTION<Stack.Init>:
    _T1 = 100
    _T2 = 0
    _T3 = (_T1 < _T2)
    if (_T3 == 0) branch _L1
    _T4 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T4
    call _PrintString
    call _Halt
_L1:
    _T5 = 1
    _T6 = (_T1 + _T5)
    _T7 = 4
    _T8 = (_T6 * _T7)
    parm _T8
    _T9 = call _Alloc
    *(_T9 + 0) = _T1
    _T10 = (_T9 + _T8)
    _T10 = (_T10 - _T7)
_L3:
    _T11 = (_T10 != _T9)
    if (_T11 == 0) branch _L2
    *(_T10 + 0) = _T2
    _T10 = (_T10 - _T7)
    branch _L3
_L2:
    _T12 = (_T9 + _T7)
    *(_T0 + 4) = _T12
    _T13 = 0
    *(_T0 + 8) = _T13
    _T14 = 3
    _T15 = *(_T0 + 0)
    _T16 = *(_T15 + 20)
    parm _T0
    parm _T14
    call _T16
    return

FUNCTION<Stack.Push>:
    _T2 = *(_T0 + 4)
    _T3 = *(_T0 + 8)
    _T4 = *(_T2 - 4)
    _T5 = 0
    _T6 = (_T3 < _T5)
    _T7 = (_T3 >= _T4)
    _T8 = (_T6 || _T7)
    if (_T8 == 0) branch _L4
    _T9 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T9
    call _PrintString
    call _Halt
_L4:
    _T10 = 4
    _T11 = (_T3 * _T10)
    _T12 = (_T2 + _T11)
    *(_T12 + 0) = _T1
    _T13 = *(_T0 + 8)
    _T14 = 1
    _T17 = (_T13 + _T14)
    *(_T0 + 8) = _T17
    return

FUNCTION<Stack.Pop>:
    _T2 = *(_T0 + 4)
    _T3 = *(_T0 + 8)
    _T4 = 1
    _T7 = (_T3 - _T4)
    _T8 = *(_T2 - 4)
    _T9 = 0
    _T10 = (_T7 < _T9)
    _T11 = (_T7 >= _T8)
    _T12 = (_T10 || _T11)
    if (_T12 == 0) branch _L5
    _T13 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T13
    call _PrintString
    call _Halt
_L5:
    _T14 = 4
    _T15 = (_T7 * _T14)
    _T16 = (_T2 + _T15)
    _T17 = *(_T16 + 0)
    _T1 = _T17
    _T18 = *(_T0 + 8)
    _T19 = 1
    _T22 = (_T18 - _T19)
    *(_T0 + 8) = _T22
    return _T1

FUNCTION<Stack.NumElems>:
    _T1 = *(_T0 + 8)
    return _T1

FUNCTION<Stack.main>:
    _T1 = call FUNCTION<Stack.new>
    _T0 = _T1
    _T2 = *(_T0 + 0)
    _T3 = *(_T2 + 8)
    parm _T0
    call _T3
    _T4 = 3
    _T5 = *(_T0 + 0)
    _T6 = *(_T5 + 20)
    parm _T0
    parm _T4
    call _T6
    _T7 = 7
    _T8 = *(_T0 + 0)
    _T9 = *(_T8 + 20)
    parm _T0
    parm _T7
    call _T9
    _T10 = 4
    _T11 = *(_T0 + 0)
    _T12 = *(_T11 + 20)
    parm _T0
    parm _T10
    call _T12
    _T13 = *(_T0 + 0)
    _T14 = *(_T13 + 12)
    parm _T0
    _T15 = call _T14
    parm _T15
    call _PrintInt
    _T16 = " "
    parm _T16
    call _PrintString
    _T17 = *(_T0 + 0)
    _T18 = *(_T17 + 16)
    parm _T0
    _T19 = call _T18
    parm _T19
    call _PrintInt
    _T20 = " "
    parm _T20
    call _PrintString
    _T21 = *(_T0 + 0)
    _T22 = *(_T21 + 16)
    parm _T0
    _T23 = call _T22
    parm _T23
    call _PrintInt
    _T24 = " "
    parm _T24
    call _PrintString
    _T25 = *(_T0 + 0)
    _T26 = *(_T25 + 16)
    parm _T0
    _T27 = call _T26
    parm _T27
    call _PrintInt
    _T28 = " "
    parm _T28
    call _PrintString
    _T29 = *(_T0 + 0)
    _T30 = *(_T29 + 12)
    parm _T0
    _T31 = call _T30
    parm _T31
    call _PrintInt
    return

main:
    call FUNCTION<Stack.main>
    return

