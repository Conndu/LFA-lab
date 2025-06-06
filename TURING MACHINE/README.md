# Binary Counter Turing Machine
## This script implements a Turing machine that counts the number of '1's in a binary string.

# Features:
- Counts '1's in binary strings (e.g., "101", "1111", "0000")
- Marks counted '1's with 'X' on the tape
- Builds a counter using '1's at the end of the tape
- Test strings can be modified in the test_strings list

## How it works:
### The machine scans the input, replaces each '1' with 'X', and adds a '1' to the counter area for each one found.
