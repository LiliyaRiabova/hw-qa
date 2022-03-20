# Front-End QA Engineer Homework

## B. Mobile App Redesign 

There are two files in `testplan` directory:
- Mobile App Redesign_Test Plan_Canary.odt
The test plan consists of a description of the Scope / Out of Scope, a work plan with a description of the planned types of testing, an example of a bug report, etc.

- Mobile App Redesign _Test_Plan_Test Cases_Canary.xlsx
The file contains two lists:
- Test Cases examples for Mobile App (TC ID, TC Name, Description, Steps, Pass/Fail criteria)
- Test Plan example with date, QA Team responsibility

## D. Implement bubble sort

Bubble sort was implemented in python.  
The directory python contains two files:
- `sorting.py` - an implementation of bubble sort
- `test_sorting.py` - unit tests for the bubble sort implementation

It sorts an array with numbers, strings, or any types that support `>` operator.  
It doesn't sort an array with mixed types, like numbers and strings.

### Run tests
`python3 python/test_sorting.py -v`

### Test output
```
test_sort_empty_list (__main__.BubbleSortTestCase) ... ok
test_sort_list_with_a_single_value (__main__.BubbleSortTestCase) ... ok
test_sort_numeric_list (__main__.BubbleSortTestCase) ... ok
test_sort_non_unique_list (__main__.BubbleSortTestCase) ... ok
test_sort_list_with_negative_values (__main__.BubbleSortTestCase) ... ok
test_sort_alphabetic_list (__main__.BubbleSortTestCase) ... ok
test_sort_floats (__main__.BubbleSortTestCase) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

```