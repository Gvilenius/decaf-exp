VTABLE<Complex>:
    NULL
    "Complex"
    FUNCTION<Complex.abs2>

VTABLE<LAMBDA>:
    NULL
    "LAMBDA"

VTABLE<Main>:
    VTABLE<Complex>
    "Main"
    FUNCTION<Complex.abs2>

VTABLE<STATIC>:
    NULL
    "STATIC"
    FUNCTION<Complex.add>
    FUNCTION<Complex.make>
    FUNCTION<Complex.mul>
    FUNCTION<Complex.sub>

FUNCTION<Main.new>:
    _T0 = 12
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Main>
    *(_T1 + 0) = _T2
    return _T1

FUNCTION<Complex.new>:
    _T0 = 12
    parm _T0
    _T1 = call _Alloc
    _T2 = VTABLE<Complex>
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

FUNCTION<Complex.make>:
    _T3 = call FUNCTION<Complex.new>
    _T2 = _T3
    _T4 = 32768
    _T5 = 0
    _T6 = (_T4 == _T5)
    if (_T6 == 0) branch _L1
    _T7 = "Decaf runtime error: Division by zero error\n"
    parm _T7
    call _PrintString
    call _Halt
_L1:
    _T8 = (_T0 % _T4)
    *(_T2 + 8) = _T8
    _T9 = 32768
    _T10 = 0
    _T11 = (_T9 == _T10)
    if (_T11 == 0) branch _L2
    _T12 = "Decaf runtime error: Division by zero error\n"
    parm _T12
    call _PrintString
    call _Halt
_L2:
    _T13 = (_T1 % _T9)
    *(_T2 + 4) = _T13
    return _T2

FUNCTION<Complex.add>:
    _T2 = *(_T0 + 8)
    _T3 = *(_T1 + 8)
    _T6 = (_T2 + _T3)
    _T7 = *(_T0 + 4)
    _T8 = *(_T1 + 4)
    _T11 = (_T7 + _T8)
    parm _T6
    parm _T11
    _T12 = call FUNCTION<Complex.make>
    return _T12

FUNCTION<Complex.sub>:
    _T2 = *(_T0 + 8)
    _T3 = *(_T1 + 8)
    _T6 = (_T2 - _T3)
    _T7 = *(_T0 + 4)
    _T8 = *(_T1 + 4)
    _T11 = (_T7 - _T8)
    parm _T6
    parm _T11
    _T12 = call FUNCTION<Complex.make>
    return _T12

FUNCTION<Complex.mul>:
    _T2 = *(_T0 + 8)
    _T3 = *(_T1 + 8)
    _T6 = (_T2 * _T3)
    _T7 = *(_T0 + 4)
    _T8 = *(_T1 + 4)
    _T11 = (_T7 * _T8)
    _T14 = (_T6 - _T11)
    _T15 = 4096
    _T16 = 0
    _T17 = (_T15 == _T16)
    if (_T17 == 0) branch _L3
    _T18 = "Decaf runtime error: Division by zero error\n"
    parm _T18
    call _PrintString
    call _Halt
_L3:
    _T19 = (_T14 / _T15)
    _T20 = *(_T0 + 8)
    _T21 = *(_T1 + 4)
    _T24 = (_T20 * _T21)
    _T25 = *(_T0 + 4)
    _T26 = *(_T1 + 8)
    _T29 = (_T25 * _T26)
    _T32 = (_T24 + _T29)
    _T33 = 4096
    _T34 = 0
    _T35 = (_T33 == _T34)
    if (_T35 == 0) branch _L4
    _T36 = "Decaf runtime error: Division by zero error\n"
    parm _T36
    call _PrintString
    call _Halt
_L4:
    _T37 = (_T32 / _T33)
    parm _T19
    parm _T37
    _T38 = call FUNCTION<Complex.make>
    return _T38

FUNCTION<Complex.abs2>:
    _T1 = *(_T0 + 8)
    _T2 = *(_T0 + 8)
    _T5 = (_T1 * _T2)
    _T6 = *(_T0 + 4)
    _T7 = *(_T0 + 4)
    _T10 = (_T6 * _T7)
    _T13 = (_T5 + _T10)
    return _T13

