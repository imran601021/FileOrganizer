import os

def test_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello")

    # Check file exists
    assert test_file.exists()
    assert test_file.read_text() == "hello"
    