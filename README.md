# 🚀 CI/CD Learning Journey

Welcome to this repository! This project serves as a hands-on playground for me to deepen my understanding and practical skills in Continuous Integration (CI) and Continuous Delivery (CD).

---

## 🎯 Purpose

My primary goal with this repository is to:

* **Learn GitHub Actions:** Explore and master the capabilities of GitHub Actions as a robust CI/CD platform.

* **Automate Workflows:** Understand how to automate various stages of the software development lifecycle, including building, testing, and potentially deploying code.

* **Improve Efficiency:** Implement automated processes to reduce manual effort, catch issues early, and streamline development workflows.

* **Enhance Knowledge:** Gain practical experience with industry-standard CI/CD practices and principles.

---

## 🛠️ Project Structure

This repository contains a simple Python program (`my_program.py`) and its corresponding unit tests (`test_my_program.py`). The CI/CD pipeline is configured using GitHub Actions.

Here's a breakdown of the key files:

* `config.py`:

    ```python
    def greet():
        print("Hello World")
    ```

    A basic Python script demonstrating a simple function.

* `test_config.py`:

    ```python
    import unittest
    # ... (full test code)
    ```

    Unit tests written using Python's built-in `unittest` framework to verify the functionality of `my_program.py`.

* `.github/workflows/python-tests.yml`:

    ```yaml
    name: Python Program and Unit Tests
    # ... (full workflow code)
    ```

    The GitHub Actions workflow definition that automates the testing process.

---

### How the CI/CD Works

The `python-tests.yml` workflow is configured to run automatically on:

* Every `push` to the `main` and `develop` branches.

* Every `pull_request` targeting the `main` and `develop` branches.

When triggered, the workflow performs the following steps:

1.  **Checks out the code:** Retrieves the latest code from the repository.

2.  **Sets up Python:** Configures the environment with multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12) to ensure compatibility.

3.  **Installs dependencies:** Although this specific project has no external dependencies, this step is included as a best practice for future expansion (e.g., installing from `requirements.txt`).

4.  **Runs Unit Tests:** Executes all tests defined in `test_my_program.py` using `python -m unittest discover`.

---

## 🌱 Learning and Growth

> "The only way to do great work is to love what you do." - Steve Jobs

Through this repository, I aim to continuously experiment with different CI/CD patterns, explore advanced GitHub Actions features, and ultimately apply these learnings to build more robust and efficient software solutions.
