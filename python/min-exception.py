# ruleid: min-missing-except
m = min([])

try:
    # ok: min-missing-except
    m = min([])
except:
    pass

try:
    # ok: min-missing-except
    m = min([])
except ValueError:
    pass

try:
    # ok: min-missing-except
    m = min([])
except ValueError as e:
    pass

try:
    # ok: min-missing-except
    m = min([])
except Exception:
    pass
