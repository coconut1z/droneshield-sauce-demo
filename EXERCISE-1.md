# Sauce demo web automation - Exercise 1
Test strategy, test plan, and decisions and reasons components of part 1 of the Droneshield QA tech assessment.

## Test Strategy
### 1. Test Objectives
- End-to-End (E2E) Testing: Ensure the application functions as a whole, covering key user workflows such as login, logout, product selection, and checkout.
- Regression Testing: Validate that changes (bug fixes, enhancements, or new features) do not negatively impact the existing functionality of the application.

### 2. Test Scope
In-Scope:
- Testing core user journeys (login, browsing products, adding items to the cart, checkout, etc.).
- Verifying that interactive UI elements such as buttons, forms, and links work as expected.
- Ensuring that the application handles edge cases (e.g., invalid input, no items in the cart).

Out-of-Scope:
- Non-core features like administration and user account management beyond basic login/logout.
- Performance, security, and load testing (unless specified).

### 3. Test Types
End-to-End Testing:
- Functional Testing: Ensure that users can complete key tasks like logging in, browsing products, adding to the cart, and checking out without errors.
- UI Testing: Ensure that the user interface is intuitive, buttons and forms work as expected, and the layout is consistent.
- Cross-Browser Testing: Test across different browsers (e.g., Chrome, Firefox, Safari) to ensure compatibility.
- User Flow Testing: Simulate the entire customer journey such as from landing on the login page to completing a purchase.

Regression Testing:
- Smoke Testing: Verify that the critical path of the application works after code changes.
- Retesting: Re-run tests for previously identified defects to confirm they are resolved.
- Full Regression: Run all functional tests to ensure no feature was inadvertently broken by recent code changes.

### 4. Test Levels
- Unit Testing: Developers should perform unit tests for individual components.
- Integration Testing: Tests should be conducted to ensure the system's modules (e.g. checkout system and payment gateway) work together as expected.
- System Testing: End-to-end functional tests to ensure the whole system behaves as expected from start to finish.
- Acceptance Testing: Validate that the product meets the acceptance criteria of the business.

### 5. Test Approach
End-to-End Testing:
- Manual Testing: Testers will manually execute scenarios to ensure the overall application works as expected.
- Automated Testing: Automated scripts using Selenium to test the user flows automatically on browsers.

Regression Testing:
- Automated Regression Suite: Maintain a comprehensive suite of automated regression tests that can be executed whenever there are changes to the application.
- Manual Testing: In case of complex workflows or major changes, manual testing may be required.

### 6. Test Environment
- Browsers: Google Chrome
- Devices: Desktop
- Operating Systems: Windows 11
- Test Tools:
    - Selenium
    - Pytest
- Test Data: Use predefined valid and invalid user credentials for login, test product data, and checkout data.

## 7. Defect Management
- Defect Reporting: Bugs will be tracked using Jira or a similar tool. Each defect will be assigned a severity (Critical, Major, Minor) and priority (High, Medium, Low).
- Defect Resolution: The development team will prioritize fixing defects based on severity and impact on user experience.
- Re-testing: Once a defect is fixed, it will be re-tested to ensure it has been resolved and no other issues have been introduced.

## Test Plan
### 1. Test Plan Details
- Test Plan ID: SD-001
- Version: 1.0
- Date: 10/01/25

### 2. Introduction
- Purpose: The purpose of this test plan is to define the testing strategy, scope, and resources for the testing activities related to the Sauce Demo website.
- Application Overview: Sauce Demo is a mock e-commerce website designed for testing purposes. It allows users to log in, view products, add items to the shopping cart, and complete the checkout process.
- Scope: The scope of this test plan includes functional testing and regression testing of various features like user authentication, product browsing, shopping cart management, and checkout processes.

### 3. Test Items
The following components will be tested:
- Login Page: Verifying correct and incorrect login functionality.
- Products Page: Ensuring that products are displayed correctly, including product images, prices, and descriptions.
- Product Page: Verifying that detailed product information is displayed when a user selects a product.
- Cart Page: Ensuring that products have been added to and can be removed from the cart.
- Checkout Process: Verifying that the user can successfully complete a purchase and confirm the order.
- Error Handling: Ensuring that appropriate error messages are displayed for invalid actions (e.g., invalid login credentials).

### 4. Features to be Tested
- Login Functionality: Valid login and invalid login.
- Product Search and Sorting: Ability to browse, filter, and view products.
- Cart Operations: Adding/removing items, checking item quantities, and verifying cart total.
- Checkout Process: Ensuring that users can complete the order with valid (mock) payment information.
- UI/UX: Verify that UI elements like buttons, links, and forms work correctly.

### 5. Test Approach
Test Types:
- Functional Testing: Verify core functionality like login, browsing, cart operations, and checkout.
- Regression Testing: Validate that new code changes do not break existing functionality.
- Usability Testing: Ensure that the application is user-friendly and intuitive.

Test Environment: Testing will be performed in:
- Browsers: Google Chrome
- Operating Systems: Windows 11

Automation Framework: Selenium will be used for automating browser interactions. Pytest will be used for test execution and reporting.

### 6. Test Criteria
Entry Criteria
- All development tasks are completed, and the application is ready for testing.
- The test environment is set up, and the necessary tools are configured.

Exit Criteria
- All test cases have been executed, and the critical defects have been fixed.
- The application passes all functional and usability tests.
- No open critical or major severity defects are remaining.

### 7. Defect Management
Defects will be logged in BUGREPORT-1.md.

Defects will be categorized based on severity:
- Critical: Application crashes, major functionality broken.
- Major: Significant feature not working, high impact on usability.
- Minor: Cosmetic issues, minor bugs with low impact.

Defects will have a priority ranging from High, Medium, and Low.

## Decisions and Reasons
- Python was selected as the language as it is what DroneShield uses. It also allows me a chance to learn a new language on the go.
- Selenium was selected as the web automation tool as I am familiar with it and it can also be written in Python. It provides a simple way to interact with UI elements on web browsers.
- Pytest was selected as the testing framework as it is used for writing and executing test cases, and providing reporting if needed. It works in conjuction with Selenium and can be easily installed through Python/pip.
- The page object model was used as it provides an approach to breaking down and interacting with the website on a framework level. With any updates to the website, the page object model allows for quick updating of the framework/tests where needed. E.g. if locator for the login button is changed, the QA will only need to update the locator in the Login Page without the need to sift through large amounts of code.