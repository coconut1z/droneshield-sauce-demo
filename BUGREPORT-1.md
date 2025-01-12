# Sauce demo web automation - Bug report 1
Bug report component of part 1 of the Droneshield QA tech assessment.

## Bugs
### Able to checkout with no items in cart
- ID: SD-001
- Description: A user is able to login, navigate to the cart and checkout with no items.
- Steps to reproduce:
    1. Login with username and password: standard_user, secret_sauce
    2. Click the cart button
    3. Click the checkout button
    4. Fill in info for first name, last name, and zip code: Conant, Feng, 1234
    5. Click the continue button
    6. Click the finish button
- Expected result: User is unable to click checkout on the cart page with no items.
- Actual result: User is able to click checkout on the cart page and receive their order confirmation.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Able to add item not found to cart
- ID: SD-002
- Description: A user is able to login, navigate to a product page, edit the url and add the item not found to cart.
- Steps to reproduce:
    1. Login with username and password: standard_user, secret_sauce
    2. Click any product such as Sauce Labs Backpack
    3. Edit query variable in URL to any value not 0-5 (inclusive) such as 6
    4. Add to cart the item not found
    5. Click the cart button
- Expected result: User is unable to add item not found to their cart.
- Actual result: User is able to add item not found to their cart and upon clicking the cart the page does not load.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Cart items persistent across different users
- ID: SD-003
- Description: The user is able to login with the first account, add an item to cart, logout, login with the second account and the cart will have the item from the first account.
- Steps to reproduce:
    1. Login with username and password: standard_user, secret_sauce
    2. Add to cart any product such as Sauce Labs Backpack
    3. Click the menu button and click logout
    4. Login with a different username and password: performance_glitch_user, secret_sauce
    5. Click the cart button
- Expected result: Cart items are not persistent across different user accounts.
- Actual result: Cart items are persistent across different user accounts and products can be added/removed.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Incorrect product images for certain users
- ID: SD-004
- Description: Certain users have incorrect product images.
- Steps to reproduce:
    1. Login with username and password: problem_user, secret_sauce
    2. Verify product images
    3. Click the menu button and click logout
    4. Login with username and password: visual_user, secret_sauce
    5. Verify product images
- Expected result: Product images should correctly match the name and description.
- Actual result: All product images for problem_user are incorrect, the first product image is incorrect for visual_user regardless of sort option.
- Severity: Minor
- Pirority: Low
- Environment: Windows 11, Google Chrome

### UI elements' positions are inconsistent for certain users
- ID: SD-005
- Description: Certain users have UI elements' positions that are inconsistent compared to other users.
- Steps to reproduce:
    1. Login with username and password: visual_user, secret_sauce
    2. Verify Add to cart button location for the last product
    3. Verify cart button location
    4. Click the cart button
    5. Verify checkout button location
- Expected result: UI elements' positions across all users should be consistent.
- Actual result: The visual_user has the last product's add to cart, cart and checkout buttons in positions that are inconsistent with other users.
- Severity: Minor
- Pirority: Low
- Environment: Windows 11, Google Chrome

### Prices displayed on Inventory page are randomised for certain users
- ID: SD-006
- Description: Certain users have displayed prices randomised on the Inventory page and not matching the Inventory Item page.
- Steps to reproduce:
    1. Login with username and password: visual_user, secret_sauce
    2. Note the prices for each product
    3. Click into a product such as Sauce Labs Onesie
    4. Note the price
    5. Click Back to Products
    6. Note the prices which have changed after the inital sign in
- Expected result: Product prices on the Inventory page should remain consistent and match with what's on the Inventory Item page.
- Actual result: Product prices on the Inventory page are randomised and do not match with what's on the Inventory Item page.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Prices displayed on Inventory page are randomised for certain users
- ID: SD-007
- Description: Certain users have displayed prices randomised on the Inventory page and not matching the Inventory Item page.
- Steps to reproduce:
    1. Login with username and password: visual_user, secret_sauce
    2. Note the prices for each product
    3. Click into a product such as Sauce Labs Onesie
    4. Note the price
    5. Click Back to Products
    6. Note the prices which have changed after the inital sign in
