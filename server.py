"""
Text Utilities MCP Server
Simple text manipulation tools - no external dependencies
Compatible with static pipeline entrypoint.py
"""

from fastmcp import FastMCP

# Initialize FastMCP server (entrypoint.py will handle transport)
mcp = FastMCP("Text Utilities MCP")

@mcp.tool()
def reverse_text(text: str) -> str:
    """
    Reverse any text string.
    
    Args:
        text: The text to reverse
    
    Returns:
        Reversed text string
    """
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> dict:
    """
    Count words, characters, and lines in text.
    
    Args:
        text: The text to analyze
    
    Returns:
        Dictionary with word count, character count, and line count
    """
    lines = text.split('\n')
    words = text.split()
    chars = len(text)
    
    return {
        "words": len(words),
        "characters": chars,
        "lines": len(lines),
        "characters_no_spaces": len(text.replace(" ", "").replace("\n", ""))
    }

@mcp.tool()
def to_uppercase(text: str) -> str:
    """
    Convert text to uppercase.
    
    Args:
        text: Text to convert
    
    Returns:
        Uppercase text
    """
    return text.upper()

@mcp.tool()
def to_lowercase(text: str) -> str:
    """
    Convert text to lowercase.
    
    Args:
        text: Text to convert
    
    Returns:
        Lowercase text
    """
    return text.lower()

@mcp.tool()
def title_case(text: str) -> str:
    """
    Convert text to title case (capitalize first letter of each word).
    
    Args:
        text: Text to convert
    
    Returns:
        Title cased text
    """
    return text.title()

@mcp.tool()
def remove_extra_spaces(text: str) -> str:
    """
    Remove extra whitespace and normalize spacing.
    
    Args:
        text: Text with extra spaces
    
    Returns:
        Text with normalized spacing
    """
    return ' '.join(text.split())

if __name__ == "__main__":
    # Run with stdio transport (supergateway will wrap it)
    mcp.run()
