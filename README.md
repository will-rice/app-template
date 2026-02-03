# Python Project Template

A modern Python application template with best practices, quality tools, and containerization built-in. Perfect for starting new Python projects quickly with a solid foundation.

## Features

- 🐍 **Python 3.11+** support
- 📦 **Modern dependency management** with [uv](https://github.com/astral-sh/uv) (fast, reliable, easy to use)
- 🧹 **Code quality tools** pre-configured:
  - [Ruff](https://github.com/astral-sh/ruff) - Fast Python linter and formatter
  - [MyPy](https://mypy-lang.org/) - Static type checking
  - [pre-commit](https://pre-commit.com/) - Git hooks for automated checks
- 🧪 **Testing framework** with [pytest](https://pytest.org/)
- 🐳 **Docker** containerization ready
- 📝 **Google-style docstrings** enforced
- 🔧 **Easy to customize** - Replace placeholders with your project details

## Getting Started

### 1. Use This Template

Click the "Use this template" button on GitHub, or clone this repository:

```bash
git clone https://github.com/will-rice/app-template.git my-new-project
cd my-new-project
```

### 2. Customize for Your Project

Update the following files with your project details:

1. **`pyproject.toml`**:
   - Change `name = "app"` to your project name
   - Update `description`, `authors`, and other metadata
   - Add/remove dependencies as needed
   - Update `module-name` in `[tool.uv.build-backend]`
   - Update `known-first-party` in `[tool.ruff.lint.isort]`
   - Update script entry point in `[project.scripts]`

2. **`README.md`**: Replace this content with your project documentation

3. **`src/app/`**: Rename the `app` directory to your project name

4. **`LICENSE`**: Update with your preferred license

5. **Test imports**: Update test files to import your renamed module

### 3. Install Dependencies

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### 4. Start Developing

Run your application:

```bash
uv run <your-project-name>
```

Or run Python directly:

```bash
uv run python src/<your-project-name>/main.py
```

## Development Workflow

### Code Quality

This template comes with pre-configured tools to maintain high code quality:

#### Linting and Formatting

```bash
# Check for linting issues
uv run ruff check

# Auto-fix linting issues
uv run ruff check --fix

# Format code
uv run ruff format
```

#### Type Checking

```bash
uv run mypy src/
```

#### Pre-commit Hooks

Install pre-commit hooks to automatically check code quality before commits:

```bash
uv run pre-commit install
```

Now checks will run automatically on `git commit`. To run manually:

```bash
uv run pre-commit run --all-files
```

### Testing

Run tests with pytest:

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/

# Run specific test file
uv run pytest tests/test_mymodule.py
```

### Docker

Build and run with Docker:

```bash
# Using Docker Compose (recommended)
docker-compose up --build

# Using Docker directly
docker build -t my-project .
docker run -p 7860:80 my-project
```

Update `docker-compose.yml` and `dockerfile` as needed for your application.

## Project Structure

```
project-root/
├── src/
│   └── app/              # Your main package (rename to your project name)
│       ├── __init__.py
│       └── app.py        # Main application entry point
├── tests/                # Test files
│   └── test_dummy.py
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── .gitignore            # Git ignore patterns
├── .dockerignore         # Docker ignore patterns
├── dockerfile            # Docker image definition
├── docker-compose.yml    # Docker Compose configuration
├── pyproject.toml        # Project configuration and dependencies
├── uv.lock              # Locked dependencies (auto-generated)
├── LICENSE              # Project license
└── README.md            # This file
```

## Configuration Files

### `pyproject.toml`

Central configuration for:
- Project metadata (name, version, authors, etc.)
- Dependencies
- Build system (uv)
- Ruff linting rules
- MyPy type checking settings
- pytest configuration
- Entry point scripts

### `.pre-commit-config.yaml`

Defines git hooks that run automatically:
- Code formatting and linting with Ruff
- Type checking with MyPy
- Test execution with pytest
- File cleanup with standard pre-commit hooks

### Ruff Configuration

Configured with:
- Google-style docstrings
- Import sorting
- Common Python best practices
- Error codes: C (convention), E (error), F (pyflakes), I (import), W (warning), D (docstring), N (naming), B (bugbear)

## Why This Template?

- **Fast setup**: Get a new project up and running in minutes
- **Best practices**: Follows modern Python development standards
- **Consistent quality**: Pre-configured linting, formatting, and type checking
- **Easy to customize**: Clear structure and well-documented configuration
- **Production ready**: Includes Docker support for easy deployment
- **Modern tooling**: Uses uv for fast, reliable dependency management

## Common Tasks

### Adding Dependencies

```bash
# Add a runtime dependency
uv add requests

# Add a development dependency
uv add --dev black
```

### Updating Dependencies

```bash
# Update all dependencies
uv lock --upgrade

# Update specific package
uv lock --upgrade-package requests
```

### Creating a New Module

1. Create a new file in `src/<your-project>/`
2. Add tests in `tests/test_<module>.py`
3. Run tests and linting to verify

### Publishing (Optional)

To publish your package to PyPI:

```bash
# Build the package
uv build

# Upload to PyPI (requires twine or similar)
uv publish
```

## Contributing

When contributing to this template:

1. Follow the existing code style
2. Add tests for new features
3. Ensure all checks pass (`pre-commit run --all-files`)
4. Update documentation as needed

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) by Astral
- Linting and formatting by [Ruff](https://github.com/astral-sh/ruff)
- Type checking by [MyPy](https://mypy-lang.org/)
- Testing with [pytest](https://pytest.org/)
