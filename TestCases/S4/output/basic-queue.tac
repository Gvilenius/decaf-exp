VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<Queue>:
    NULL
    "Queue"
    FUNCTION<Queue.DeQueue>
    FUNCTION<Queue.EnQueue>
    FUNCTION<Queue.Init>

VTABLE<QueueItem>:
    NULL
    "QueueItem"
    FUNCTION<QueueItem.GetData>
    FUNCTION<QueueItem.GetNext>
    FUNCTION<QueueItem.GetPrev>
    FUNCTION<QueueItem.Init>
    FUNCTION<QueueItem.SetNext>
    FUNCTION<QueueItem.SetPrev>

VTABLE<STATIC>:
    NULL
    "STATIC"

FUNCTION<QueueItem.new>:
    _T0 = 16
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<QueueItem>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Queue.new>:
    _T0 = 12
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Queue>
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

FUNCTION<QueueItem.Init>:
    *(_T0 + 4) = _T1
    *(_T0 + 8) = _T2
    *(_T2 + 12) = _T0
    *(_T0 + 12) = _T3
    *(_T3 + 8) = _T0
    return

FUNCTION<QueueItem.GetData>:
    _T1 = *(_T0 + 4)
    return _T1

FUNCTION<QueueItem.GetNext>:
    _T1 = *(_T0 + 8)
    return _T1

FUNCTION<QueueItem.GetPrev>:
    _T1 = *(_T0 + 12)
    return _T1

FUNCTION<QueueItem.SetNext>:
    *(_T0 + 8) = _T1
    return

FUNCTION<QueueItem.SetPrev>:
    *(_T0 + 12) = _T1
    return

FUNCTION<Queue.Init>:
    _T1 = call FUNCTION<QueueItem.new>
    *(_T0 + 4) = _T1
    _T2 = 0
    _T3 = *(_T0 + 4)
    _T4 = *(_T0 + 4)
    _T5 = *(_T0 + 4)
    _T6 = *(_T5 + 0)
    _T7 = *(_T6 + 20)
    parm _T5
    parm _T2
    parm _T3
    parm _T4
    call _T7
    return

FUNCTION<Queue.EnQueue>:
    _T3 = call FUNCTION<QueueItem.new>
    _T2 = _T3
    _T4 = *(_T0 + 4)
    _T5 = *(_T4 + 0)
    _T6 = *(_T5 + 12)
    parm _T4
    _T7 = call _T6
    _T8 = *(_T0 + 4)
    _T9 = *(_T2 + 0)
    _T10 = *(_T9 + 20)
    parm _T2
    parm _T1
    parm _T7
    parm _T8
    call _T10
    return

FUNCTION<Queue.DeQueue>:
    _T2 = *(_T0 + 4)
    _T3 = *(_T2 + 0)
    _T4 = *(_T3 + 16)
    parm _T2
    _T5 = call _T4
    _T6 = *(_T0 + 4)
    _T9 = (_T5 == _T6)
    if (_T9 == 0) branch _L1
    _T10 = "Queue Is Empty"
    parm _T10
    call _PrintString
    _T11 = 0
    return _T11
    branch _L2
_L1:
    _T13 = *(_T0 + 4)
    _T14 = *(_T13 + 0)
    _T15 = *(_T14 + 16)
    parm _T13
    _T16 = call _T15
    _T12 = _T16
    _T17 = *(_T12 + 0)
    _T18 = *(_T17 + 8)
    parm _T12
    _T19 = call _T18
    _T1 = _T19
    _T20 = *(_T12 + 0)
    _T21 = *(_T20 + 12)
    parm _T12
    _T22 = call _T21
    _T23 = *(_T12 + 0)
    _T24 = *(_T23 + 16)
    parm _T12
    _T25 = call _T24
    _T26 = *(_T25 + 0)
    _T27 = *(_T26 + 24)
    parm _T25
    parm _T22
    call _T27
    _T28 = *(_T12 + 0)
    _T29 = *(_T28 + 16)
    parm _T12
    _T30 = call _T29
    _T31 = *(_T12 + 0)
    _T32 = *(_T31 + 12)
    parm _T12
    _T33 = call _T32
    _T34 = *(_T33 + 0)
    _T35 = *(_T34 + 28)
    parm _T33
    parm _T30
    call _T35
_L2:
    return _T1

main:
    _T2 = call FUNCTION<Queue.new>
    _T0 = _T2
    _T3 = *(_T0 + 0)
    _T4 = *(_T3 + 16)
    parm _T0
    call _T4
    _T5 = 0
    _T1 = _T5
_L4:
    _T6 = 10
    _T9 = (_T1 < _T6)
    if (_T9 == 0) branch _L3
    _T10 = *(_T0 + 0)
    _T11 = *(_T10 + 12)
    parm _T0
    parm _T1
    call _T11
    _T12 = 1
    _T15 = (_T1 + _T12)
    _T1 = _T15
    branch _L4
_L3:
    _T16 = 0
    _T1 = _T16
_L6:
    _T17 = 4
    _T20 = (_T1 < _T17)
    if (_T20 == 0) branch _L5
    _T21 = *(_T0 + 0)
    _T22 = *(_T21 + 8)
    parm _T0
    _T23 = call _T22
    parm _T23
    call _PrintInt
    _T24 = " "
    parm _T24
    call _PrintString
    _T25 = 1
    _T28 = (_T1 + _T25)
    _T1 = _T28
    branch _L6
_L5:
    _T29 = "\n"
    parm _T29
    call _PrintString
    _T30 = 0
    _T1 = _T30
_L8:
    _T31 = 10
    _T34 = (_T1 < _T31)
    if (_T34 == 0) branch _L7
    _T35 = *(_T0 + 0)
    _T36 = *(_T35 + 12)
    parm _T0
    parm _T1
    call _T36
    _T37 = 1
    _T40 = (_T1 + _T37)
    _T1 = _T40
    branch _L8
_L7:
    _T41 = 0
    _T1 = _T41
_L10:
    _T42 = 17
    _T45 = (_T1 < _T42)
    if (_T45 == 0) branch _L9
    _T46 = *(_T0 + 0)
    _T47 = *(_T46 + 8)
    parm _T0
    _T48 = call _T47
    parm _T48
    call _PrintInt
    _T49 = " "
    parm _T49
    call _PrintString
    _T50 = 1
    _T53 = (_T1 + _T50)
    _T1 = _T53
    branch _L10
_L9:
    _T54 = "\n"
    parm _T54
    call _PrintString
    return

