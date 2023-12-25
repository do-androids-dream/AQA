# AQA

Testcase 1

Summary: [Calculator app] Verify math addition operation functionality with "result preview" field of the app's display

Priority: High

Precondition: Calculator app installed, calculator app is running

Steps:
1. Click on the buttons "5", "+", "3"

Expected results: "result preview" field on the bottom of app's display shows "8"

----------------------
Testcase 2

Summary: [Calculator app] Verify math subtraction operation functionality with "result preview" field of the app's display

Priority: High

Precondition: Calculator app installed, calculator app is running

Steps:
1. Click on the buttons "1", "0", "-", "5"

Expected results: "result preview" field on the bottom of app's display shows "5"

----------------------
Testcase 3

Summary: [Calculator app] Verify handling of impossible math operation functionality

Priority: High

Precondition: Calculator app installed, calculator app is running

Steps:
1. Click on the buttons "3", "/", "0", "="

Expected results: "Can't divide by 0" message is displayed on the application display

---------------------
Testcase 4

Summary: [Calculator app] Verify handling of max value overflow functionality

Priority: High

Precondition: Calculator app installed, calculator app is running

Steps:
1. Click on the buttons "9", "9", "9", "9", "9", "9", "^", "9", "9", "9", "9", "9", "9", "="

Expected results: "Value too large" message is displayed on the application display