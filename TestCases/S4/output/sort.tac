VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    NULL
    "Main"

VTABLE<MergeSort>:
    NULL
    "MergeSort"

VTABLE<QuickSort>:
    NULL
    "QuickSort"

VTABLE<Rng>:
    NULL
    "Rng"
    FUNCTION<Rng.next>

VTABLE<STATIC>:
    NULL
    "STATIC"
    FUNCTION<QuickSort.sort>
    FUNCTION<Rng.make>
    FUNCTION<MergeSort.sort>
    FUNCTION<MergeSort.sort_impl>

FUNCTION<QuickSort.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<QuickSort>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Rng.new>:
    _T0 = 8
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Rng>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<MergeSort.new>:
    _T0 = 4
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<MergeSort>
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
    _T4 = 500
    _T5 = 0
    _T6 = (_T4 < _T5)
    if (_T6 == 0) branch _L1
    _T7 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T7
    call _PrintString
    call _Halt
_L1:
    _T8 = 1
    _T9 = (_T4 + _T8)
    _T10 = 4
    _T11 = (_T9 * _T10)
    parm _T11
    _T12 = call _Alloc
    *(_T12 + 0) = _T4
    _T13 = (_T12 + _T11)
    _T13 = (_T13 - _T10)
_L3:
    _T14 = (_T13 != _T12)
    if (_T14 == 0) branch _L2
    *(_T13 + 0) = _T5
    _T13 = (_T13 - _T10)
    branch _L3
_L2:
    _T15 = (_T12 + _T10)
    _T3 = _T15
    _T17 = 500
    _T18 = 0
    _T19 = (_T17 < _T18)
    if (_T19 == 0) branch _L4
    _T20 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T20
    call _PrintString
    call _Halt
_L4:
    _T21 = 1
    _T22 = (_T17 + _T21)
    _T23 = 4
    _T24 = (_T22 * _T23)
    parm _T24
    _T25 = call _Alloc
    *(_T25 + 0) = _T17
    _T26 = (_T25 + _T24)
    _T26 = (_T26 - _T23)
_L6:
    _T27 = (_T26 != _T25)
    if (_T27 == 0) branch _L5
    *(_T26 + 0) = _T18
    _T26 = (_T26 - _T23)
    branch _L6
_L5:
    _T28 = (_T25 + _T23)
    _T16 = _T28
    _T30 = 0
    _T29 = _T30
_L8:
    _T31 = *(_T3 - 4)
    _T34 = (_T29 < _T31)
    if (_T34 == 0) branch _L7
    _T35 = *(_T3 - 4)
    _T36 = 0
    _T37 = (_T29 < _T36)
    _T38 = (_T29 >= _T35)
    _T39 = (_T37 || _T38)
    if (_T39 == 0) branch _L9
    _T40 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T40
    call _PrintString
    call _Halt
_L9:
    _T41 = 4
    _T42 = (_T29 * _T41)
    _T43 = (_T3 + _T42)
    _T44 = *(_T0 + 0)
    _T45 = *(_T44 + 8)
    parm _T0
    _T46 = call _T45
    _T47 = 500
    _T48 = 0
    _T49 = (_T47 == _T48)
    if (_T49 == 0) branch _L10
    _T50 = "Decaf runtime error: Division by zero error\n"
    parm _T50
    call _PrintString
    call _Halt
_L10:
    _T51 = (_T46 % _T47)
    *(_T43 + 0) = _T51
    _T52 = *(_T16 - 4)
    _T53 = 0
    _T54 = (_T29 < _T53)
    _T55 = (_T29 >= _T52)
    _T56 = (_T54 || _T55)
    if (_T56 == 0) branch _L11
    _T57 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T57
    call _PrintString
    call _Halt
_L11:
    _T58 = 4
    _T59 = (_T29 * _T58)
    _T60 = (_T16 + _T59)
    _T61 = *(_T3 - 4)
    _T62 = 0
    _T63 = (_T29 < _T62)
    _T64 = (_T29 >= _T61)
    _T65 = (_T63 || _T64)
    if (_T65 == 0) branch _L12
    _T66 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T66
    call _PrintString
    call _Halt
