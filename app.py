import gradio as gr

# --------- Core logic: Binary Search with step recording --------- #

def parse_array(arr_str: str):
    """
    Parse a comma-separated string of integers into a Python list.
    Raise ValueError with a friendly message if parsing fails.
    """
    if not arr_str or arr_str.strip() == "":
        raise ValueError("Input list cannot be empty.")

    parts = [p.strip() for p in arr_str.split(",") if p.strip() != ""]
    if not parts:
        raise ValueError("Input list cannot be empty.")

    try:
        numbers = [int(p) for p in parts]
    except ValueError:
        raise ValueError("Please enter ONLY integers separated by commas, e.g., 1, 3, 5, 7.")

    return numbers


def binary_search_with_steps(arr_str: str, target_str: str):
    """
    Main function called by Gradio.
    It parses inputs, validates them, runs binary search,
    and returns (result_summary, steps_description).
    """
    # --- 1. Parse and validate input --- #
    try:
        arr = parse_array(arr_str)
    except ValueError as e:
        return f"❌ Input Error: {e}", ""

    if not target_str or target_str.strip() == "":
        return "❌ Input Error: Target value cannot be empty.", ""

    try:
        target = int(target_str)
    except ValueError:
        return "❌ Input Error: Target must be an integer.", ""

    # Binary search requires a sorted list (non-decreasing order).
    sorted_arr = sorted(arr)
    if arr != sorted_arr:
        return (
            "❌ For binary search, the list must be sorted in non-decreasing order.\n"
            f"   Hint: Sorted version of your list is: {sorted_arr}",
            ""
        )

    # --- 2. Run Binary Search and record steps --- #
    steps = []
    low, high = 0, len(arr) - 1
    step_num = 1
    found_index = -1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            steps.append(
                f"Step {step_num}:\n"
                f"  low = {low}, high = {high}, mid = {mid}\n"
                f"  arr[mid] = {mid_value} == target → ✅ FOUND at index {mid}."
            )
            found_index = mid
            break
        elif mid_value < target:
            steps.append(
                f"Step {step_num}:\n"
                f"  low = {low}, high = {high}, mid = {mid}\n"
                f"  arr[mid] = {mid_value} < target {target} → "
                f"move low to mid + 1 ({mid + 1})."
            )
            low = mid + 1
        else:  # mid_value > target
            steps.append(
                f"Step {step_num}:\n"
                f"  low = {low}, high = {high}, mid = {mid}\n"
                f"  arr[mid] = {mid_value} > target {target} → "
                f"move high to mid - 1 ({mid - 1})."
            )
            high = mid - 1

        step_num += 1

    # --- 3. Build final summary message --- #
    if found_index == -1:
        steps.append(
            f"Search finished with low = {low}, high = {high}.\n"
            f"Target {target} was not found in the list."
        )
        summary = f" Result: Target {target} was NOT found in the list."
    else:
        summary = (
            f"✅ Result: Target {target} was found at index {found_index} "
            f"(0-based indexing)."
        )

    steps_md = "\n\n".join(steps)
    return summary, steps_md


# --------- Gradio UI definition --------- #

with gr.Blocks() as demo:
    gr.Markdown(
        """
        #  Binary Search Visualizer
        This app demonstrates **Binary Search** step-by-step.

        - Enter a **sorted** list of integers (comma-separated).
        - Enter a target integer.
        - Click **Run Binary Search** to see each step of the algorithm.
        """
    )

    with gr.Row():
        arr_input = gr.Textbox(
            label="Sorted list of integers (comma-separated)",
            value="1, 3, 5, 7, 9, 11"
        )
        target_input = gr.Textbox(
            label="Target integer",
            value="7"
        )

    run_button = gr.Button("Run Binary Search")

    result_output = gr.Markdown(label="Result Summary")
    steps_output = gr.Markdown(label="Detailed Steps")

    run_button.click(
        fn=binary_search_with_steps,
        inputs=[arr_input, target_input],
        outputs=[result_output, steps_output]
    )

# In Colab we directly launch，and open share=True get internet link
if __name__ == "__main__":
    demo.launch()