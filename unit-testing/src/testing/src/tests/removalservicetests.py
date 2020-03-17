
from mymodule import RemovalService

from unittest import TestCase
from unittest.mock import patch


class RemovalServiceTest(TestCase):
    """Unit Test class that tests out the RemovalServiceClass"""

    @patch('mymodule.os.path')
    @patch('mymodule.os')
    def test_rm_on_a_nonexistent_file(self, mock_os, mock_path):
        service = RemovalService()

        mock_path.isfile.return_value = False

        service.rm("any_path")

        self.assertFalse(mock_os.remove.called, "The remove call should not go through on a non-existent file")

    @patch('mymodule.os.path')
    @patch('mymodule.os')
    def test_rm_on_an_existing_file(self, mock_os, mock_path):
        mock_path.isfile.return_value = True

        service = RemovalService()
        service.rm("existing filename")

        mock_os.remove.assert_called_with("existing filename")