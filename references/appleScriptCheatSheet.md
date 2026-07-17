### Control Statements

|                          Keyword                          |                                                  Description                                                  |
|:---------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
|               `if` `then` `else` `else if`                |                        Conditional statement to execute code based on given conditions                        |
|                         `repeat`                          |                                     Marks the beginning of a repeat loop                                      |
|                       `end repeat`                        |                                        Marks the end of a repeat loop                                         |
|                `repeat with... from... to`                |                                       Loops through a series of numbers                                       |
|                   `repeat with...in...`                   |                                       Loops through each item in a list                                       |
|                      `repeat until`                       |                                   Loops until a specified condition is true                                   |
|                      `repeat while`                       |                                Loops as long as a specified condition is true                                 |
|                       `exit repeat`                       |                                   Immediately exits the current repeat loop                                   |
|                `try` `on error` `end try`                 |                               Handles errors that occur during script execution                               |
|                     `tell` `end tell`                     |                             Directs commands to a specific application or object.                             |
| `considering` `ignoring` `end considering` `end ignoring` |                               Specifies how text comparisons should be handled                                |
|               `with timeout` `end timeout`                |                               Sets a time limit for a block of code to execute                                |


---
### More Information

### repeat with...from...to...by

In AppleScript, the repeat with statement with from and to allows for iterating a specific number of times, with a loop variable incrementing or decrementing through a defined range.

Explanation:
- loopVariable: This is a variable that will hold the current value of the iteration. It is automatically declared by AppleScript within the scope of the loop.
- startValue: The initial value assigned to loopVariable at the beginning of the first iteration.
- endValue: The value at which the loop will terminate. The loop continues as long as loopVariable is between startValue and endValue (inclusive).
- by stepValue (Optional): This specifies the increment or decrement value for loopVariable in each iteration. If omitted, the stepValue defaults to 1. A negative stepValue can be used to count downwards.

```shell
repeat with loopVariable from startValue to endValue [by stepValue]
    -- Statements to be repeated
end repeat

```

Example 2

This script will display dialogs showing "Iteration number: 1", "Iteration number: 2", and so on, up to "Iteration number: 5".

```shell
repeat with i from 1 to 5
    display dialog "Iteration number: " & i as string
end repeat
```


Example 3

This script will display dialogs counting down from 10 to 1.

```shell
repeat with j from 10 to 1 by -1
    display dialog "Countdown: " & j as string
end repeat
```

Example 4

This script iterates through a list of fruits, displaying each one in a dialog.

```shell
set myFruits to {"apple", "banana", "orange"}
repeat with k from 1 to (count of myFruits)
    set currentFruit to item k of myFruits
    display dialog "Current fruit: " & currentFruit
end repeat
```

### repeat with...in...

The AppleScript `repeat with...in...` statement is a control flow structure used to iterate over the items within a list or collection. This form of the repeat loop is particularly useful when you need to process each element of a list sequentially.

Explanation
- `repeat with loopVariable in aList` This initiates the loop.
    - `loopVariable` This is a temporary variable that will hold the value of the current item from aList during each iteration of the loop. You do not need to declare this variable beforehand; AppleScript creates it implicitly.
    - `aList` This is the list or collection of items you want to iterate through. It can be a literal list (e.g., {"apple", "banana", "cherry"}) or a variable holding a list.
- `--statements to be executed for each item` This is the body of the loop, containing the commands that will be executed for each item in aList. Inside the loop, you can refer to the current item using loopVariable.
- `end repeat` This marks the end of the repeat loop.

```shell
repeat with loopVariable in aList
    -- statements to be executed for each item
end repeat
```

Example

This script iterates through a list of fruits, displaying each one in a dialog.

```shell
set myFruits to {"apple", "banana", "cherry"}

repeat with currentFruit in myFruits
    display dialog "The current fruit is: " & currentFruit
end repeat

```
Important Considerations

- Loop Variable Scope
  - The `loopVariable` exists only within the scope of the `repeat` loop. 
  - Its value after the loop completes will be the last item it held during the final iteration
- Exiting the Loop
  - You can use the `exit repeat` statement within the loop to prematurely terminate the iteration and continue execution after `end repeat`
- Modifying the List During Iteration
  - Modifying the list you are iterating over withing the loop can lead to unexpected behavior. 
  - If you need to modify the list, it's often safer to create a new list or iterate over a copy

