import re
from typing import List, Any, Optional

def clean_text(text: str) -> str:
    """
    Cleans the given text by removing special characters and extra spaces, and converting it to lowercase.

    Args:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def chunk_list(lst: List[Any], n: int) -> List[List[Any]]:
    """
    Breaks a list into smaller lists of size n.

    Args:
    lst (List[Any]): The list to be chunked.
    n (int): The chunk size.

    Returns:
    List[List[Any]]: A list of chunks.
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def try_parse_int(value: str, default: Optional[int] = None) -> Optional[int]:
    """
    Attempts to convert a string to an integer. Returns a default value if the conversion fails.

    Args:
    value (str): The string to convert.
    default (Optional[int]): The default value to return if conversion fails.

    Returns:
    Optional[int]: The converted integer or the default value.
    """
    try:
        return int(value)
    except ValueError:
        return default


if __name__ == "__main__":
    # print(clean_text("Hello, World!    This is a test."))
    # print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
    # print(try_parse_int("123"), try_parse_int("abc", default=-1))
