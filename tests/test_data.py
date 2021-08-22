import pytest
from pathlib import Path
from rdflib import Graph

def test_data(format='turtle'):
    graph = Graph().parse(location="data.ttl", format=format)
