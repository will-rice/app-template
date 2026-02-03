# Template Usage Guide

This document provides step-by-step instructions for using this Python project template.

## Quick Setup Checklist

Follow these steps to customize this template for your project:

### 1. Clone or Use Template

```bash
# Using GitHub's "Use this template" button (recommended)
# OR clone directly:
git clone https://github.com/will-rice/app-template.git your-project-name
cd your-project-name
```

### 2. Rename the Package

```bash
# Rename the src/app directory to your project name
mv src/app src/your_project_name
```

### 3. Update pyproject.toml

Replace the TODO comments in `pyproject.toml`:

- `name = "app"` → `name = "your-project-name"`
- Update `description`
- Update `authors` with your name and email
- Update `module-name = ["app"]` → `module-name = ["your_project_name"]`
- Update `known-first-party = ["app"]` → `known-first-party = ["your_project_name"]`
- Update `app = "app.app:main"` → `your_script = "your_project_name.main:main"`
- Add your project dependencies in the `dependencies` list

### 4. Update Package Imports

In `src/your_project_name/__init__.py`, update:
```python
from app.app import main  # Change to:
from your_project_name.main import main
```

### 5. Update Test Files

In `tests/`, update any imports from `app` to `your_project_name`.

### 6. Update README.md

Replace the template README content with your project's documentation.

### 7. Update Docker Configuration (Optional)

If using Docker:
- Update `docker-compose.yml` service name and ports
- Update `dockerfile` if needed for your application

### 8. Initialize Your Repository

```bash
# Remove the existing git history and start fresh
rm -rf .git
git init
git add .
git commit -m "Initial commit from template"

# Set your remote repository
git remote add origin https://github.com/yourusername/your-project.git
git push -u origin main
```

### 9. Install Dependencies

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync --dev
```

### 10. Set Up Pre-commit Hooks

```bash
uv run pre-commit install
```

### 11. Verify Everything Works

```bash
# Run tests
uv run pytest

# Run linting
uv run ruff check

# Run type checking
uv run mypy src/

# Run your application
uv run your-project-name
```

## File-by-File Customization Guide

### Required Changes

| File | What to Change |
|------|---------------|
| `pyproject.toml` | Project name, description, author, dependencies, scripts |
| `src/app/` | Rename directory to your project name |
| `src/app/__init__.py` | Update imports and metadata |
| `README.md` | Replace with your project documentation |

### Optional Changes

| File | What to Change |
|------|---------------|
| `docker-compose.yml` | Service names, ports, environment variables |
| `dockerfile` | Base image, exposed ports, commands |
| `.pre-commit-config.yaml` | Add/remove hooks based on your needs |
| `LICENSE` | Update with your preferred license |

## Common Customizations

### Adding Dependencies

```bash
# Add runtime dependency
uv add requests

# Add development dependency
uv add --dev pytest-asyncio
```

### Changing Python Version

Update `requires-python` in `pyproject.toml`:
```toml
requires-python = ">=3.12"
```

And update `dockerfile` if using Docker:
```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
```

### Adding Entry Points

Add multiple scripts in `pyproject.toml`:
```toml
[project.scripts]
my-cli = "your_project.cli:main"
my-server = "your_project.server:run"
```

### Configuring Ruff

Modify `[tool.ruff.lint]` in `pyproject.toml` to enable/disable rules:
```toml
[tool.ruff.lint]
select = ["C", "E", "F", "I", "W", "D", "N", "B", "A"]  # Add more rule categories
ignore = ["D107", "D203"]  # Add rules to ignore
```

## Template Features

### What's Included

- ✅ Modern Python packaging with uv
- ✅ Ruff for fast linting and formatting
- ✅ MyPy for type checking
- ✅ pytest for testing
- ✅ Pre-commit hooks
- ✅ Docker support
- ✅ Comprehensive .gitignore
- ✅ Google-style docstring configuration

### What You Need to Add

- Your application code
- Your project-specific dependencies
- Tests for your application
- Documentation specific to your project
- CI/CD configuration (GitHub Actions, GitLab CI, etc.)

## Best Practices

1. **Keep dependencies minimal** - Only add what you need
2. **Write tests early** - Add tests as you develop features
3. **Use type hints** - MyPy is configured, take advantage of it
4. **Follow docstring conventions** - Google-style is enforced
5. **Run pre-commit hooks** - They catch issues before commits
6. **Update the README** - Keep documentation current

## Troubleshooting

### Import Errors After Renaming

If you get import errors after renaming the package:
1. Check all imports in `src/` and `tests/`
2. Verify `module-name` in `pyproject.toml` matches your directory name
3. Run `uv sync` to update the environment

### Pre-commit Hook Failures

If pre-commit hooks fail:
1. Fix the reported issues
2. Run `uv run ruff check --fix` to auto-fix
3. Run `uv run ruff format` to format code
4. Commit again

### Docker Build Fails

If Docker build fails:
1. Verify `pyproject.toml` syntax is correct
2. Check that all required files are not in `.dockerignore`
3. Ensure the entry point in `pyproject.toml` is correct

## Next Steps

After setting up your project:

1. **Add your code** - Start developing your application
2. **Write tests** - Add test coverage for your features
3. **Set up CI/CD** - Add GitHub Actions or similar
4. **Configure IDE** - Set up your editor with Python tools
5. **Add documentation** - Write user guides, API docs, etc.

## Support

For issues with the template itself, please open an issue at:
https://github.com/will-rice/app-template/issues

For project-specific questions, refer to your project's documentation.
