# Sauce demo web automation
Part 1 of the Droneshield QA tech assessment.

## Description
This project uses Python and Selenium to perform end to end automation testing of [Swag Labs](https://www.saucedemo.com/).

## Installation
Assuming Python is already installed:
1. Clone the repository
2. Navigate to the project directory
```bash
cd sauce_demo
```
3. Install dependencies
```bash
pip install pytest selenium
```

## Usage
To run the tests, use:
```bash
pytest tests/test_sauce_demo.py -v
```
The "-v" command line option will show verbose output; it'll show the name of each test and is more readable.