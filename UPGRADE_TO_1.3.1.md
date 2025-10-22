# Upgrading to v1.3.1

## Critical Fix: Module Name Conflict

Version 1.3.1 fixes a critical bug where both `arc-superset-dialect` and `arc-superset-arrow` packages were using the same module name (`arc_dialect.py`), causing file conflicts and SQLAlchemy entry point registration failures.

## What Changed

### Module Names
- **arc-superset-arrow**: `arc_dialect.py` → `arc_dialect_arrow.py`
- **arc-superset-dialect**: `arc_dialect.py` → `arc_dialect_json.py`

### Driver Names
- **arc-superset-arrow**: `api` → `arrow`
- **arc-superset-dialect**: `api` → `json` (to be implemented)

### Connection Strings
- **Arrow (recommended)**: `arc+arrow://API_KEY@HOST:PORT/DATABASE`
- **JSON**: `arc.json://API_KEY@HOST:PORT/DATABASE`

The connection string format now follows SQLAlchemy's standard `backend+driver://` convention.

## Upgrade Steps

### 1. Uninstall Old Versions
```bash
# As root/sudo in Superset container
pip uninstall arc-superset-dialect arc-superset-arrow -y

# If permission denied, use sudo
sudo pip uninstall arc-superset-dialect arc-superset-arrow -y

# Or manually remove files
sudo rm -rf /usr/local/lib/python3.10/site-packages/arc_dialect.py \
            /usr/local/lib/python3.10/site-packages/arc_superset_*-*.dist-info \
            /usr/local/lib/python3.10/site-packages/__pycache__/arc_dialect.*
```

### 2. Install v1.3.1
```bash
pip install arc-superset-arrow==1.3.1
# or
pip install arc-superset-dialect==1.3.1
# or both (now works without conflicts!)
pip install arc-superset-arrow==1.3.1 arc-superset-dialect==1.3.1
```

### 3. Update Connection Strings

In Superset, update your Arc database connections:

**Old (v1.3.0):**
```
arc://your-api-key@localhost:8000/default
```

**New (v1.3.1):**
```
arc+arrow://your-api-key@localhost:8000/default
```

Or for JSON dialect:
```
arc.json://your-api-key@localhost:8000/default
```

### 4. Test Connection

After updating the connection string, click "Test Connection" in Superset to verify it works.

## Why This Fix Was Needed

The original implementation had multiple issues:

1. **File Conflicts**: Both packages installed a file named `arc_dialect.py` to the same location:
   ```
   /usr/local/lib/python3.10/site-packages/arc_dialect.py
   ```
   When both were installed, the second installation would overwrite the first.

2. **Entry Point Conflicts**: Both packages registered similar entry points, causing SQLAlchemy confusion.

3. **Superset Validation**: The connection string format `arc://` didn't follow SQLAlchemy's `backend+driver://` convention, causing Superset to reject it with: "Invalid connection string, a valid string usually follows: backend+driver://user:password@database-host/database-name"

Now each package has:
- Unique module name (`arc_dialect_arrow.py` vs `arc_dialect_json.py`)
- Proper driver name (`arrow` vs `json`)
- Standards-compliant connection string format (`arc+arrow://` vs `arc.json://`)

## Which Dialect Should I Use?

**Use `arc-superset-arrow` (recommended)**
- Uses Apache Arrow IPC format for data transfer
- 3-5x faster query performance
- More efficient memory usage
- Binary columnar format
- Connection string: `arc+arrow://...`

**Use `arc-superset-dialect` (JSON)**
- Standard JSON response format
- Better for debugging (human-readable)
- Connection string: `arc.json://...`

Both dialects are functionally equivalent and support all Arc features (multi-database, SHOW DATABASES, SHOW TABLES, etc.).

## Docker Installation

If using Docker/Docker Compose, update your Dockerfile:

```dockerfile
FROM apache/superset:latest

USER root
RUN pip install --no-cache-dir arc-superset-arrow==1.3.1
USER superset
```

Then rebuild and restart:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Troubleshooting

### "Can't load plugin: sqlalchemy.dialects:arc"
- Uninstall all old versions completely
- Clear Python cache: `sudo rm -rf /usr/local/lib/python3.10/site-packages/__pycache__/arc_dialect.*`
- Install v1.3.1
- Restart Superset

### "Invalid connection string"
- Make sure you're using the new format: `arc+arrow://...` (with plus sign)
- The old format `arc://` no longer works

### Permission denied during uninstall
- Use `sudo pip uninstall` or manually remove files as root
- Or rebuild your Docker container from scratch
