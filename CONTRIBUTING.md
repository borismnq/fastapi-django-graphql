# Contributing to Django GraphQL Federation Template

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `poetry install`
5. Make your changes
6. Run tests and linting
7. Commit your changes
8. Push to your fork
9. Create a Pull Request

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting: `poetry run black .`
- Use isort for import sorting: `poetry run isort .`
- Run pylint for linting: `poetry run pylint apps/ core/`

### Testing

- Write tests for new features
- Ensure all tests pass: `poetry run pytest`
- Aim for high test coverage

### Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Reference issues when applicable

### Pull Requests

- Provide a clear description of the changes
- Link to related issues
- Ensure CI checks pass
- Request review from maintainers

## Questions?

Feel free to open an issue for any questions or concerns.
