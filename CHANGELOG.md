# Changelog

All notable changes to the Arc Superset Dialect will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-10-08

### Fixed
- **Critical**: `get_table_names()` now correctly uses `SHOW TABLES FROM {schema}` when querying specific databases
  - Previously, schema parameter was ignored and only showed tables from the default database
  - Now properly queries the specified database (e.g., `benchmark`, `production`) when user selects a schema in Superset
  - Fixes issue where selecting a non-default schema would show empty table list

### Changed
- Removed outdated comments about schema parameter not being used
- Cleaned up `get_table_names()` implementation for clarity

## [1.1.0] - 2025-10-08

### Added
- **Multi-Database Support**: Arc databases are now exposed as schemas in Superset
  - `SHOW DATABASES` command to list all available databases
  - Schema filtering in `get_table_names()` to show tables per database
  - Support for cross-database queries (`SELECT * FROM production.cpu`)
  - Documentation for multi-database usage in README

### Changed
- `get_schema_names()` now returns all Arc databases instead of just ["default"]
- `get_table_names()` now filters tables by schema (database) when specified
- Updated README with multi-database examples and usage guide
- Version bumped to 1.1.0 for feature release

### Fixed
- Table discovery now correctly parses SHOW TABLES output for multi-database structure
- Schema parameter is now properly used for database filtering

## [1.0.3] - 2025-10-07

### Fixed
- Table discovery showing partition years (2025) instead of measurement names
- `get_table_names()` now correctly uses first column (measurement name)
- Removed hardcoded fallback tables

## [1.0.2] - 2025-10-07

### Added
- `do_ping()` method for Superset connection testing
- Better error handling in table discovery

## [1.0.1] - 2025-10-07

### Fixed
- Package installation issue - switched from `packages=find_packages()` to `py_modules=["arc_dialect"]`
- Now correctly includes arc_dialect.py in PyPI package

## [1.0.0] - 2025-10-07

### Added
- Initial release of Arc Superset Dialect
- SQLAlchemy dialect implementation for Arc API
- Support for Arc authentication via API keys
- Auto-discovery of tables and measurements
- Docker image with pre-installed dialect
- Comprehensive README with setup instructions