main:
    _T1 = 51
    _T0 = _T1
    _T3 = 4096
    _T2 = _T3
    _T5 = 2
    _T6 = - _T5
    _T9 = (_T6 * _T2)
    _T4 = _T9
    _T11 = 4
    _T14 = (_T11 * _T2)
    _T15 = 1
    _T18 = (_T0 - _T15)
    _T19 = 0
    _T20 = (_T18 == _T19)
    if (_T20 == 0) branch _L5
    _T21 = "Decaf runtime error: Division by zero error\n"
    parm _T21
    call _PrintString
    call _Halt
_L5:
    _T22 = (_T14 / _T18)
    _T10 = _T22
    _T24 = 0
    _T25 = (_T0 < _T24)
    if (_T25 == 0) branch _L6
    _T26 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T26
    call _PrintString
    call _Halt
_L6:
    _T27 = 1
    _T28 = (_T0 + _T27)
    _T29 = 4
    _T30 = (_T28 * _T29)
    parm _T30
    _T31 = call _Alloc
    *(_T31 + 0) = _T0
    _T32 = (_T31 + _T30)
    _T32 = (_T32 - _T29)
_L8:
    _T33 = (_T32 != _T31)
    if (_T33 == 0) branch _L7
    *(_T32 + 0) = _T24
    _T32 = (_T32 - _T29)
    branch _L8
_L7:
    _T34 = (_T31 + _T29)
    _T23 = _T34
    _T36 = 0
    _T37 = (_T0 < _T36)
    if (_T37 == 0) branch _L9
    _T38 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T38
    call _PrintString
    call _Halt
_L9:
    _T39 = 1
    _T40 = (_T0 + _T39)
    _T41 = 4
    _T42 = (_T40 * _T41)
    parm _T42
    _T43 = call _Alloc
    *(_T43 + 0) = _T0
    _T44 = (_T43 + _T42)
    _T44 = (_T44 - _T41)
_L11:
    _T45 = (_T44 != _T43)
    if (_T45 == 0) branch _L10
    *(_T44 + 0) = _T36
    _T44 = (_T44 - _T41)
    branch _L11
_L10:
    _T46 = (_T43 + _T41)
    _T35 = _T46
    _T48 = 0
    _T47 = _T48
_L13:
    _T51 = (_T47 < _T0)
    if (_T51 == 0) branch _L12
    _T52 = *(_T23 - 4)
    _T53 = 0
    _T54 = (_T47 < _T53)
    _T55 = (_T47 >= _T52)
    _T56 = (_T54 || _T55)
    if (_T56 == 0) branch _L14
    _T57 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T57
    call _PrintString
    call _Halt
_L14:
    _T58 = 4
    _T59 = (_T47 * _T58)
    _T60 = (_T23 + _T59)
    _T61 = 0
    _T62 = (_T0 < _T61)
    if (_T62 == 0) branch _L15
    _T63 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T63
    call _PrintString
    call _Halt
_L15:
    _T64 = 1
    _T65 = (_T0 + _T64)
    _T66 = 4
    _T67 = (_T65 * _T66)
    parm _T67
    _T68 = call _Alloc
    *(_T68 + 0) = _T0
    _T69 = (_T68 + _T67)
    _T69 = (_T69 - _T66)
_L17:
    _T70 = (_T69 != _T68)
    if (_T70 == 0) branch _L16
    *(_T69 + 0) = _T61
    _T69 = (_T69 - _T66)
    branch _L17
_L16:
    _T71 = (_T68 + _T66)
    *(_T60 + 0) = _T71
    _T72 = *(_T35 - 4)
    _T73 = 0
    _T74 = (_T47 < _T73)
    _T75 = (_T47 >= _T72)
    _T76 = (_T74 || _T75)
    if (_T76 == 0) branch _L18
    _T77 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T77
    call _PrintString
    call _Halt
_L18:
    _T78 = 4
    _T79 = (_T47 * _T78)
    _T80 = (_T35 + _T79)
    _T81 = 0
    _T82 = (_T0 < _T81)
    if (_T82 == 0) branch _L19
    _T83 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T83
    call _PrintString
    call _Halt
_L19:
    _T84 = 1
    _T85 = (_T0 + _T84)
    _T86 = 4
    _T87 = (_T85 * _T86)
    parm _T87
    _T88 = call _Alloc
    *(_T88 + 0) = _T0
    _T89 = (_T88 + _T87)
    _T89 = (_T89 - _T86)
_L21:
    _T90 = (_T89 != _T88)
    if (_T90 == 0) branch _L20
    *(_T89 + 0) = _T81
    _T89 = (_T89 - _T86)
    branch _L21