- Expected result: Product prices on the Inventory page should remain consistent and match with what's on the Inventory Item page.
- Actual result: Product prices on the Inventory page are randomised and do not match with what's on the Inventory Item page.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Certain users are unable to add/remove items to/from cart
- ID: SD-008
- Description: Certain users are unable to add certain items to the cart and unable to remove items from the cart from the Inventory and Inventory Item page.
- Steps to reproduce:
    1. Login with username and password: problem_user, secret_sauce
    2. Click Add to cart for each item
    3. Click Remove for items that have been added successfully to cart
- Expected result: Users are able to freely add and remove items from to/from cart from the Inventory and Inventory Item page.
- Actual result: The problem_user and error_user are only able to add items 1, 2, and 5 to cart, are unable to remove these items from the Inventory and Inventory Item page, and unable to add items 3, 4 and 6 to cart.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Item redirecting to incorrect inventory item page for certain users
- ID: SD-009
- Description: Clicking on an item in the Inventory page will redirect to the incorrect Inventory Item page.
- Steps to reproduce:
    1. Login with username and password: problem_user, secret_sauce
    2. Click an item such as Sauce Labs Bike Light
    3. Verify the item details
- Expected result: Clicking on an item in the Inventory page redirects to the correct one.
- Actual result: Certain users are not being redirected to the correct Inventory Item page when selecting one from the Inventory page.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Certain users unable to enter checkout information which prevents checking out
- ID: SD-010
- Description: The last name field for checkout information cannot be entered which prevents checking out for certain users.
- Steps to reproduce:
    1. Login with username and password: problem_user, secret_sauce
    2. Click Add to cart for an item such as the first one
    3. Click the cart button and then Checkout
    4. Fill in info for first name and zip code: Conant, 1234
    5. Fill in info for last name: Feng
    6. Click the Continue button
- Expected result: Users are able to fill in checkout info and continue the checkout process
- Actual result: The problem_user is unable to enter data in the last name field, which instead replaces the entire value in the first name field with the last entered character and prevents them from checking out. The error_user is unable to enter data in the last name field but does not affect the first name field.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Certain users unable to sort items on the Inventory page
- ID: SD-011
- Description: The sort element on the Inventory page can be interacted with but certain users are unable to select a sort option.
- Steps to reproduce:
    1. Login with username and password: problem_user, secret_sauce
    2. Click on the Sort element.
    3. Click on any sort option such as Price (low to high)
- Expected result: Users are able sort the items on the Inventory page from the selected sort option.
- Actual result: Certain users are able to click on a sort option but it is not actually being selected and no sorting is applied.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Browser error pop-up on selecting sort option for certain users
- ID: SD-012
- Description: The sort element on the Inventory page can be interacted with but certain users that select a sort option will receive an error pop-up.
- Steps to reproduce:
    1. Login with username and password: error_user, secret_sauce
    2. Click on the Sort element.
    3. Click on any sort option such as Price (low to high)
- Expected result: Users are able sort the items on the Inventory page from the selected sort option.
- Actual result: A browser error-pop up appears for certain users and no sorting is applied.
- Severity: Major
- Pirority: Medium
- Environment: Windows 11, Google Chrome

### Certain users able to continue checkout process when not all checkout info is provided
- ID: SD-013
- Description: Certain users are unable to fill in all checkout info but still able to continue the checkout process
- Steps to reproduce:
    1. Login with username and password: error_user, secret_sauce
    2. Click Add to cart for an item such as the first one
    3. Click the cart button and then Checkout
    4. Fill in info for first name and zip code: Conant, 1234
    5. Fill in info for last name: Feng
    6. Click the Continue button
- Expected result: Users are able to fill in checkout info and continue the checkout process.
- Actual result: Certain users are unable to enter any last name data but are still able to click Continue to progress to the checkout overview.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome

### Certain users unable to finish the checkout process
- ID: SD-014
- Description: Certain users are unable to click finish and complete the checkout process
- Steps to reproduce:
    1. Login with username and password: error_user, secret_sauce
    2. Click Add to cart for an item such as the first one
    3. Click the cart button and then Checkout
    4. Fill in info for first name and zip code: Conant, 1234
    5. Click the Continue button
    6. Click the Finish button
- Expected result: Users are able to complete the checkout process and receive a confirmation.
- Actual result: Certain users can click Finish but the checkout process does not progress.
- Severity: Critical
- Pirority: High
- Environment: Windows 11, Google Chrome