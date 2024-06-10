from setuptools import setup, find_packages

setup(
    name="verifyauth",
    version="0.1.0",
    description="Um decorator para FastAPI para verificar autenticação e autorização por meio de um serviço externo Saphira.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Cosme Sousa",
    author_email="cosme.sousa@saphira.com.br",
    url="https://github.com/Cosmess/verifyauth_module",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fastapi"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