_L20:
    _T91 = (_T88 + _T86)
    *(_T80 + 0) = _T91
    _T93 = 0
    _T92 = _T93
_L23:
    _T96 = (_T92 < _T0)
    if (_T96 == 0) branch _L22
    _T97 = *(_T23 - 4)
    _T98 = 0
    _T99 = (_T47 < _T98)
    _T100 = (_T47 >= _T97)
    _T101 = (_T99 || _T100)
    if (_T101 == 0) branch _L24
    _T102 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T102
    call _PrintString
    call _Halt
_L24:
    _T103 = 4
    _T104 = (_T47 * _T103)
    _T105 = (_T23 + _T104)
    _T106 = *(_T105 + 0)
    _T107 = *(_T106 - 4)
    _T108 = 0
    _T109 = (_T92 < _T108)
    _T110 = (_T92 >= _T107)
    _T111 = (_T109 || _T110)
    if (_T111 == 0) branch _L25
    _T112 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T112
    call _PrintString
    call _Halt
_L25:
    _T113 = 4
    _T114 = (_T92 * _T113)
    _T115 = (_T106 + _T114)
    _T118 = (_T92 * _T10)
    _T121 = (_T4 + _T118)
    _T124 = (_T47 * _T10)
    _T127 = (_T4 + _T124)
    parm _T121
    parm _T127
    _T128 = call FUNCTION<Complex.make>
    *(_T115 + 0) = _T128
    _T129 = *(_T35 - 4)
    _T130 = 0
    _T131 = (_T47 < _T130)
    _T132 = (_T47 >= _T129)
    _T133 = (_T131 || _T132)
    if (_T133 == 0) branch _L26
    _T134 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T134
    call _PrintString
    call _Halt
_L26:
    _T135 = 4
    _T136 = (_T47 * _T135)
    _T137 = (_T35 + _T136)
    _T138 = *(_T137 + 0)
    _T139 = *(_T138 - 4)
    _T140 = 0
    _T141 = (_T92 < _T140)
    _T142 = (_T92 >= _T139)
    _T143 = (_T141 || _T142)
    if (_T143 == 0) branch _L27
    _T144 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T144
    call _PrintString
    call _Halt
_L27:
    _T145 = 4
    _T146 = (_T92 * _T145)
    _T147 = (_T138 + _T146)
    _T148 = call FUNCTION<Complex.new>
    *(_T147 + 0) = _T148
    _T149 = 1
    _T152 = (_T92 + _T149)
    _T92 = _T152
    branch _L23
_L22:
    _T153 = 1
    _T156 = (_T47 + _T153)
    _T47 = _T156
    branch _L13
_L12:
    _T158 = 0
    _T157 = _T158
_L29:
    _T159 = 20
    _T162 = (_T157 < _T159)
    if (_T162 == 0) branch _L28
    _T164 = 0
    _T163 = _T164
_L31:
    _T167 = (_T163 < _T0)
    if (_T167 == 0) branch _L30
    _T169 = 0
    _T168 = _T169
_L33:
    _T172 = (_T168 < _T0)
    if (_T172 == 0) branch _L32
    _T174 = *(_T35 - 4)
    _T175 = 0
    _T176 = (_T163 < _T175)
    _T177 = (_T163 >= _T174)
    _T178 = (_T176 || _T177)
    if (_T178 == 0) branch _L34
    _T179 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T179
    call _PrintString
    call _Halt
_L34:
    _T180 = 4
    _T181 = (_T163 * _T180)
    _T182 = (_T35 + _T181)
    _T183 = *(_T182 + 0)
    _T184 = *(_T183 - 4)
    _T185 = 0
    _T186 = (_T168 < _T185)
    _T187 = (_T168 >= _T184)
    _T188 = (_T186 || _T187)
    if (_T188 == 0) branch _L35
    _T189 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T189
    call _PrintString
    call _Halt
_L35:
    _T190 = 4
    _T191 = (_T168 * _T190)
    _T192 = (_T183 + _T191)
    _T193 = *(_T192 + 0)
    _T173 = _T193
    _T194 = *(_T173 + 0)
    _T195 = *(_T194 + 8)
    parm _T173
    _T196 = call _T195
    _T197 = 4
    _T200 = (_T197 * _T2)
    _T203 = (_T200 * _T2)
    _T206 = (_T196 < _T203)
    if (_T206 == 0) branch _L36
    _T207 = *(_T35 - 4)
    _T208 = 0
    _T209 = (_T163 < _T208)
    _T210 = (_T163 >= _T207)
    _T211 = (_T209 || _T210)
    if (_T211 == 0) branch _L37
    _T212 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T212
    call _PrintString
    call _Halt