_L12:
    _T67 = 4
    _T68 = (_T29 * _T67)
    _T69 = (_T3 + _T68)
    _T70 = *(_T69 + 0)
    *(_T60 + 0) = _T70
    _T71 = 1
    _T74 = (_T29 + _T71)
    _T29 = _T74
    branch _L8
_L7:
    _T75 = 0
    _T76 = *(_T3 - 4)
    _T77 = 1
    _T80 = (_T76 - _T77)
    parm _T3
    parm _T75
    parm _T80
    call FUNCTION<QuickSort.sort>
    _T82 = 0
    _T81 = _T82
_L14:
    _T83 = *(_T3 - 4)
    _T86 = (_T81 < _T83)
    if (_T86 == 0) branch _L13
    _T87 = *(_T3 - 4)
    _T88 = 0
    _T89 = (_T81 < _T88)
    _T90 = (_T81 >= _T87)
    _T91 = (_T89 || _T90)
    if (_T91 == 0) branch _L15
    _T92 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T92
    call _PrintString
    call _Halt
_L15:
    _T93 = 4
    _T94 = (_T81 * _T93)
    _T95 = (_T3 + _T94)
    _T96 = *(_T95 + 0)
    parm _T96
    call _PrintInt
    _T97 = " "
    parm _T97
    call _PrintString
    _T98 = 1
    _T101 = (_T81 + _T98)
    _T81 = _T101
    branch _L14
_L13:
    _T102 = "\n"
    parm _T102
    call _PrintString
    parm _T16
    call FUNCTION<MergeSort.sort>
    _T104 = 0
    _T103 = _T104
_L17:
    _T105 = *(_T16 - 4)
    _T108 = (_T103 < _T105)
    if (_T108 == 0) branch _L16
    _T109 = *(_T16 - 4)
    _T110 = 0
    _T111 = (_T103 < _T110)
    _T112 = (_T103 >= _T109)
    _T113 = (_T111 || _T112)
    if (_T113 == 0) branch _L18
    _T114 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T114
    call _PrintString
    call _Halt
_L18:
    _T115 = 4
    _T116 = (_T103 * _T115)
    _T117 = (_T16 + _T116)
    _T118 = *(_T117 + 0)
    parm _T118
    call _PrintInt
    _T119 = " "
    parm _T119
    call _PrintString
    _T120 = 1
    _T123 = (_T103 + _T120)
    _T103 = _T123
    branch _L17
_L16:
    _T124 = "\n"
    parm _T124
    call _PrintString
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
    if (_T5 == 0) branch _L19
    _T6 = "Decaf runtime error: Division by zero error\n"
    parm _T6
    call _PrintString
    call _Halt
_L19:
    _T7 = (_T2 % _T3)
    _T10 = (_T1 * _T7)
    _T11 = 22221
    _T14 = (_T10 + _T11)
    _T15 = 65536
    _T16 = 0
    _T17 = (_T15 == _T16)
    if (_T17 == 0) branch _L20
    _T18 = "Decaf runtime error: Division by zero error\n"
    parm _T18
    call _PrintString
    call _Halt
_L20:
    _T19 = (_T14 % _T15)
    *(_T0 + 4) = _T19
    _T20 = *(_T0 + 4)
    return _T20

FUNCTION<QuickSort.sort>:
    _T3 = _T1
    _T4 = _T2
    _T8 = (_T2 - _T1)
    _T9 = 2
    _T10 = 0
    _T11 = (_T9 == _T10)
    if (_T11 == 0) branch _L21
    _T12 = "Decaf runtime error: Division by zero error\n"
    parm _T12
    call _PrintString
    call _Halt
_L21:
    _T13 = (_T8 / _T9)
    _T16 = (_T1 + _T13)
    _T17 = *(_T0 - 4)
    _T18 = 0
    _T19 = (_T16 < _T18)
    _T20 = (_T16 >= _T17)
    _T21 = (_T19 || _T20)
    if (_T21 == 0) branch _L22
    _T22 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T22
    call _PrintString
    call _Halt
