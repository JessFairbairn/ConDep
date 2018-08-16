from unittest import mock
import unittest

from pymunk_cd.parsing.cd_definitions import CDDefinition
from pymunk_cd.primitives import Primitives

class CompoundDefinition(unittest.TestCase):    

    def test_can_take_preceding_definition(self):
        definition = CDDefinition(Primitives.INGEST)
        definition.sense_id = 'fall'
        definition.preceding = CDDefinition(Primitives.PROPEL)
        

    
