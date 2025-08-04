from setuptools import setup, find_packages

setup(
    name="grikod2",
    use_scm_version=True,  # Sürüm bilgisini setuptools_scm ile alır
    setup_requires=["setuptools", "wheel", "setuptools_scm"],  # Gerekli kurulum bağımlılıkları
    version='1.1.3',
    packages=find_packages(where="src"),  # src dizinindeki modülleri bul
    package_dir={"": "src"},  # src dizinine yönlendirme
    include_package_data=True,  # Ek dosyaları dahil et
    install_requires=[
        # Projenizin bağımlılıklarını buraya ekleyin
    ],
    author="Mehmet Keçeci",
    description="Binary to Gray code conversion package for efficient data encoding.",
    url="https://github.com/KuantumBS/grikod2",
    license="MIT",
    python_requires='>=3.9',
)
