mprotect() sets the executable flag on a region of memory, where
certain data is copied. [man page](https://linux.die.net/man/2/mprotect)

Since this explanation uses objdump it might seem a bit harder, but
using Ghidra should be a easier.

Extract that data (objdump or something, have a look at what is in the
register that gets called). Alternatively use Ghidra to decompile the
binary. This walkthrough uses objdump.

From objdump we can see that a region of memory is allocated with
memalign, and a value called keychecker is copied to that region of
memory.

```
    11df:	e8 6c fe ff ff       	callq  1050 <memalign@plt>
    11e4:	48 89 05 75 2e 00 00 	mov    %rax,0x2e75(%rip)        # 4060 <magicbuffer>
    11eb:	8b 45 d4             	mov    -0x2c(%rbp),%eax
    11ee:	48 63 c8             	movslq %eax,%rcx
    11f1:	48 8b 05 68 2e 00 00 	mov    0x2e68(%rip),%rax        # 4060 <magicbuffer>
    11f8:	ba 07 00 00 00       	mov    $0x7,%edx
    11fd:	48 89 ce             	mov    %rcx,%rsi
    1200:	48 89 c7             	mov    %rax,%rdi
    1203:	e8 58 fe ff ff       	callq  1060 <mprotect@plt>
    1208:	48 8b 05 51 2e 00 00 	mov    0x2e51(%rip),%rax        # 4060 <magicbuffer>
    120f:	48 8b 0d 0a 0e 00 00 	mov    0xe0a(%rip),%rcx        # 2020 <keychecker>
    1216:	48 8b 1d 0b 0e 00 00 	mov    0xe0b(%rip),%rbx        # 2028 <keychecker+0x8>
    121d:	48 89 08             	mov    %rcx,(%rax)
    1220:	48 89 58 08          	mov    %rbx,0x8(%rax)
    1224:	48 8b 0d 05 0e 00 00 	mov    0xe05(%rip),%rcx        # 2030 <keychecker+0x10>
    122b:	48 8b 1d 06 0e 00 00 	mov    0xe06(%rip),%rbx        # 2038 <keychecker+0x18>
    1232:	48 89 48 10          	mov    %rcx,0x10(%rax)
    1236:	48 89 58 18          	mov    %rbx,0x18(%rax)
    123a:	48 8b 0d ff 0d 00 00 	mov    0xdff(%rip),%rcx        # 2040 <keychecker+0x20>
    1241:	48 8b 1d 00 0e 00 00 	mov    0xe00(%rip),%rbx        # 2048 <keychecker+0x28>
    1248:	48 89 48 20          	mov    %rcx,0x20(%rax)
    124c:	48 89 58 28          	mov    %rbx,0x28(%rax)
    1250:	48 8b 0d f9 0d 00 00 	mov    0xdf9(%rip),%rcx        # 2050 <keychecker+0x30>
    1257:	48 8b 1d fa 0d 00 00 	mov    0xdfa(%rip),%rbx        # 2058 <keychecker+0x38>
    125e:	48 89 48 30          	mov    %rcx,0x30(%rax)
    1262:	48 89 58 38          	mov    %rbx,0x38(%rax)
    1266:	0f b7 15 f3 0d 00 00 	movzwl 0xdf3(%rip),%edx        # 2060 <keychecker+0x40>
    126d:	66 89 50 40          	mov    %dx,0x40(%rax)
    1271:	48 8b 05 e8 2d 00 00 	mov    0x2de8(%rip),%rax        # 4060 <magicbuffer>
```

A bit further you see a `callq` on register `%r8` which contains that
magicbuffer.

```
	1271:	48 8b 05 e8 2d 00 00 	mov    0x2de8(%rip),%rax        # 4060 <magicbuffer>
    1278:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
	...
	12e6:	41 ff d0             	callq  *%r8
```

So it seems that a block of memory is copied, and executed. Now let's
investigate what is inside `keychecker`

From the read only data section we can extract the data from position
`0x2020` until `0x2068`.

```
Contents of section .rodata:
 2000 01000200 00000000 00000000 00000000  ................
 2010 00000000 00000000 00000000 00000000  ................
 2020 554889e5 897dfc89 75f88955 f4894df0  UH...}..u..U..M.
 2030 817dfc7c 99000075 22817df8 5c460000  .}.|...u".}.\F..
 2040 7519817d f4859e00 00751081 7df086a5  u..}.....u..}...
 2050 00007507 b8010000 00eb05b8 00000000  ..u.............
 2060 5dc30000 00000000 55736520 74686520  ].......Use the 
 2070 666f7572 206b6579 73206173 20706172  four keys as par
 2080 616d6574 65727320 746f2067 61696e20  ameters to gain 
 2090 61636365 73732e00 4578616d 706c653a  access..Example:
 20a0 202e2f63 68616c6c 656e6765 20312032   ./challenge 1 2
 20b0 20332034 00756863 74667b25 3034782d   3 4.uhctf{%04x-
 20c0 25303478 2d253034 782d2530 34787d0a  %04x-%04x-%04x}.
 20d0 0057726f 6e67206b 65797300           .Wrong keys. 
```

Copy that data to a disassembler (online or something else) and you'll
get some very simple checks for 4 values.

![](./disassembler.png)

These are 4 very simple checks with 4 values (from the input arguments).

Use those 4 values to get the keys and flag.

`./challenge 39292 18012 40581 42374`
