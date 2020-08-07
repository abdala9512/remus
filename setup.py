from  setuptools import setup , find_packages


REQUIRED_MODULES = ["pandas", 
                    "boto3",
                    "requests",
                    "json", 
                    "yaml", 
                    "sqlalquemy"]


# Python enhancemente protocol 8 (PEP8)
# PEP8 review with pycodestyle module
# pycodestyle python_script.py
# [file.py]:line_number:column_number: error_code error_description
setup(
    name="remus",
    version="0.1.0",
    description="Recommendation System for music based on Spotify data - Module",
    author="Miguel Arquez Abdala",
    author_email="miguel.arquez12@gmail.com",
    package_dir={"":"remus"},
    install_requires=REQUIRED_MODULES,
    packages=find_packages("remus"),
    include_package_data=False,
    url=""

)
