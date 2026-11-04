"""Regression coverage for database selection in Arc Arrow URLs."""

from sqlalchemy.engine import make_url

from arc_dialect_arrow import ArcDialect


def _connect(url):
    dialect = ArcDialect()
    args, kwargs = dialect.create_connect_args(make_url(url))
    return dialect.connect(*args, **kwargs)


def test_database_from_url_is_sent_as_arc_database_header():
    connection = _connect("arc+arrow://token@localhost:8000/analytics")
    try:
        assert connection.database == "analytics"
        assert connection.session.headers["X-Arc-Database"] == "analytics"
    finally:
        connection.close()


def test_database_name_is_url_decoded_before_setting_header():
    connection = _connect("arc+arrow://token@localhost:8000/team%20metrics")
    try:
        assert connection.database == "team metrics"
        assert connection.session.headers["X-Arc-Database"] == "team metrics"
    finally:
        connection.close()


def test_missing_database_keeps_existing_default_behavior():
    connection = _connect("arc+arrow://token@localhost:8000")
    try:
        assert connection.database is None
        assert "X-Arc-Database" not in connection.session.headers
    finally:
        connection.close()
