from pathlib import Path

from ckan.lib.helpers import clean_html
from pglast import parse_sql

assert Path("ckan.ini").is_file()
assert clean_html("<p>Hello</p><script>alert(1)</script>") == "<p>Hello</p>"
assert "javascript:" not in clean_html('<a href="javascript:alert(1)">link</a>')
assert len(parse_sql("SELECT 1")) == 1
assert len(parse_sql("SELECT 1; SELECT 2")) == 2
