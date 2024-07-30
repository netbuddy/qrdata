import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrdata",
    version="0.0.2",
    author="netbuddy",
    author_email="netbuddy@qq.com",
    description="a tool that can generate qrcode from text or file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netbuddy/qrcode",
    project_urls={
        "Bug Tracker": "https://github.com/netbuddy/qrcode/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
    ],
    # package_dir={"": "qrdata"},
    include_package_data=True,  # 包含 MANIFEST.in 文件中指定的数据文件
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['qrdata = qrdata.main:main']},
    install_requires=[
        'chardet>=5.2.0',
        'numpy>=2.0.1',
        'opencv-python>=4.10.0.84',
        'pillow>=10.4.0',
        'pypng>=0.20220715.0',
        'PySide6>=6.7.2',
        'PySide6_Addons>=6.7.2',
        'PySide6_Essentials>=6.7.2',
        'pyzbar>=0.1.9',
        'qrcode>=7.4.2',
        'shiboken6>=6.7.2',
        'typing_extensions>=4.12.2',
        'zxing>=1.0.3'
    ],
    python_requires=">=3.9",
)