_L22:
    _T23 = 4
    _T24 = (_T16 * _T23)
    _T25 = (_T0 + _T24)
    _T26 = *(_T25 + 0)
    _T5 = _T26
_L24:
    _T29 = (_T3 <= _T4)
    if (_T29 == 0) branch _L23
_L26:
    _T30 = *(_T0 - 4)
    _T31 = 0
    _T32 = (_T3 < _T31)
    _T33 = (_T3 >= _T30)
    _T34 = (_T32 || _T33)
    if (_T34 == 0) branch _L27
    _T35 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T35
    call _PrintString
    call _Halt
_L27:
    _T36 = 4
    _T37 = (_T3 * _T36)
    _T38 = (_T0 + _T37)
    _T39 = *(_T38 + 0)
    _T42 = (_T39 < _T5)
    if (_T42 == 0) branch _L25
    _T43 = 1
    _T46 = (_T3 + _T43)
    _T3 = _T46
    branch _L26
_L25:
_L29:
    _T47 = *(_T0 - 4)
    _T48 = 0
    _T49 = (_T4 < _T48)
    _T50 = (_T4 >= _T47)
    _T51 = (_T49 || _T50)
    if (_T51 == 0) branch _L30
    _T52 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T52
    call _PrintString
    call _Halt
_L30:
    _T53 = 4
    _T54 = (_T4 * _T53)
    _T55 = (_T0 + _T54)
    _T56 = *(_T55 + 0)
    _T59 = (_T56 > _T5)
    if (_T59 == 0) branch _L28
    _T60 = 1
    _T63 = (_T4 - _T60)
    _T4 = _T63
    branch _L29
_L28:
    _T66 = (_T3 <= _T4)
    if (_T66 == 0) branch _L31
    _T68 = *(_T0 - 4)
    _T69 = 0
    _T70 = (_T3 < _T69)
    _T71 = (_T3 >= _T68)
    _T72 = (_T70 || _T71)
    if (_T72 == 0) branch _L32
    _T73 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T73
    call _PrintString
    call _Halt
_L32:
    _T74 = 4
    _T75 = (_T3 * _T74)
    _T76 = (_T0 + _T75)
    _T77 = *(_T76 + 0)
    _T67 = _T77
    _T78 = *(_T0 - 4)
    _T79 = 0
    _T80 = (_T3 < _T79)
    _T81 = (_T3 >= _T78)
    _T82 = (_T80 || _T81)
    if (_T82 == 0) branch _L33
    _T83 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T83
    call _PrintString
    call _Halt
_L33:
    _T84 = 4
    _T85 = (_T3 * _T84)
    _T86 = (_T0 + _T85)
    _T87 = *(_T0 - 4)
    _T88 = 0
    _T89 = (_T4 < _T88)
    _T90 = (_T4 >= _T87)
    _T91 = (_T89 || _T90)
    if (_T91 == 0) branch _L34
    _T92 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T92
    call _PrintString
    call _Halt
_L34:
    _T93 = 4
    _T94 = (_T4 * _T93)
    _T95 = (_T0 + _T94)
    _T96 = *(_T95 + 0)
    *(_T86 + 0) = _T96
    _T97 = *(_T0 - 4)
    _T98 = 0
    _T99 = (_T4 < _T98)
    _T100 = (_T4 >= _T97)
    _T101 = (_T99 || _T100)
    if (_T101 == 0) branch _L35
    _T102 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T102
    call _PrintString
    call _Halt
_L35:
    _T103 = 4
    _T104 = (_T4 * _T103)
    _T105 = (_T0 + _T104)
    *(_T105 + 0) = _T67
    _T106 = 1
    _T109 = (_T3 + _T106)
    _T3 = _T109
    _T110 = 1
    _T113 = (_T4 - _T110)
    _T4 = _T113
_L31:
    branch _L24
_L23:
    _T116 = (_T1 < _T4)
    if (_T116 == 0) branch _L36
    parm _T0
    parm _T1
    parm _T4
    call FUNCTION<QuickSort.sort>