### repeat until

The AppleScript repeat until statement executes a block of code repeatedly until a specified Boolean condition becomes true.

Explanation

- `repeat until Boolean_expression` This initiates the loop. `Boolean_expression` is an expression that evaluates to either `true` or `false`
- `-- Statements to be executed` This represents the block of code that will be executed in each iteration of the loop.
- `end repeat` This marks the end of the repeat until loop.

How it works
- The `Boolean_expression` is evaluated.
- If `Boolean_expression` is `false`, the statements within the loop are executed.
- After the statements are executed, the `Boolean_expression` is evaluated again.
- This process continues until `Boolean_expression` becomes true.
- Once `Boolean_expression` is `true`, the loop terminates, and execution resumes with the statement immediately following `end repeat`

> Important Note: If the `Boolean_expression` is already `true` when the `repeat until` statement is first encountered, the statements within the loop will not be executed even once.

Example

In this example, the dialog will be displayed for counter values from 0 to 5. When counter becomes 6, the repeat until condition (counter is greater than 5) becomes true, and the loop terminates. The final dialog will then show that the counter is 6.

```shell
set counter to 0
repeat until counter is greater than 5
    display dialog "Counter: " & counter
    set counter to counter + 1
end repeat
display dialog "Loop finished. Counter is now: " & counter
```

### repeat while

In AppleScript, the `repeat while` statement repeatedly executes a block of code as long as a specified boolean condition remains `true`

```shell
repeat while <boolean_expression>
    -- Statements to be executed repeatedly
end repeat
```

Explanation

- `repeat while <boolean_expression>` This initiates the loop. The `<boolean_expression>` is evaluated before each iteration.
- `-- Statements to be executed repeatedly` This is the block of code that will be executed if the `<boolean_expression>` evaluates to `true`
- `end repeat` This marks the end of the `repeat while` loop

How it Works

- The `repeat while` loop continues to execute its enclosed statements as long as the boolean expression after `while` evaluates to `true`
- If the boolean expression evaluates to `false` at the beginning of an iteration, the loop terminates, and script execution resumes after `end repeat`
- You can also use the `exit repeat` statement within the loop to prematurely terminate the loop based on an internal condition.

### exit repeat

In AppleScript, the `exit repeat` statement is used to terminate a repeat loop prematurely. 
When `exit repeat` is encountered within a loop, the script execution immediately jumps to the statement following the `end repeat` of that loop.

```shell
repeat
    -- Statements inside the loop
    set userReply to the text returned of (display dialog "Do you want to exit the loop?" default answer "")
    if userReply is "yes" then
        exit repeat -- Exits the loop if the condition is met
    end if
    -- More statements inside the loop
end repeat
-- Script execution resumes here after the loop is exited
```

Key points about exit repeat
- It can be used within any type of repeat loop: `repeat`, `repeat with`, `repeat while`, `repeat until`, and `repeat X times`
- It is often used in conjunction with an `if` statement to conditionally exit a loop based on a specific condition.
- In the case of nested repeat loops, `exit repeat` only exits the innermost loop in which it is placed. 
- There is no direct command to globally exit all nested loops simultaneously.

Example

```shell
set userName to ""

repeat
    display dialog "Please enter your username:" default answer ""
    set userName to text returned of result

    if userName is not equal to "" then
        exit repeat -- Exit the loop if a username is entered
    end if
end repeat

display dialog "Welcome, " & userName & "!"
```

Explanation
- `set userName to ""` Initializes an empty string variable `userName`
- `repeat ...` `end repeat` This creates an infinite loop. The code inside will continue to execute until explicitly told to stop.
- `display dialog "Please enter your username:" default answer ""` Displays a dialog box prompting the user to enter their username. The `default answer ""` ensures the input field is initially empty.
- `set userName to text returned of result` Stores the text entered by the user in the `userName` variable.
- `if userName is not equal to "" then exit repeat` This is the core of the example. It checks if the `userName` variable is not empty. If it contains any text (meaning the user entered something), the `exit repeat` statement is executed, terminating the `repeat` loop.
- `display dialog "Welcome, " & userName & "!"` After the loop is exited, this line displays a welcome message including the entered username.

This script demonstrates how `exit repeat` can be used to break out of a loop based on a specific condition, in this case, ensuring the user provides input before proceeding.