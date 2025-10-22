# Changelog

All notable changes to the Arc Superset Arrow Dialect will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.3] - 2024-10-22

### Changed
- Version bump to stay in sync with arc-superset-dialect
- No functional changes from 1.3.2

## [1.3.2] - 2024-10-22

### Fixed
- Documentation updates for connection string format

## [1.3.1] - 2024-10-22

### Fixed
- **Critical**: Fixed module name conflict with arc-superset-dialect
  - Renamed module from `arc_dialect` to `arc_dialect_arrow` to avoid file conflicts
  - Changed driver name from `api` to `arrow` for proper SQLAlchemy registration
  - Connection string format: `arc+arrow://...` (follows SQLAlchemy `backend+driver` convention)
  - Fixes SQLAlchemy "Can't load plugin" error when both dialects are installed
  - Fixes Superset validation error "Invalid connection string"

### Changed
- Module name: `arc_dialect.py` → `arc_dialect_arrow.py`
- Driver name: `api` → `arrow`
- Connection string format: `arc://...` → `arc+arrow://...`
- Registers both `arc` (base) and `arc.arrow` (explicit) entry points

## [1.3.0] - 2024-10-21

### Changed
- BREAKING: Updated query endpoint from `/query/arrow` to `/api/v1/query/arrow` for Arc v1.0.0 compatibility
- Requires Arc Core v1.0.0 or later

### Added
- Improved error handling in do_ping() method with better logging

## [1.0.1] - 2024-10-14

### Fixed
- Fixed missing pyarrow dependency in setup.py

## [1.0.0] - 2024-10-12

### Added
- Initial release of Arc Superset dialect with Apache Arrow support
- High-performance binary columnar data format using Apache Arrow IPC
- 28-75% faster query performance compared to JSON serialization
- Support for all standard SQL operations
- Multi-database support with SHOW DATABASES
- Table discovery with SHOW TABLES
- Comprehensive type mapping between DuckDB and SQLAlchemy types
- Connection pooling and session management
