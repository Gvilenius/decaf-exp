VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<Node>:
    NULL
    "Node"

VTABLE<RBTree>:
    VTABLE<Node>
    "RBTree"
    FUNCTION<RBTree.delete>
    FUNCTION<RBTree.delete_fix>
    FUNCTION<RBTree.insert>
    FUNCTION<RBTree.insert_fix>
    FUNCTION<RBTree.print>
    FUNCTION<RBTree.print_impl>
    FUNCTION<RBTree.rotate>
    FUNCTION<RBTree.transplant>

VTABLE<Rng>:
    NULL
    "Rng"
    FUNCTION<Rng.next>

VTABLE<STATIC>:
    NULL
    "STATIC"
    FUNCTION<Node.make>
    FUNCTION<RBTree.make1>
    FUNCTION<Rng.make>

FUNCTION<Node.new>:
    _T0 = 24
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Node>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<RBTree.new>:
    _T0 = 32
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<RBTree>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Rng.new>:
    _T0 = 8
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Rng>
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
    _T1 = 19260817
    parm _T1
    _T2 = call FUNCTION<Rng.make>
    _T0 = _T2
    _T4 = call FUNCTION<RBTree.make1>
    _T3 = _T4
    _T6 = 0
    _T5 = _T6
_L2:
    _T7 = 5
    _T10 = (_T5 < _T7)
    if (_T10 == 0) branch _L1
    _T12 = 0
    _T11 = _T12
_L4:
    _T13 = 500
    _T16 = (_T11 < _T13)
    if (_T16 == 0) branch _L3
    _T17 = *(_T0 + 0)
    _T18 = *(_T17 + 8)
    parm _T0
    _T19 = call _T18
    _T20 = 500
    _T21 = 0
    _T22 = (_T20 == _T21)
    if (_T22 == 0) branch _L5
    _T23 = "Decaf runtime error: Division by zero error\n"
    parm _T23
    call _PrintString
    call _Halt
_L5:
    _T24 = (_T19 % _T20)
    _T25 = *(_T3 + 0)
    _T26 = *(_T25 + 16)
    parm _T3
    parm _T24
    call _T26
    _T27 = 1
    _T30 = (_T11 + _T27)
    _T11 = _T30
    branch _L4
_L3:
    _T32 = 0
    _T31 = _T32
_L7:
    _T33 = 500
    _T36 = (_T31 < _T33)
    if (_T36 == 0) branch _L6
    _T37 = *(_T0 + 0)
    _T38 = *(_T37 + 8)
    parm _T0
    _T39 = call _T38
    _T40 = 500
    _T41 = 0
    _T42 = (_T40 == _T41)
    if (_T42 == 0) branch _L8
    _T43 = "Decaf runtime error: Division by zero error\n"
    parm _T43
    call _PrintString
    call _Halt
_L8:
    _T44 = (_T39 % _T40)
    _T45 = *(_T3 + 0)
    _T46 = *(_T45 + 8)
    parm _T3
    parm _T44
    call _T46
    _T47 = 1
    _T50 = (_T31 + _T47)
    _T31 = _T50
    branch _L7
_L6:
    _T51 = 1
    _T54 = (_T5 + _T51)
    _T5 = _T54
    branch _L2
_L1:
    _T55 = *(_T3 + 0)
    _T56 = *(_T55 + 24)
    parm _T3
    call _T56
    return

FUNCTION<Rng.make>:
    _T2 = call FUNCTION<Rng.new>
    _T1 = _T2
    *(_T1 + 4) = _T0
    return _T1

FUNCTION<Rng.next>:
    _T1 = 15625
    _T2 = *(_T0 + 4)
    _T3 = 10000
    _T4 = 0
    _T5 = (_T3 == _T4)
    if (_T5 == 0) branch _L9
    _T6 = "Decaf runtime error: Division by zero error\n"
    parm _T6
    call _PrintString
    call _Halt
_L9:
    _T7 = (_T2 % _T3)
    _T10 = (_T1 * _T7)
    _T11 = 22221
    _T14 = (_T10 + _T11)
    _T15 = 65536
    _T16 = 0
    _T17 = (_T15 == _T16)
    if (_T17 == 0) branch _L10
    _T18 = "Decaf runtime error: Division by zero error\n"
    parm _T18
    call _PrintString
    call _Halt
_L10:
    _T19 = (_T14 % _T15)
    *(_T0 + 4) = _T19
    _T20 = *(_T0 + 4)
    return _T20

