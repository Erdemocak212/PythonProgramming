""" 1) """

custom_power = lambda x=0, /, e=1: x ** e



""" 2) """

def custom_equation(
    x: int = 0, /,
    y: int = 0, /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
   
    return (x ** a + y ** b) / c



""" 3) """

_call_count = 0
_caller_info = {}

def fn_w_counter():
    global _call_count, _caller_info

    import inspect

    caller = inspect.currentframe().f_back.f_globals.get("__name__", "unknown")

    _call_count += 1
    _caller_info[caller] = _caller_info.get(caller, 0) + 1

    return _call_count, _caller_info
