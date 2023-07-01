# import language_tool_python


def solve_grammar_mistakes(text):
    """
    This function takes a text as input and corrects any grammar mistakes using LanguageTool library.

    Parameters:
    text (str): The text to be checked and corrected

    Returns:
    str: The corrected text with grammar mistakes fixed
    """
    try:
        # Check if the input text is a string
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")

        # Initialize LanguageTool
        tool = language_tool_python.LanguageTool('en-US')

        # Check and correct grammar mistakes in the text
        corrected_text = language_tool_python.correct(text, tool.check(text))

        return corrected_text
    except TypeError as e:
        # Log the error
        print(f"Error: {e}")
        return ""