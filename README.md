# App Template

A Python application template built with Gradio for quick web app development.

## Features

- 🐍 Python 3.11+ support
- 🎨 Gradio web interface
- 🐳 Docker containerization
- 🧹 Code quality tools (Ruff, MyPy, pre-commit)
- 🧪 Testing with pytest
- 📦 Modern Python packaging with uv

## Quick Start

### Local Development

1. **Install dependencies:**

   ```bash
   uv sync
   ```

2. **Run the application:**

   ```bash
   uv run app
   ```

3. **Access the app:**
   Open your browser to `http://localhost:80`

### Docker

1. **Build and run with Docker Compose:**

   ```bash
   docker-compose up --build
   ```

2. **Access the app:**
   Open your browser to `http://localhost:7860`

## Development

### Code Quality

This project uses several tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **pytest**: Testing framework
- **pre-commit**: Git hooks for automated checks

### Running Tests

```bash
uv run pytest
```

### Linting and Formatting

```bash
uv run ruff check
uv run ruff format
```

### Type Checking

```bash
uv run mypy src/
```

## Project Structure

```
app-template/
├── src/app/           # Main application code
├── tests/             # Test files
├── dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

## Configuration

The application is configured through `pyproject.toml`, which includes:

- Project metadata and dependencies
- Ruff linting rules
- MyPy type checking settings
- pytest configuration

## License

This project is licensed under the terms specified in the LICENSE file.
