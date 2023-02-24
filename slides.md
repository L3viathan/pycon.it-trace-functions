!image snaket.png
!up 7
!printf '    \e[1;37mTrace functions: building a tiny debugger\e[0m\n\n'
!printf '     \e[3;37mJonathan Oberländer — PyCon Italia, 2023\e[0m\n\n'

============

// reset:
!!rm -f mypdb.py
!!git checkout -- buggy_code.py

# About me

- Developer working at [solute](https://solute.de):
  - German e-commerce company based in Karlsruhe
- <3 Python

============

# Format

- Live-coding
    - mistakes can happen
    - happy for audience suggestions/corrections/...
- Result will be pushed to a repo (link at the end)

============

# Debugging

============

// look at and try out buggy code
// mention print() debugging, but:
// too inflexible, let's use breakpoint() instead.
// try pdb
!!tmux new-window
!!tmux send-keys 'vim buggy_code.py' Enter

# `breakpoint()`

- replacement for `pdb.set_trace()`; PEP 553
- calls the breakpoint hook
- set by `PYTHONBREAKPOINT`; default: pdb.set_trace

================
// now show simplest possible trace function in buggy code
!!tmux next-window

# Trace functions

- hooks for debuggers
- **global** trace function:
    - called when entering new scope
    - _can_ return local trace function
    - set via `sys.settrace(some_callable)`
- **local** trace function:
    - called at certain other events

================
!!tmux next-window
# Events

- `call`
- `line`
- `return` (`arg`: return value)
- `exception` (`arg`: exception tuple)
- `opcode`*

================

# Frames
// who knows what this is?

≈ entries on the call stack

references to

- current code object
- current file with line number
- current locals, globals
- parent frame

================

!!tmux next-window

# Takeaway

- set a global trace function with `sys.settrace`
- have it return a local trace function
- events: `call`, `line`, `return`, `exception`
- frames: interpreter state with
    - .f_lineno
    - .f_code
    - .f_trace
    - .f_back
    - ...

================
# Meta takeaway

- Python is very introspectable
- Make toy version of complex systems to understand them
- Doing this is a lot of fun

================

!image snakeend.png
!up 6

!printf '\e[37m    Thank you!\e[0m\n\n'
!printf '\e[37m    Questions?\e[0m\n\n\n'

!printf ' \e[3;37m@L3viathan@mastodon.social\e[0m\n'

<https://github.com/L3viathan/pycon.it-trace-functions>

================

# The elephant in the room: PEP-669

- changes the way trace functions work, but:
    - backwards-compatible (less performant)
    - in 3.12…

================

# That ugly way to redefine locals

!unsetlocal exec
```python
ctypes.pythonapi.PyFrame_LocalsToFast(
    ctypes.py_object(frame),
    ctypes.c_int(0),
)
```

===============

# Presentation framework: `representty`

`IPython` + `rich` + `viu` + Markdown

===============

!image firenze.png
