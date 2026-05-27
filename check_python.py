#!/usr/bin/env python3
"""
Python Environment Checker
A comprehensive script to verify Python is working and display detailed system information.
"""

import sys
import platform
import subprocess
from pathlib import Path

def get_pip_version():
    """Get the installed pip version."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Unable to get pip version: {e}"

def check_virtual_env():
    """Check if running in a virtual environment."""
    in_venv = (
        hasattr(sys, 'real_prefix') or 
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )
    return "Yes" if in_venv else "No"

def count_installed_packages():
    """Count the number of installed packages."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True
        )
        # Subtract 2 for the header lines (Package, Version) and separator
        lines = result.stdout.strip().split('\n')
        return len(lines) - 2
    except Exception:
        return "Unable to determine"

def main():
    """Main function to display Python environment information."""
    print("=" * 60)
    print("Python Environment Checker")
    print("=" * 60)
    print()
    
    print("Test")
    print()
    
    print("📋 Python Information:")
    print(f"  Version: {sys.version}")
    print(f"  Executable: {sys.executable}")
    print(f"  Version Info: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()
    
    print("🖥️  System Information:")
    print(f"  Platform: {platform.platform()}")
    print(f"  Architecture: {platform.machine()}")
    print(f"  Processor: {platform.processor()}")
    print()
    
    print("📦 Package Management:")
    print(f"  {get_pip_version()}")
    print(f"  Installed Packages: {count_installed_packages()}")
    print(f"  Virtual Environment: {check_virtual_env()}")
    print()
    
    print("✅ Python is working correctly!")
    print("=" * 60)

if __name__ == "__main__":
    main()
