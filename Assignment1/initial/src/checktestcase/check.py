import sys
import os
import glob
import subprocess
import unittest
import shutil
import platform
from antlr4 import *
# from src.test.TestUtils import TestLexer, TestParser
import requests


data = requests.get(
    "https://docs.google.com/spreadsheets/d/1ZaQPt_QLKzFuiSDw3UG0XTGVLwMddEjWfAPYu-PlKd4/edit?usp=sharing")
print(data.text)
# print("12")
