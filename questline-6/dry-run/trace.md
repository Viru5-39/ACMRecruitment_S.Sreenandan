A = 5

B = 3

SUM = 0

print("Initial: A =", A, ", B =", B, ", SUM =", SUM)

for i in range(1, B + 1):
    
    print(f"\nStep {i}:")
    print("Before: SUM =", SUM)
    SUM = SUM + A
    print(f"Operation: SUM = SUM + A → {SUM}")

print("\nFinal Output:", SUM)


## Trace Table

This table shows the state of the variables at each step of the execution.

| Step        | Variable `i` | Variable `A` | Variable `B` | Condition `i <= B` | Variable `SUM` (Before) | Operation `SUM = SUM + A` | Variable `SUM` (After) |
|-------------|:------------:|:------------:|:------------:|:------------------:|:-----------------------:|:-------------------------:|:----------------------:|
| **Initial** | -            | 5            | 3            | -                  | -                       | -                         | 0                      |
| **Loop 1**  | 1            | 5            | 3            | True               | 0                       | `0 + 5`                   | 5                      |
| **Loop 2**  | 2            | 5            | 3            | True               | 5                       | `5 + 5`                   | 10                     |
| **Loop 3**  | 3            | 5            | 3            | True               | 10                      | `10 + 5`                  | 15                     |
| **Final**   | -            | 5            | 3            | False (Loop ends)  | -                       | -                         | **15**                 |

## Predicted Output

Based on the trace, the full output of the program will be:

Initial: A = 5 , B = 3 , SUM = 0

Step 1:
Before: SUM = 0
Operation: SUM = SUM + A → 5

Step 2:
Before: SUM = 5
Operation: SUM = SUM + A → 10

Step 3:
Before: SUM = 10
Operation: SUM = SUM + A → 15

Final Output: 15
