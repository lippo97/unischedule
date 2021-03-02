#!/usr/bin/env python3

from typing import Optional
import yaml
from data import Schedule

def load_data(path) -> Optional[Schedule]:
    with open(path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return Schedule(data['schedule'])
        except yaml.YAMLError:
            return None
