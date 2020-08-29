from setuptools import setup, find_packages


setup(
    name="pytorch_convolutional_rnn",
    description="Pytorch Convolutional RNN",
    packages=find_packages(),
    install_requires=["torch", "typing_extensions"],
)
