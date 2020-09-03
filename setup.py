from distutils.core import setup

setup(name="snshandler",
      version="0.0",
      install_requires=["boto3", "logging"],
      package_dir={"logging-sns-handler": "src"})
