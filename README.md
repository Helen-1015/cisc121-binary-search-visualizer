# Binary Search Visualizer

A small Python + Gradio app that **visually simulates Binary Search** step by step.  
The user enters a sorted list of integers and a target value, and the app shows how the search range shrinks until the value is found (or not found).

---

## 1. Computational Thinking Breakdown (CT)

This project uses the 4 major components of **Computational Thinking**:

---

## 1.1 Decomposition — Breaking down the problem

I decomposed the full project into smaller tasks:

### **Input handling**
- Read a comma-separated list of integers.
- Read the target integer.

### **Validation**
- Ensure the list is not empty.
- Ensure the string contains only integers.
- Ensure the list is sorted (binary search requires sorted input).

### **Binary Search core algorithm**
- Initialize pointers: `low`, `high`.
- While `low <= high`:
  - Compute `mid`
  - Compare values
  - Move left/right
- Log every step in a human-readable way.

### **User Interface (Gradio)**
- Two textboxes (array + target)
- “Run Binary Search” button
- Display result (found / not found)
- Display detailed step-by-step explanation

---

## 1.2 Pattern Recognition — Recognizing repeated structure

Binary Search always follows the same pattern:

1. Look at the **middle** of the current search interval.
2. If middle < target → discard left half.
3. If middle > target → discard right half.
4. Repeat until found or interval is empty.

This “divide-and-conquer” pattern appears in:
- Guess-the-number games  
- Searching sorted databases  
- Tree-based algorithms  

Recognizing this pattern simplifies the algorithm design and ensures efficiency: **O(log n)**.

---

## 1.3 Abstraction — Focusing on essential ideas

The app hides unimportant details and only shows the essentials:

### **Shown to user**
- Input list and target
- `low`, `high`, `mid` at each step
- Value comparisons
- Each decision: move left, move right, or found

### **Hidden**
- String parsing details
- Exceptions / raw errors
- UI framework internals (event loop, callbacks)

This abstraction keeps the explanation clean and focused.

---

## 1.4 Algorithm Design — High-level flow

### **Binary Search Process**
1. Parse and validate input  
2. Ensure list is sorted  
3. Set `low = 0`, `high = len(arr)-1`  
4. Repeat:
   - `mid = (low + high) // 2`
   - Compare and update range  
5. Return result + step logs  

---

## **Flowchart (text version)**

```
Start
  |
  v
User inputs array + target
  |
  v
Parse & validate
  |
  v
Valid? ---- No ----> Show error and stop
  |
 Yes
  |
  v
low = 0, high = n-1
  |
  v
While low <= high ?
  |         \
  |          \ No -> Output "NOT FOUND"
  v
Compute mid
Compare arr[mid] with target
  |           |            |
  v           v            v
> target   < target      == target
  |           |            |
high=mid-1  low=mid+1   Output "FOUND"
  \___________|__________/
```

# 2. Implementation Details (Python + Gradio)

The entire app is implemented in **app.py**.

---

## 2.1 Core functions

### `parse_array(arr_str)`
- Takes a comma-separated string (e.g., "1, 3, 5, 7").

- Strips whitespace, converts each item to int.

- Raises ValueError with a friendly message if the input is invalid.

### `binary_search_with_steps(arr_str, target_str)`
- Called by Gradio when the user clicks the button.

- Parses and validates both the list and the target.

- Checks that the input list is sorted; if not, it shows the sorted version as a hint.

- Runs the Binary Search loop.

- Returns:

 - A short summary string (found / not found).

 - A multi-line string describing each step.
---

## 2.2 Gradio UI

The UI is built using gr.Blocks:
- One Markdown block for the title and short description.

- A row with two gr.Textbox components:

  - arr_input for the sorted list.

  - target_input for the target.

- A gr.Button called “Run Binary Search”.

- Two gr.Markdown outputs:

  - result_output for the summary.

  - steps_output for the detailed steps.

The button is wired like this:
    
    run_button.click(
    
    fn=binary_search_with_steps,
    
    inputs=[arr_input, target_input],
    
    outputs=[result_output, steps_output]
    )


So every time the user clicks, the function runs and the outputs are updated.

---

# 3. Project Structure


    CISC121-BinarySearch-Project/
  
   │
  
   ├── app.py               # Main Gradio app (Binary Search logic + UI)
   
   ├── README.md            # This documentation file
  
   ├── requirements.txt     # Python dependencies (gradio)
  
   └── Screenshots/         # Example screenshots of the app
      
       ├── test_found.png
       
       ├── test_not_found.png
       
       └── test_error.png



---

# 4. How to Run Locally

- Clone or download this repository:
- Install dependencies (ideally in a virtual environment):
- Run the app:
  python app.py
- Visit the URL printed in the terminal.

---

# 5. Online Demo Links

- GitHub: https://github.com/Helen-1015/cisc121-binary-search-visualizer  
- Hugging Face Space: <YOUR_HF_LINK>  

---

# 6. Testing & Edge Cases

I tested the app with several input cases:

### Normal case- target found
Inout List: `1,3,5,7,9,11`  
Target: `7`

Result: 7 found at index 3 (0-based).

Steps clearly show how low, high, and mid change.

### Not found
List: `1,3,5,7,9`  
Target: `2`

Result: “Target 2 was NOT found.”

Steps show the range eventually becomes invalid (low > high).

### Single-element list（found）
List: `5`  
Target: `5`

Result: found at index `0` 

### Single-element list（not found）
List: `5`  
Target: `7`

Result: not found

### Unsorted list
- List: `5,1,3`

- Target: `3`

- Result: an error message explaining that the list must be sorted,
plus a hint showing the sorted version.

### Invalid input
- Empty list string, missing target, or non-integer characters.

- Result: clear error messages such as
  “Input list cannot be empty.” or
  “Target must be an integer.”

Screenshots are in `Screenshots/`.

---

# 7. AI Usage Declaration

AI tool used: **ChatGPT (OpenAI)**  

I used ChatGPT (OpenAI) as an AI assistant to:

- Brainstorm and refine the project idea (choosing Binary Search).

- Help draft the initial version of the Python + Gradio code.

- Help write and structure this README (decomposition, pattern recognition, abstraction, algorithm design, and flowchart).

- I reviewed, edited, and tested all code myself to make sure it runs correctly and matches the assignment requirements.

This README and code have been customized by me after AI assistance.

Final testing and verification done by me.

---

# 8. Author

- **Name:** Hailin Zhang  
- **Course:** CISC 121 – Algorithm Visualization Project  
- **Algorithm:** Binary Search  




