"""Logic tests: call the tool's function directly, no MCP involved."""

from mcp_server.mcp_server import get_documentation_from_database


def test_doc_has_title_body_and_source_as_non_empty_strings():
    doc = get_documentation_from_database()

    assert set(doc) == {"title", "body", "source"}
    for key, value in doc.items():
        assert isinstance(value, str) and value, f"{key} should be a non-empty string"


def test_doc_comes_from_mocked_database():
    doc = get_documentation_from_database()
    assert doc["source"] == "mocked_database"
