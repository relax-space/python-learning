import json
import logging
import math
import os
import random
import traceback
import uuid
from collections import UserDict
from datetime import datetime
from functools import partial
from string import Formatter
from typing import Dict, List, OrderedDict, Union


def get_format_params(format_str: str) -> List[str]:
    return [fname for _, fname, _, _ in Formatter().parse(format_str) if fname]


req_param = '''{
        "username": "xiaoxinmiao",
        "password": "1111",
        "lang": "zh_CN"
    }'''


param_list = get_format_params(req_param)

print(param_list)
