import pytest
from mock import Mock
from mock_example import Person, DB

@pytest.fixture
def mock_db():
    retun Mock(spec=DB)