FUNCTION<Node.make>:
    _T4 = call FUNCTION<Node.new>
    _T3 = _T4
    *(_T3 + 8) = _T2
    *(_T3 + 16) = _T0
    *(_T3 + 12) = _T1
    *(_T3 + 20) = _T1
    _T5 = 1
    *(_T3 + 4) = _T5
    return _T3

FUNCTION<RBTree.make1>:
    _T1 = call FUNCTION<RBTree.new>
    _T0 = _T1
    _T3 = call FUNCTION<Node.new>
    _T2 = _T3
    *(_T2 + 16) = _T2
    *(_T2 + 12) = _T2
    *(_T2 + 20) = _T2
    *(_T0 + 28) = _T2
    *(_T0 + 24) = _T2
    return _T0

FUNCTION<RBTree.transplant>:
    _T4 = *(_T1 + 16)
    _T3 = _T4
    _T5 = *(_T0 + 24)
    _T8 = (_T3 == _T5)
    if (_T8 == 0) branch _L11
    *(_T0 + 28) = _T2
    branch _L12
_L11:
    _T9 = *(_T3 + 20)
    _T12 = (_T9 == _T1)
    if (_T12 == 0) branch _L13
    *(_T3 + 20) = _T2
    branch _L14
_L13:
    *(_T3 + 12) = _T2
_L14:
_L12:
    *(_T2 + 16) = _T3
    return

FUNCTION<RBTree.rotate>:
    _T3 = *(_T1 + 16)
    _T2 = _T3
    _T5 = *(_T2 + 16)
    _T4 = _T5
    *(_T1 + 16) = _T4
    _T6 = *(_T0 + 24)
    _T9 = (_T4 == _T6)
    if (_T9 == 0) branch _L15
    *(_T0 + 28) = _T1
    branch _L16
_L15:
    _T10 = *(_T4 + 20)
    _T13 = (_T10 == _T2)
    if (_T13 == 0) branch _L17
    *(_T4 + 20) = _T1
    branch _L18
_L17:
    *(_T4 + 12) = _T1
_L18:
_L16:
    _T14 = *(_T2 + 12)
    _T17 = (_T14 == _T1)
    if (_T17 == 0) branch _L19
    _T18 = *(_T1 + 20)
    *(_T2 + 12) = _T18
    _T19 = *(_T1 + 20)
    *(_T19 + 16) = _T2
    *(_T1 + 20) = _T2
    branch _L20
_L19:
    _T20 = *(_T1 + 12)
    *(_T2 + 20) = _T20
    _T21 = *(_T1 + 12)
    *(_T21 + 16) = _T2
    *(_T1 + 12) = _T2
_L20:
    *(_T2 + 16) = _T1
    return

FUNCTION<RBTree.insert_fix>:
_L22:
    _T2 = *(_T1 + 16)
    _T3 = *(_T2 + 4)
    if (_T3 == 0) branch _L21
    _T5 = *(_T1 + 16)
    _T4 = _T5
    _T7 = *(_T4 + 16)
    _T6 = _T7
    _T9 = *(_T6 + 12)
    _T12 = (_T9 == _T4)
    _T8 = _T12
    if (_T8 == 0) branch _L23
    _T14 = *(_T6 + 12)
    _T13 = _T14
    branch _L24
_L23:
    _T15 = *(_T6 + 20)
    _T13 = _T15
_L24:
    _T16 = *(_T13 + 4)
    if (_T16 == 0) branch _L25
    _T17 = 0
    *(_T4 + 4) = _T17
    _T18 = 0
    *(_T13 + 4) = _T18
    _T19 = 1
    *(_T6 + 4) = _T19
    _T1 = _T6
    branch _L26
_L25:
    _T20 = *(_T4 + 12)
    _T23 = (_T20 == _T1)
    _T26 = (_T23 != _T8)
    if (_T26 == 0) branch _L27
    _T27 = *(_T0 + 0)
    _T28 = *(_T27 + 32)
    parm _T0
    parm _T1
    call _T28
    _T29 = _T1
    _T1 = _T4
    _T4 = _T29
    _T30 = *(_T4 + 16)
    _T6 = _T30
_L27:
    _T31 = 0
    *(_T4 + 4) = _T31
    _T32 = 1
    *(_T6 + 4) = _T32
    _T33 = *(_T0 + 0)
    _T34 = *(_T33 + 32)
    parm _T0
    parm _T4
    call _T34
_L26:
    branch _L22
_L21:
    _T35 = *(_T0 + 28)
    _T36 = 0
    *(_T35 + 4) = _T36
    return

FUNCTION<RBTree.insert>:
    _T3 = *(_T0 + 28)
    _T2 = _T3
    _T5 = *(_T0 + 24)
    _T4 = _T5
