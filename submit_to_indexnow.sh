#!/bin/bash

# IndexNow URL Submission Script
# This script submits your website URLs to IndexNow for faster indexing

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=================================================="
echo "IndexNow URL Submission"
echo "=================================================="
echo ""

# Check if Python virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install requests
else
    source .venv/bin/activate
fi

# Check if requests library is installed
if ! python -c "import requests" 2>/dev/null; then
    echo "📦 Installing required Python packages..."
    pip install requests
fi

# Run the submission script
echo "🚀 Submitting URLs to IndexNow..."
echo ""
python indexnow_submit.py

# Check exit status
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "✅ Submission completed!"
    echo "=================================================="
    echo ""
    echo "📋 Next steps:"
    echo "1. Check Bing Webmaster Tools: https://www.bing.com/webmasters/"
    echo "2. Monitor indexing status in the URL Inspection tool"
    echo "3. Run this script again whenever you publish new content"
    echo ""
else
    echo ""
    echo "=================================================="
    echo "❌ Submission failed"
    echo "=================================================="
    echo ""
    echo "Please check the error messages above and try again."
    exit 1
fi
