import os
from pathlib import Path


BASE_DIR = Path(os.path.abspath(__file__)).parents[2]
TESTS_DIR = Path(os.path.abspath(__file__)).parents[1]
TESTS_FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures')
