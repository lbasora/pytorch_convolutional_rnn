from setuptools import setup, find_packages


setup(
    name="convolutional_rnn",
    description="Pytorch Convolutional RNN",
    packages=find_packages(),
    install_requires=["torch", "typing_extensions"],
)
