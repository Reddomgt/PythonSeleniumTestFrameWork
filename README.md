# Python Selenium Test Framework 🚀

![Python Selenium Test Framework](https://img.shields.io/badge/Python%20Selenium%20Test%20Framework-v1.0-blue.svg) ![GitHub](https://img.shields.io/github/license/Reddomgt/PythonSeleniumTestFrameWork) ![Issues](https://img.shields.io/github/issues/Reddomgt/PythonSeleniumTestFrameWork) ![Forks](https://img.shields.io/github/forks/Reddomgt/PythonSeleniumTestFrameWork) ![Stars](https://img.shields.io/github/stars/Reddomgt/PythonSeleniumTestFrameWork)

Welcome to the **Python Selenium Test Framework**! This repository contains a modular and scalable Selenium-based test automation framework built with Python. It is designed to simplify web application testing by following best practices, including the Page Object Design Pattern and data-driven testing. The framework supports multiple browsers and allows for dynamic browser selection at runtime.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Framework Structure](#framework-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [Links](#links)

## Features 🌟

- **Modular Design**: Organize tests in a way that promotes reuse and maintainability.
- **Page Object Model**: Simplify the code and improve readability by separating page logic from test logic.
- **Cross-Browser Testing**: Run tests across multiple browsers seamlessly.
- **Dynamic Browser Selection**: Choose the browser at runtime for flexible testing.
- **Data-Driven Testing**: Easily run the same tests with different sets of data.
- **Easy Integration**: Works well with CI/CD tools to automate your testing pipeline.

## Installation 🛠️

To get started with the Python Selenium Test Framework, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Reddomgt/PythonSeleniumTestFrameWork.git
   cd PythonSeleniumTestFrameWork
   ```

2. **Install Dependencies**:

   Use pip to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup WebDriver**:

   Make sure to download the appropriate WebDriver for your browser. Place it in your system's PATH or specify its location in the configuration file.

## Usage 📖

To run your tests, you can use the `pytest` command:

```bash
pytest tests/
```

### Example Test

Here is a simple example of a test case using the framework:

```python
from pages.login_page import LoginPage

def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("username", "password")
    assert login_page.is_login_successful()
```

### Dynamic Browser Selection

You can specify the browser type when running the tests:

```bash
pytest --browser chrome
```

This allows you to easily switch between browsers without changing your test code.

## Framework Structure 📁

The framework follows a structured approach to keep everything organized. Here’s a breakdown of the main directories:

```
PythonSeleniumTestFrameWork/
│
├── tests/                # Test cases
│   ├── test_login.py
│   └── test_signup.py
│
├── pages/                # Page Object Models
│   ├── login_page.py
│   └── signup_page.py
│
├── drivers/              # WebDriver binaries
│   ├── chromedriver
│   └── geckodriver
│
├── utils/                # Utility functions
│   ├── config.py
│   └── logger.py
│
└── requirements.txt      # Required packages
```

## Contributing 🤝

We welcome contributions to the Python Selenium Test Framework! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

Please ensure your code follows the existing style and includes tests where applicable.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Links 🔗

For more information and to download the latest releases, visit our [Releases page](https://github.com/Reddomgt/PythonSeleniumTestFrameWork/releases).

Explore the framework and contribute to its growth. If you have any questions, feel free to check the "Releases" section for updates and improvements.

Happy testing! 🧪