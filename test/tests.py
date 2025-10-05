import os

# tests/test_file_organizer.py
def test_sample_file_creation(tmp_path):
    # Create a file inside temporary test folder
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello")

    # Check file exists
    assert test_file.exists()
    assert test_file.read_text() == "hello"