_L36:
    _T119 = (_T3 < _T2)
    if (_T119 == 0) branch _L37
    parm _T0
    parm _T3
    parm _T2
    call FUNCTION<QuickSort.sort>
_L37:
    return

FUNCTION<MergeSort.sort>:
    _T1 = 0
    _T2 = *(_T0 - 4)
    _T3 = *(_T0 - 4)
    _T4 = 0
    _T5 = (_T3 < _T4)
    if (_T5 == 0) branch _L38
    _T6 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T6
    call _PrintString
    call _Halt
_L38:
    _T7 = 1
    _T8 = (_T3 + _T7)
    _T9 = 4
    _T10 = (_T8 * _T9)
    parm _T10
    _T11 = call _Alloc
    *(_T11 + 0) = _T3
    _T12 = (_T11 + _T10)
    _T12 = (_T12 - _T9)
_L40:
    _T13 = (_T12 != _T11)
    if (_T13 == 0) branch _L39
    *(_T12 + 0) = _T4
    _T12 = (_T12 - _T9)
    branch _L40
_L39:
    _T14 = (_T11 + _T9)
    parm _T0
    parm _T1
    parm _T2
    parm _T14
    call FUNCTION<MergeSort.sort_impl>
    return

FUNCTION<MergeSort.sort_impl>:
    _T4 = 1
    _T7 = (_T1 + _T4)
    _T10 = (_T7 < _T2)
    if (_T10 == 0) branch _L41
    _T14 = (_T1 + _T2)
    _T15 = 2
    _T16 = 0
    _T17 = (_T15 == _T16)
    if (_T17 == 0) branch _L42
    _T18 = "Decaf runtime error: Division by zero error\n"
    parm _T18
    call _PrintString
    call _Halt
_L42:
    _T19 = (_T14 / _T15)
    _T11 = _T19
    parm _T0
    parm _T1
    parm _T11
    parm _T3
    call FUNCTION<MergeSort.sort_impl>
    parm _T0
    parm _T11
    parm _T2
    parm _T3
    call FUNCTION<MergeSort.sort_impl>
    _T20 = _T1
    _T21 = _T11
    _T23 = 0
    _T22 = _T23
_L44:
    _T26 = (_T20 < _T11)
    _T29 = (_T21 < _T2)
    _T32 = (_T26 && _T29)
    if (_T32 == 0) branch _L43
    _T33 = *(_T0 - 4)
    _T34 = 0
    _T35 = (_T21 < _T34)
    _T36 = (_T21 >= _T33)
    _T37 = (_T35 || _T36)
    if (_T37 == 0) branch _L45
    _T38 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T38
    call _PrintString
    call _Halt
_L45:
    _T39 = 4
    _T40 = (_T21 * _T39)
    _T41 = (_T0 + _T40)
    _T42 = *(_T41 + 0)
    _T43 = *(_T0 - 4)
    _T44 = 0
    _T45 = (_T20 < _T44)
    _T46 = (_T20 >= _T43)
    _T47 = (_T45 || _T46)
    if (_T47 == 0) branch _L46
    _T48 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T48
    call _PrintString
    call _Halt
_L46:
    _T49 = 4
    _T50 = (_T20 * _T49)
    _T51 = (_T0 + _T50)
    _T52 = *(_T51 + 0)
    _T55 = (_T42 < _T52)
    if (_T55 == 0) branch _L47
    _T56 = *(_T3 - 4)
    _T57 = 0
    _T58 = (_T22 < _T57)
    _T59 = (_T22 >= _T56)
    _T60 = (_T58 || _T59)
    if (_T60 == 0) branch _L49
    _T61 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T61
    call _PrintString
    call _Halt
_L49:
    _T62 = 4
    _T63 = (_T22 * _T62)
    _T64 = (_T3 + _T63)
    _T65 = *(_T0 - 4)
    _T66 = 0
    _T67 = (_T21 < _T66)
    _T68 = (_T21 >= _T65)
    _T69 = (_T67 || _T68)
    if (_T69 == 0) branch _L50
    _T70 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T70
    call _PrintString
    call _Halt
