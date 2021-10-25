# ruleid: max-missing-except
m = max([])

try:
    # ok: max-missing-except
    m = max([])
except:
    pass

try:
    # ok: max-missing-except
    m = max([])
except ValueError:
    pass

try:
    # ok: max-missing-except
    m = max([])
except ValueError as e:
    pass

try:
    # ok: max-missing-except
    m = max([])
except Exception:
    pass
