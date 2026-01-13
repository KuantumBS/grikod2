# __init__.py

from __future__ import annotations

import importlib
import warnings
import os

# Geliştirme modunda yeniden yükleme (isteğe bağlı)
if os.getenv("DEVELOPMENT") == "true":
    try:
        import grikod2.grikod2
        importlib.reload(grikod2.grikod2)
    except (ImportError, KeyError):
        pass

# Doğru modül adıyla içe aktarım yapın: grikod2.py → .grikod2
try:
    from .grikod2 import ikili_2_gri_kod, run_interactive_converter, InvalidBinaryError
except ImportError as e:
    warnings.warn(f"Gerekli modül yüklenemedi: {e}", ImportWarning)

__all__ = ["ikili_2_gri_kod", "run_interactive_converter", "InvalidBinaryError"]

__version__ = "1.1.4"

def eski_fonksiyon():
    warnings.warn(
        "eski_fonksiyon() artık kullanılmamaktadır...",
        category=DeprecationWarning,
        stacklevel=2
    )
