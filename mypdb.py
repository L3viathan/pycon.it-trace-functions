import sys
import inspect

STEP_INTO = False
JUMP_TO_RETURN = False

def l_trace(frame, event, arg):
    global STEP_INTO, JUMP_TO_RETURN
    if JUMP_TO_RETURN and event != "return":
        return
    with open(inspect.getsourcefile(frame)) as f:
        lines = [line.rstrip() for line in f]
    print(lines[frame.f_lineno - 1])
    while True:
        match input("mypdb> "):
            case "":
                continue
            case "q" | "quit":
                raise RuntimeError
            case "n" | "next":
                break
            case "c" | "continue":
                frame.f_trace = None
                sys.settrace(None)
                break
            case "s" | "step":
                STEP_INTO = True
                break
            case "r" | "return":
                JUMP_TO_RETURN = True
                break
            case "l" | "line":
                context = []
                for i in range(frame.f_lineno - 3, frame.f_lineno + 3):
                    if i < 0 or i > len(lines) - 1:
                        continue
                    if i == frame.f_lineno - 1:
                        context.append(f"{i + 1}> {lines[i]}")
                    else:
                        context.append(f"{i + 1}  {lines[i]}")
                print(*context, sep="\n")
            case command:
                value = eval(command, frame.f_globals, frame.f_locals)
                if value is not None:
                    print(repr(value))

def g_trace(frame, event, arg):
    if STEP_INTO:
        return l_trace

def set_trace():
    sys.settrace(g_trace)
    sys._getframe(1).f_trace = l_trace