_L29:
    _T6 = *(_T0 + 24)
    _T9 = (_T2 != _T6)
    if (_T9 == 0) branch _L28
    _T4 = _T2
    _T10 = *(_T2 + 8)
    _T13 = (_T10 == _T1)
    if (_T13 == 0) branch _L30
    return
    branch _L31
_L30:
    _T14 = *(_T2 + 8)
    _T17 = (_T14 < _T1)
    if (_T17 == 0) branch _L32
    _T18 = *(_T2 + 20)
    _T2 = _T18
    branch _L33
_L32:
    _T19 = *(_T2 + 12)
    _T2 = _T19
_L33:
_L31:
    branch _L29
_L28:
    _T21 = *(_T0 + 24)
    parm _T4
    parm _T21
    parm _T1
    _T22 = call FUNCTION<Node.make>
    _T20 = _T22
    _T23 = *(_T0 + 24)
    _T26 = (_T4 == _T23)
    if (_T26 == 0) branch _L34
    *(_T0 + 28) = _T20
    branch _L35
_L34:
    _T27 = *(_T4 + 8)
    _T30 = (_T27 < _T1)
    if (_T30 == 0) branch _L36
    *(_T4 + 20) = _T20
    branch _L37
_L36:
    *(_T4 + 12) = _T20
_L37:
_L35:
    _T31 = *(_T0 + 0)
    _T32 = *(_T31 + 20)
    parm _T0
    parm _T20
    call _T32
    return

FUNCTION<RBTree.delete_fix>:
_L39:
    _T2 = *(_T0 + 28)
    _T5 = (_T1 != _T2)
    _T6 = *(_T1 + 4)
    _T7 = ! _T6
    _T10 = (_T5 && _T7)
    if (_T10 == 0) branch _L38
    _T12 = *(_T1 + 16)
    _T11 = _T12
    _T14 = *(_T11 + 12)
    _T17 = (_T14 == _T1)
    _T13 = _T17
    if (_T13 == 0) branch _L40
    _T19 = *(_T11 + 20)
    _T18 = _T19
    branch _L41
_L40:
    _T20 = *(_T11 + 12)
    _T18 = _T20
_L41:
    _T21 = *(_T18 + 4)
    if (_T21 == 0) branch _L42
    _T22 = 0
    *(_T18 + 4) = _T22
    _T23 = 1
    *(_T11 + 4) = _T23
    _T24 = *(_T0 + 0)
    _T25 = *(_T24 + 32)
    parm _T0
    parm _T18
    call _T25
    if (_T13 == 0) branch _L43
    _T26 = *(_T11 + 20)
    _T18 = _T26
    branch _L44
_L43:
    _T27 = *(_T11 + 12)
    _T18 = _T27
_L44:
_L42:
    _T28 = *(_T18 + 12)
    _T29 = *(_T28 + 4)
    _T30 = ! _T29
    _T31 = *(_T18 + 20)
    _T32 = *(_T31 + 4)
    _T33 = ! _T32
    _T36 = (_T30 && _T33)
    if (_T36 == 0) branch _L45
    _T37 = 0
    *(_T18 + 4) = _T37
    _T1 = _T11
    branch _L46
_L45:
    _T39 = *(_T18 + 20)
    _T38 = _T39
    _T41 = *(_T18 + 12)
    _T40 = _T41
    if (_T13 == 0) branch _L47
    _T42 = _T38
    _T38 = _T40
    _T40 = _T42
_L47:
    _T43 = *(_T40 + 4)
    _T44 = ! _T43
    if (_T44 == 0) branch _L48
    _T45 = 0
    *(_T38 + 4) = _T45
    _T46 = 1
    *(_T18 + 4) = _T46
    _T47 = *(_T0 + 0)
    _T48 = *(_T47 + 32)
    parm _T0
    parm _T38
    call _T48
    if (_T13 == 0) branch _L49
    _T49 = *(_T11 + 20)
    _T18 = _T49
    _T50 = *(_T18 + 20)
    _T40 = _T50
    branch _L50
_L49:
    _T51 = *(_T11 + 12)
    _T18 = _T51
    _T52 = *(_T18 + 12)
    _T40 = _T52
_L50:
_L48:
    _T53 = *(_T11 + 4)
    *(_T18 + 4) = _T53
    _T54 = 0
    *(_T11 + 4) = _T54
    _T55 = 0
    *(_T40 + 4) = _T55
    _T56 = *(_T0 + 0)
    _T57 = *(_T56 + 32)
    parm _T0
    parm _T18
    call _T57
    _T58 = *(_T0 + 28)
    _T1 = _T58
