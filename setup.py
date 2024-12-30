from setuptools import find_packages, setup

setup(
    name="kamera",
    version="0.3.1",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    description="A simple webcam streaming package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cobanov/kamera",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "opencv-python",
        "python-multipart",
    ],
    entry_points={
        "console_scripts": [
            "kamera=kamera.app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
