#!/bin/bash

# Wappalyzer for python 3 is not a pip package
# so this script will download the repo from Github
# and the wappalyzer module will import from local filesystem
# future work for the datasploit3 org will be to 
# fork the repo and create the necessary files for a pip package


git clone https://github.com/datasploit3/python3-Wappalyzer.git
cp python3-Wappalyzer/Wappalyzer.git domain/
