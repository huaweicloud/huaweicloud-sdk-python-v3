import sys
import warnings

_MIN_PY_VERSION = (3, 6)

if sys.version_info < _MIN_PY_VERSION:
    current_version = ".".join(str(v) for v in sys.version_info[:3])
    min_version = ".".join(str(v) for v in _MIN_PY_VERSION)
    msg = (
        "'huaweicloudsdkcore' will drop support for Python < {min} very soon. "
        "You are using Python {current}. "
        "Please upgrade to Python {min}+ to ensure future compatibility."
    ).format(current=current_version, min=min_version)

    warnings.warn(msg, FutureWarning)
