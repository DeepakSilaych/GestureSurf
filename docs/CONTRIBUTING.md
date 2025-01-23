# Contributing Guide

## Getting Started

Thank you for considering contributing to the Sign Language Gesture Control project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## How Can I Contribute?

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information
   - Screenshots if applicable

### Suggesting Enhancements

1. Check existing issues for similar suggestions
2. Create a new issue with:
   - Clear description of the enhancement
   - Rationale and use cases
   - Potential implementation approach

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/yourusername/SignLanguageRecogniser_Realtime.git
cd SignLanguageRecogniser_Realtime
```

2. Set up development environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. Run tests:
```bash
python -m pytest tests/
```

## Coding Guidelines

### Python Style Guide

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for classes and functions
- Keep functions focused and modular
- Comment complex logic

### Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issues and pull requests
- Format: `[type]: Brief description`
  - Types: feat, fix, docs, style, refactor, test, chore

### Testing

- Write unit tests for new features
- Ensure all tests pass before submitting
- Include integration tests when needed
- Maintain test coverage

## Project Structure

Follow the existing project structure:
```
src/
├── config/          # Configuration files
├── models/          # ML models and related code
└── utils/           # Utility functions
```

### File Naming

- Use lowercase with underscores
- Be descriptive and clear
- Follow existing patterns
- Add appropriate extensions

## Documentation

### Code Documentation

- Add docstrings to all functions and classes
- Include type hints
- Explain complex algorithms
- Update relevant documentation

### README Updates

- Keep installation instructions current
- Document new features
- Update troubleshooting guides
- Maintain clear examples

## Review Process

1. Submit pull request
2. Address review comments
3. Update documentation
4. Ensure CI/CD passes
5. Await maintainer approval

## Questions?

Feel free to:
- Open an issue for discussion
- Contact maintainers
- Join project discussions

Thank you for contributing!
