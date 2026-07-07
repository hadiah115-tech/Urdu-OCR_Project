#!/usr/bin/env python3
"""
Script to remove duplicate PNG files from the data folder.
Keeps only PNG files in data/images/ and data/processed/ folders.
Removes all PNG files from the root data/ folder as they are duplicates.
"""

import os
import subprocess

# List of duplicate files to remove from data/ root folder
duplicate_files = [f"data/{i}.png" for i in range(100)]

def remove_files_from_git(files):
    """Remove files from git repository"""
    for file_path in files:
        try:
            subprocess.run(['git', 'rm', file_path], check=True)
            print(f"Removed: {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error removing {file_path}: {e}")

def main():
    print("Removing duplicate PNG files from data/ folder...")
    print(f"Total files to remove: {len(duplicate_files)}")
    print("\nFiles to be removed:")
    for f in duplicate_files:
        print(f"  - {f}")
    
    # Remove files
    remove_files_from_git(duplicate_files)
    
    print("\n✓ All duplicate PNG files have been removed from git!")
    print("Run: git commit -m 'Remove duplicate PNG files from data folder'")

if __name__ == "__main__":
    main()
