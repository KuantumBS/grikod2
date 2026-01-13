# grikod2 (Gri Kod, Gray Code)
---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15352206.svg)](https://doi.org/10.5281/zenodo.15352206)

[![WorkflowHub DOI](https://img.shields.io/badge/DOI-10.48546%2Fworkflowhub.datafile.13.1-blue)](https://doi.org/10.48546/workflowhub.datafile.13.1)

[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod2/badges/version.svg)](https://anaconda.org/bilgi/grikod2)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod2/badges/latest_release_date.svg)](https://anaconda.org/bilgi/grikod2)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod2/badges/platforms.svg)](https://anaconda.org/bilgi/grikod2)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod2/badges/license.svg)](https://anaconda.org/bilgi/grikod2)
[![Open Source](https://img.shields.io/badge/Open%20Source-Open%20Source-brightgreen.svg)](https://opensource.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python CI](https://github.com/KuantumBS/grikod2/actions/workflows/python_ci.yml/badge.svg?branch=main)](https://github.com/KuantumBS/grikod2/actions/workflows/python_ci.yml)
[![codecov](https://codecov.io/gh/KuantumBS/grikod2/graph/badge.svg?token=1SDH8E9RAJ)](https://codecov.io/gh/KuantumBS/grikod2)
[![Documentation Status](https://readthedocs.org/projects/grikod2/badge/?version=latest)](https://grikod2.readthedocs.io/en/latest/)
[![Binder](https://terrarium.evidencepub.io/badge_logo.svg)](https://terrarium.evidencepub.io/v2/gh/KuantumBS/grikod2/HEAD)
[![PyPI version](https://badge.fury.io/py/grikod2.svg)](https://badge.fury.io/py/grikod2)
[![PyPI Downloads](https://static.pepy.tech/badge/grikod2)](https://pepy.tech/projects/grikod2)
[![Linted with Ruff](https://img.shields.io/badge/Linted%20with-Ruff-green?logo=python&logoColor=white)](https://github.com/astral-sh/ruff)

---

<p align="left">
    <table>
        <tr>
            <td style="text-align: center;">PyPI</td>
            <td style="text-align: center;">
                <a href="https://pypi.org/project/grikod2/">
                    <img src="https://badge.fury.io/py/grikod2.svg" alt="PyPI version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">Conda</td>
            <td style="text-align: center;">
                <a href="https://anaconda.org/bilgi/grikod2">
                    <img src="https://anaconda.org/bilgi/grikod2/badges/version.svg" alt="conda-forge version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">DOI</td>
            <td style="text-align: center;">
                <a href="https://doi.org/10.5281/zenodo.15352206">
                    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.15352206.svg" alt="DOI" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">License: MIT</td>
            <td style="text-align: center;">
                <a href="https://opensource.org/licenses/MIT">
                    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" height="18"/>
                </a>
            </td>
        </tr>
    </table>
</p>

---
A Python library for converting binary numbers to Gray Code with ease.

---

## Tanım (Türkçe)
Gri Kod: grikod2 İkili sayıları Gri Koda çevirir.

## Description (English)
Gri Kod: grikod2 converts binary numbers to Gray Code.

---

## Kurulum (Türkçe) / Installation (English)

### Python ile Kurulum / Install with pip, conda, mamba
```bash
pip install grikod2 -U
python -m pip install -U grikod2
conda install bilgi::grikod2 -y
mamba install bilgi::grikod2 -y
```

```diff
- pip uninstall grikod2 -y
+ pip install -U grikod2
+ python -m pip install -U grikod2
```

[PyPI](https://pypi.org/project/grikod2/)

### Test Kurulumu / Test Installation

```bash
pip install -i https://test.pypi.org/simple/ grikod2 -U
```

### Github Master Kurulumu / GitHub Master Installation

**Terminal:**

```bash
pip install git+https://github.com/KuantumBS/grikod2.git
```

**Jupyter Lab, Notebook, Visual Studio Code:**

```python
!pip install git+https://github.com/KuantumBS/grikod2.git
# or
%pip install git+https://github.com/KuantumBS/grikod2.git
```

---

## Kullanım (Türkçe) / Usage (English)

```python
import grikod2
grikod2.__version__
```

```python
import grikod2
grikod2.ikili_2_gri_kod("1010")
```

```python
import grikod2

def main():
    # Binary numbers: ikili sayılar
    binary_numbers = ["0", "1", "10", "11", "100", "101", "1111"]

    for binary in binary_numbers:
        try:
            gray_code = grikod2.ikili_2_gri_kod(binary)
            print(f"Binary: İkili: {binary} -> Gri Kod: {gray_code}")
        except grikod2.InvalidBinaryError as e:
            print(f"İkili: {binary} -> Hata: {e}")

if __name__ == "__main__":
    main()
```
```
Binary: İkili: 0 -> Gri Kod: 0
Binary: İkili: 1 -> Gri Kod: 1
Binary: İkili: 10 -> Gri Kod: 11
Binary: İkili: 11 -> Gri Kod: 10
Binary: İkili: 100 -> Gri Kod: 110
Binary: İkili: 101 -> Gri Kod: 111
Binary: İkili: 1111 -> Gri Kod: 1000


#Input: 100
#Output example
#000:000
#001:001
#010:011
#011:010
#100:110
#101:111
#110:101
#111:100
```

```python
import grikod2

def main():
    print("🌟 Gri Kod Dönüştürücü - grikod2 Paketi ile")
    print("Geçerli bir ikili sayı girin (örneğin: 1101)")
    print("Çıkmak için 'q' yazın.\n")

    while True:
        user_input = input("İkili sayı: ").strip()

        if user_input.lower() == 'q':
            print("👋 Çıkılıyor. İyi günler!")
            break

        try:
            gray_code = grikod2.ikili_2_gri_kod(user_input)
            print(f"✅ Gri Kod: {gray_code}\n")
        except grikod2.InvalidBinaryError as e:
            print(f"❌ Giriş Hatası: {e}\n")
        except Exception as e:
            print(f"⚠️ Beklenmeyen hata: {e}\n")

if __name__ == "__main__":
    main()
```

```python
import grikod2

if __name__ == "__main__":
    print("🚀 GriKod2 Etkileşimli Moduna Hoş Geldiniz!")
    grikod2.run_interactive_converter()
```

---

### Development
```bash
# Clone the repository
git clone https://github.com/KuantumBS/grikod2.git
cd grikod2

# Install in development mode
python -m pip install -ve . # Install package in development mode

# Run tests
pytest

Notebook, Jupyterlab, Colab, Visual Studio Code
!python -m pip install git+https://github.com/KuantumBS/grikod2.git
```
---

## Citation

If this library was useful to you in your research, please cite us. Following the [GitHub citation standards](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), here is the recommended citation.

### BibTeX


### APA

```
Keçeci, M. (2025). Grikod2 [Data set]. WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.13.1

Keçeci, M. (2025). Grikod2. GitHub, PYPI, Anaconda, Zenodo. https://doi.org/10.5281/zenodo.15352206

```

### Chicago

```
Keçeci, Mehmet. Grikod2 [Data set]. WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.13.1

Keçeci, Mehmet. "Grikod2". Zenodo, 06 Mayıs 2025. https://doi.org/10.5281/zenodo.15352206

```


### Lisans (Türkçe) / License (English)

```
This project is licensed under the MIT License.

```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FWhiteSymmetry%2Fgrikod2.svg?type=shield&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2FWhiteSymmetry%2Fgrikod2?ref=badge_shield&issueType=license)

# Pixi:

[![Pixi](https://img.shields.io/badge/Pixi-Pixi-brightgreen.svg)](https://prefix.dev/channels/bilgi)

pixi init grikod2

cd grikod2

pixi workspace channel add https://repo.prefix.dev/bilgi --prepend

✔ Added https://repo.prefix.dev/bilgi

pixi add grikod2

✔ Added grikod2 >=1.1.4,<2

pixi install

pixi shell

pixi run python -c "import grikod2; print(grikod2.__version__)"

### Çıktı: 1.1.4

pixi remove grikod2

conda install -c https://prefix.dev/bilgi grikod2

pixi run python -c "import grikod2; print(grikod2.__version__)"

### Çıktı: 1.1.4

pixi run pip list | grep grikod2

### grikod  1.1.4

pixi run pip show grikod2

Name: grikod2

Version: 1.1.4

Summary: Converts binary numbers to Gray Code. Grikod2 (Gray Code, Grey Code)

Home-page: https://github.com/KuantumBS/grikod2

Author: Mehmet Keçeci

Author-email: Mehmet Keçeci <...>

License: MIT License

Copyright (c) 2025 Mehmet Keçeci

