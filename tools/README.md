# Development Tools

Python utility scripts for portfolio maintenance and development.

## Scripts

### refactor.py
Extracts inline CSS and JavaScript from HTML files into separate external files.
- Parses `<style>` tags and saves to `css/`
- Extracts `<script>` tags and saves to `js/`
- Maintains clean separation of concerns

### build_new_index.py
Rebuilds the main index.html with clean, modular structure.
- Generates semantic HTML5 markup
- Links external CSS and JS files
- Preserves content while improving structure

### generate_cv.py
Generates resume in multiple formats from portfolio data.
- Exports to PDF, DOCX, or plain text
- Uses portfolio content as single source of truth
- Maintains consistent formatting

### clean_files.py
File cleanup and formatting utilities.
- Removes trailing whitespace
- Standardizes line endings
- Formats HTML/CSS/JS for consistency

### fix_links.py
Updates and validates all internal and external links.
- Checks for broken links
- Updates path references after refactoring
- Validates URL formats

### reextract_proper.py
Re-extracts content from backup files during major refactoring.
- Parses backup HTML structure
- Extracts specific sections or components
- Useful for recovering content after structure changes

### restore.py
Restores files from backups when needed.
- Copies from `.backups/` directory
- Preserves original file timestamps
- Useful for rollback scenarios

## Usage

All scripts are designed to run from the project root:

```bash
# From 1portfolio/ directory
python tools/refactor.py
python tools/generate_cv.py --format pdf
```

## Requirements

- Python 3.7+
- Standard library only (no external dependencies required)
- Scripts assume they're run from the portfolio root directory

## Notes

These are maintenance tools for the developer. They are not required for portfolio deployment or normal usage. The live portfolio runs on pure HTML/CSS/JavaScript with no build step.
