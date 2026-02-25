# Testing Strategy

## Overview
This project uses unit testing and integration testing to verify the Quick-Calc calculator.

Unit tests check individual functions such as addition, subtraction, multiplication, division, and clear.

Integration tests verify that different parts of the application work together correctly.

## Testing Pyramid
Most tests in this project are unit tests because they are fast and focus on core logic.
A smaller number of integration tests ensure the full workflow works correctly.

## Black-Box vs White-Box Testing
Unit tests use white-box testing because internal functions are tested directly.
Integration tests use black-box testing because they verify outputs based on inputs.

## Functional vs Non-Functional Testing
Functional testing verifies that calculator operations work correctly.
Non-functional testing such as performance and UI usability was not included.

## Regression Testing
These tests can be reused after future updates to ensure existing features still work.

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_add | Unit | Pass |
| test_subtract | Unit | Pass |
| test_multiply | Unit | Pass |
| test_divide | Unit | Pass |
| test_divide_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_clear | Unit | Pass |
| test_full_addition_flow | Integration | Pass |
| test_clear_function | Integration | Pass |
