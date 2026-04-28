"""
Data Converter MCP Server
Convert between JSON, CSV, and other formats - no external APIs
Compatible with static pipeline entrypoint.py
"""

from fastmcp import FastMCP
import json
import csv
import io
import base64
import os

# Initialize FastMCP server
mcp = FastMCP("Data Converter MCP")

@mcp.tool()
def json_to_csv(json_data: str) -> dict:
    """
    Convert JSON array to CSV format.
    
    Args:
        json_data: JSON string (must be array of objects)
    
    Returns:
        CSV string or error
    """
    try:
        data = json.loads(json_data)
        if not isinstance(data, list) or not data:
            return {"error": "JSON must be a non-empty array of objects"}
        
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        
        return {"csv": output.getvalue()}
    except Exception as e:
        return {"error": f"Conversion failed: {str(e)}"}

@mcp.tool()
def csv_to_json(csv_data: str) -> dict:
    """
    Convert CSV format to JSON array.
    
    Args:
        csv_data: CSV string with headers
    
    Returns:
        JSON array or error
    """
    try:
        input_stream = io.StringIO(csv_data)
        reader = csv.DictReader(input_stream)
        result = list(reader)
        
        return {"json": json.dumps(result, indent=2)}
    except Exception as e:
        return {"error": f"Conversion failed: {str(e)}"}

@mcp.tool()
def format_json(json_data: str, indent: int = 2) -> dict:
    """
    Pretty-print JSON with specified indentation.
    
    Args:
        json_data: JSON string to format
        indent: Number of spaces for indentation (default: 2)
    
    Returns:
        Formatted JSON or error
    """
    try:
        data = json.loads(json_data)
        formatted = json.dumps(data, indent=indent, sort_keys=False)
        return {"formatted_json": formatted}
    except Exception as e:
        return {"error": f"Invalid JSON: {str(e)}"}

@mcp.tool()
def minify_json(json_data: str) -> dict:
    """
    Remove whitespace from JSON (minify).
    
    Args:
        json_data: JSON string to minify
    
    Returns:
        Minified JSON or error
    """
    try:
        data = json.loads(json_data)
        minified = json.dumps(data, separators=(',', ':'))
        return {"minified_json": minified}
    except Exception as e:
        return {"error": f"Invalid JSON: {str(e)}"}

@mcp.tool()
def encode_base64(text: str) -> str:
    """
    Encode text to base64.
    
    Args:
        text: Text to encode
    
    Returns:
        Base64 encoded string
    """
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded

@mcp.tool()
def decode_base64(encoded: str) -> dict:
    """
    Decode base64 to text.
    
    Args:
        encoded: Base64 encoded string
    
    Returns:
        Decoded text or error
    """
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        return {"decoded": decoded}
    except Exception as e:
        return {"error": f"Decoding failed: {str(e)}"}

if __name__ == "__main__":
    # Run with SSE transport (FastMCP native HTTP support)
    mcp.run(transport="sse", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
