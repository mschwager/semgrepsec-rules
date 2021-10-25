# ruleid: zero-division-missing-except
m = 5 / 0

try:
    # ok: zero-division-missing-except
    m = 5 / 0
except:
    pass

try:
    # ok: zero-division-missing-except
    m = 5 / 0
except ZeroDivisionError:
    pass

try:
    # ok: zero-division-missing-except
    m = 5 / 0
except ZeroDivisionError as e:
    pass

try:
    # ok: zero-division-missing-except
    m = 5 / 0
except Exception:
    pass