_L46:
    branch _L39
_L38:
    _T59 = 0
    *(_T1 + 4) = _T59
    return

FUNCTION<RBTree.delete>:
    _T3 = *(_T0 + 28)
    _T2 = _T3
_L52:
    _T4 = *(_T0 + 24)
    _T7 = (_T2 != _T4)
    if (_T7 == 0) branch _L51
    _T8 = *(_T2 + 8)
    _T11 = (_T8 == _T1)
    if (_T11 == 0) branch _L53
    branch _L51
    branch _L54
_L53:
    _T12 = *(_T2 + 8)
    _T15 = (_T12 < _T1)
    if (_T15 == 0) branch _L55
    _T16 = *(_T2 + 20)
    _T2 = _T16
    branch _L56
_L55:
    _T17 = *(_T2 + 12)
    _T2 = _T17
_L56:
_L54:
    branch _L52
_L51:
    _T18 = _T2
    _T21 = *(_T18 + 4)
    _T20 = _T21
    _T22 = *(_T2 + 12)
    _T23 = *(_T0 + 24)
    _T26 = (_T22 == _T23)
    if (_T26 == 0) branch _L57
    _T27 = *(_T2 + 20)
    _T19 = _T27
    _T28 = *(_T0 + 0)
    _T29 = *(_T28 + 36)
    parm _T0
    parm _T2
    parm _T19
    call _T29
    branch _L58
_L57:
    _T30 = *(_T2 + 20)
    _T31 = *(_T0 + 24)
    _T34 = (_T30 == _T31)
    if (_T34 == 0) branch _L59
    _T35 = *(_T2 + 12)
    _T19 = _T35
    _T36 = *(_T0 + 0)
    _T37 = *(_T36 + 36)
    parm _T0
    parm _T2
    parm _T19
    call _T37
    branch _L60
_L59:
    _T38 = *(_T2 + 20)
    _T18 = _T38
_L62:
    _T39 = *(_T18 + 12)
    _T40 = *(_T0 + 24)
    _T43 = (_T39 != _T40)
    if (_T43 == 0) branch _L61
    _T44 = *(_T18 + 12)
    _T18 = _T44
    branch _L62
_L61:
    _T45 = *(_T18 + 4)
    _T20 = _T45
    _T46 = *(_T18 + 20)
    _T19 = _T46
    _T47 = *(_T18 + 16)
    _T50 = (_T47 == _T2)
    if (_T50 == 0) branch _L63
    *(_T19 + 16) = _T18
    branch _L64
_L63:
    _T51 = *(_T0 + 0)
    _T52 = *(_T51 + 36)
    parm _T0
    parm _T18
    parm _T19
    call _T52
    _T53 = *(_T2 + 20)
    *(_T18 + 20) = _T53
    _T54 = *(_T18 + 20)
    *(_T54 + 16) = _T18
_L64:
    _T55 = *(_T0 + 0)
    _T56 = *(_T55 + 36)
    parm _T0
    parm _T2
    parm _T18
    call _T56
    _T57 = *(_T2 + 12)
    *(_T18 + 12) = _T57
    _T58 = *(_T18 + 12)
    *(_T58 + 16) = _T18
    _T59 = *(_T2 + 4)
    *(_T18 + 4) = _T59
_L60:
_L58:
    _T60 = ! _T20
    if (_T60 == 0) branch _L65
    _T61 = *(_T0 + 0)
    _T62 = *(_T61 + 12)
    parm _T0
    parm _T19
    call _T62
_L65:
    return

FUNCTION<RBTree.print>:
    _T1 = *(_T0 + 28)
    _T2 = *(_T0 + 0)
    _T3 = *(_T2 + 28)
    parm _T0
    parm _T1
    call _T3
    return

FUNCTION<RBTree.print_impl>:
    _T2 = *(_T0 + 24)
    _T5 = (_T1 == _T2)
    if (_T5 == 0) branch _L66
    return
    branch _L67
_L66:
    _T6 = *(_T1 + 12)
    _T7 = *(_T0 + 0)
    _T8 = *(_T7 + 28)
    parm _T0
    parm _T6
    call _T8
    _T9 = *(_T1 + 8)
    parm _T9
    call _PrintInt
    _T10 = " "
    parm _T10
    call _PrintString
    _T11 = *(_T1 + 20)
    _T12 = *(_T0 + 0)
    _T13 = *(_T12 + 28)
    parm _T0
    parm _T11
    call _T13
_L67:
    return