_L50:
    _T71 = 4
    _T72 = (_T21 * _T71)
    _T73 = (_T0 + _T72)
    _T74 = *(_T73 + 0)
    *(_T64 + 0) = _T74
    _T75 = 1
    _T78 = (_T21 + _T75)
    _T21 = _T78
    branch _L48
_L47:
    _T79 = *(_T3 - 4)
    _T80 = 0
    _T81 = (_T22 < _T80)
    _T82 = (_T22 >= _T79)
    _T83 = (_T81 || _T82)
    if (_T83 == 0) branch _L51
    _T84 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T84
    call _PrintString
    call _Halt
_L51:
    _T85 = 4
    _T86 = (_T22 * _T85)
    _T87 = (_T3 + _T86)
    _T88 = *(_T0 - 4)
    _T89 = 0
    _T90 = (_T20 < _T89)
    _T91 = (_T20 >= _T88)
    _T92 = (_T90 || _T91)
    if (_T92 == 0) branch _L52
    _T93 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T93
    call _PrintString
    call _Halt
_L52:
    _T94 = 4
    _T95 = (_T20 * _T94)
    _T96 = (_T0 + _T95)
    _T97 = *(_T96 + 0)
    *(_T87 + 0) = _T97
    _T98 = 1
    _T101 = (_T20 + _T98)
    _T20 = _T101
_L48:
    _T102 = 1
    _T105 = (_T22 + _T102)
    _T22 = _T105
    branch _L44
_L43:
_L54:
    _T108 = (_T20 < _T11)
    if (_T108 == 0) branch _L53
    _T109 = *(_T3 - 4)
    _T110 = 0
    _T111 = (_T22 < _T110)
    _T112 = (_T22 >= _T109)
    _T113 = (_T111 || _T112)
    if (_T113 == 0) branch _L55
    _T114 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T114
    call _PrintString
    call _Halt
_L55:
    _T115 = 4
    _T116 = (_T22 * _T115)
    _T117 = (_T3 + _T116)
    _T118 = *(_T0 - 4)
    _T119 = 0
    _T120 = (_T20 < _T119)
    _T121 = (_T20 >= _T118)
    _T122 = (_T120 || _T121)
    if (_T122 == 0) branch _L56
    _T123 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T123
    call _PrintString
    call _Halt
_L56:
    _T124 = 4
    _T125 = (_T20 * _T124)
    _T126 = (_T0 + _T125)
    _T127 = *(_T126 + 0)
    *(_T117 + 0) = _T127
    _T128 = 1
    _T131 = (_T22 + _T128)
    _T22 = _T131
    _T132 = 1
    _T135 = (_T20 + _T132)
    _T20 = _T135
    branch _L54
_L53:
    _T136 = 0
    _T20 = _T136
_L58:
    _T139 = (_T20 < _T22)
    if (_T139 == 0) branch _L57
    _T142 = (_T20 + _T1)
    _T143 = *(_T0 - 4)
    _T144 = 0
    _T145 = (_T142 < _T144)
    _T146 = (_T142 >= _T143)
    _T147 = (_T145 || _T146)
    if (_T147 == 0) branch _L59
    _T148 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T148
    call _PrintString
    call _Halt
_L59:
    _T149 = 4
    _T150 = (_T142 * _T149)
    _T151 = (_T0 + _T150)
    _T152 = *(_T3 - 4)
    _T153 = 0
    _T154 = (_T20 < _T153)
    _T155 = (_T20 >= _T152)
    _T156 = (_T154 || _T155)
    if (_T156 == 0) branch _L60
    _T157 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T157
    call _PrintString
    call _Halt
_L60:
    _T158 = 4
    _T159 = (_T20 * _T158)
    _T160 = (_T3 + _T159)
    _T161 = *(_T160 + 0)
    *(_T151 + 0) = _T161
    _T162 = 1
    _T165 = (_T20 + _T162)
    _T20 = _T165
    branch _L58
_L57:
_L41:
    return

