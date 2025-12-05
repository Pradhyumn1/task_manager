# Contributing to To-Do List API

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, Django version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - why is this enhancement useful?
- **Possible implementation** (optional)

### Pull Requests

1. **Fork** the repository
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Write tests** for your changes
5. **Run the test suite** to ensure everything passes:
   ```bash
   python manage.py test
   ```
6. **Commit your changes** with clear commit messages:
   ```bash
   git commit -m "Add amazing feature"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Open a Pull Request**

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/todo-list-api.git
   cd todo-list-api
   ```

2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Run tests:
   ```bash
   python manage.py test
   ```

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions small and focused
- Write self-documenting code

## Testing Guidelines

- Write tests for all new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Test both success and failure cases

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add user registration endpoint
Fix task filtering bug (#123)
Update README with deployment instructions
```

## Project Structure

```
todo_django/
├── todo_project/       # Main project settings
├── tasks/             # Tasks app
├── authentication/    # Authentication app
├── manage.py
└── requirements.txt
```

## Questions?

Feel free to open an issue with the `question` label!

Thank you for contributing! 🚀
