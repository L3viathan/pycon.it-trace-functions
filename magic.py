from types import FrameType
import fishhook
import dis


def depth(frame):
    d = 1
    while frame := frame.f_back:
        d += 1
    return d

@fishhook.hook(FrameType)
def __repr__(self):
    return f"""
┏━\x1b[3mFrame\x1b[0m━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ \x1b[1mf_code\x1b[0m   │ \x1b[32m{"…" + self.f_code.co_filename[-28:]:<29s}\x1b[0m ┃
┃ \x1b[1mf_lineno\x1b[0m │ \x1b[36m{str(self.f_lineno):>29s}\x1b[0m ┃
┃ \x1b[1mf_lasti\x1b[0m  │ \x1b[36m{str(self.f_lasti):>29s}\x1b[0m ┃
┃ \x1b[1mdepth\x1b[0m    │ \x1b[36m{str(depth(self)):>29s}\x1b[0m ┃
┃ \x1b[1mlasti\x1b[0m    │ \x1b[31m{dis.opname[self.f_code.co_code[self.f_lasti]]:>29s}\x1b[0m ┃
┗━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""".strip()