_L37:
    _T213 = 4
    _T214 = (_T163 * _T213)
    _T215 = (_T35 + _T214)
    _T216 = *(_T215 + 0)
    _T217 = *(_T216 - 4)
    _T218 = 0
    _T219 = (_T168 < _T218)
    _T220 = (_T168 >= _T217)
    _T221 = (_T219 || _T220)
    if (_T221 == 0) branch _L38
    _T222 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T222
    call _PrintString
    call _Halt
_L38:
    _T223 = 4
    _T224 = (_T168 * _T223)
    _T225 = (_T216 + _T224)
    parm _T173
    parm _T173
    _T226 = call FUNCTION<Complex.mul>
    _T227 = *(_T23 - 4)
    _T228 = 0
    _T229 = (_T163 < _T228)
    _T230 = (_T163 >= _T227)
    _T231 = (_T229 || _T230)
    if (_T231 == 0) branch _L39
    _T232 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T232
    call _PrintString
    call _Halt
_L39:
    _T233 = 4
    _T234 = (_T163 * _T233)
    _T235 = (_T23 + _T234)
    _T236 = *(_T235 + 0)
    _T237 = *(_T236 - 4)
    _T238 = 0
    _T239 = (_T168 < _T238)
    _T240 = (_T168 >= _T237)
    _T241 = (_T239 || _T240)
    if (_T241 == 0) branch _L40
    _T242 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T242
    call _PrintString
    call _Halt
_L40:
    _T243 = 4
    _T244 = (_T168 * _T243)
    _T245 = (_T236 + _T244)
    _T246 = *(_T245 + 0)
    parm _T226
    parm _T246
    _T247 = call FUNCTION<Complex.add>
    *(_T225 + 0) = _T247
_L36:
    _T248 = 1
    _T251 = (_T168 + _T248)
    _T168 = _T251
    branch _L33
_L32:
    _T252 = 1
    _T255 = (_T163 + _T252)
    _T163 = _T255
    branch _L31
_L30:
    _T256 = 1
    _T259 = (_T157 + _T256)
    _T157 = _T259
    branch _L29
_L28:
    _T261 = 0
    _T260 = _T261
_L42:
    _T264 = (_T260 < _T0)
    if (_T264 == 0) branch _L41
    _T266 = 0
    _T265 = _T266
_L44:
    _T269 = (_T265 < _T0)
    if (_T269 == 0) branch _L43
    _T270 = *(_T35 - 4)
    _T271 = 0
    _T272 = (_T260 < _T271)
    _T273 = (_T260 >= _T270)
    _T274 = (_T272 || _T273)
    if (_T274 == 0) branch _L45
    _T275 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T275
    call _PrintString
    call _Halt
_L45:
    _T276 = 4
    _T277 = (_T260 * _T276)
    _T278 = (_T35 + _T277)
    _T279 = *(_T278 + 0)
    _T280 = *(_T279 - 4)
    _T281 = 0
    _T282 = (_T265 < _T281)
    _T283 = (_T265 >= _T280)
    _T284 = (_T282 || _T283)
    if (_T284 == 0) branch _L46
    _T285 = "Decaf runtime error: Array subscript out of bounds\n"
    parm _T285
    call _PrintString
    call _Halt
_L46:
    _T286 = 4
    _T287 = (_T265 * _T286)
    _T288 = (_T279 + _T287)
    _T289 = *(_T288 + 0)
    _T290 = *(_T289 + 0)
    _T291 = *(_T290 + 8)
    parm _T289
    _T292 = call _T291
    _T293 = 4
    _T296 = (_T293 * _T2)
    _T299 = (_T296 * _T2)
    _T302 = (_T292 < _T299)
    if (_T302 == 0) branch _L47
    _T303 = "**"
    parm _T303
    call _PrintString
    branch _L48
_L47:
    _T304 = "  "
    parm _T304
    call _PrintString
_L48:
    _T305 = 1
    _T308 = (_T265 + _T305)
    _T265 = _T308
    branch _L44
_L43:
    _T309 = "\n"
    parm _T309
    call _PrintString
    _T310 = 1
    _T313 = (_T260 + _T310)
    _T260 = _T313
    branch _L42
_L41:
    return

