#!/usr/bin/env python3
"""
IndexNow submission script for javadbayazi.github.io
Submits URLs to IndexNow protocol (supported by Bing, Yandex, etc.)
"""

import json
import requests
import uuid
import os
from datetime import datetime

# Configuration
SITE_URL = "https://javadbayazi.github.io"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

# Generate or use existing API key
API_KEY_FILE = "indexnow_api_key.txt"

def generate_api_key():
    """Generate a random API key for IndexNow"""
    return str(uuid.uuid4())

def get_or_create_api_key():
    """Get existing API key or create a new one"""
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as f:
            return f.read().strip()
    else:
        api_key = generate_api_key()
        with open(API_KEY_FILE, 'w') as f:
            f.write(api_key)
        print(f"✓ Generated new API key: {api_key}")
        print(f"✓ API key saved to: {API_KEY_FILE}")
        return api_key

def create_api_key_file(api_key):
    """Create the API key verification file that needs to be hosted"""
    key_filename = f"{api_key}.txt"
    with open(key_filename, 'w') as f:
        f.write(api_key)
    print(f"\n⚠️  IMPORTANT: Upload '{key_filename}' to the root of your website")
    print(f"   It should be accessible at: {SITE_URL}/{key_filename}")
    return key_filename

def get_site_urls():
    """Get main URLs from the website"""
    urls = [
        SITE_URL,  # Homepage
        f"{SITE_URL}/cv/",
        f"{SITE_URL}/publications/",
        f"{SITE_URL}/projects/",
        f"{SITE_URL}/blog/",
        f"{SITE_URL}/repositories/",
        f"{SITE_URL}/services/",
        f"{SITE_URL}/news/",
    ]
    return urls

def submit_to_indexnow(api_key, urls):
    """Submit URLs to IndexNow"""
    
    # Prepare the payload
    payload = {
        "host": "javadbayazi.github.io",
        "key": api_key,
        "keyLocation": f"{SITE_URL}/{api_key}.txt",
        "urlList": urls
    }
    
    print(f"\n📤 Submitting {len(urls)} URLs to IndexNow...")
    print("URLs being submitted:")
    for url in urls:
        print(f"  - {url}")
    
    try:
        # Submit to IndexNow
        response = requests.post(
            INDEXNOW_ENDPOINT,
            headers={
                "Content-Type": "application/json; charset=utf-8"
            },
            json=payload,
            timeout=30
        )
        
        print(f"\n📊 Response Status: {response.status_code}")
        
        # Check response
        if response.status_code == 200:
            print("✅ SUCCESS! URLs submitted successfully to IndexNow")
            print("   Your URLs will be processed by search engines supporting IndexNow")
            print("   (Bing, Yandex, and others)")
            return True
        elif response.status_code == 202:
            print("✅ ACCEPTED! URLs submitted successfully to IndexNow")
            print("   Your URLs have been accepted and will be processed")
            return True
        elif response.status_code == 400:
            print("❌ ERROR: Bad request - Invalid format")
            print(f"   Response: {response.text}")
            return False
        elif response.status_code == 403:
            print("❌ ERROR: Forbidden - Verify your API key file is accessible")
            print(f"   Make sure {SITE_URL}/{api_key}.txt exists and contains the key")
            return False
        elif response.status_code == 422:
            print("❌ ERROR: Unprocessable Entity - URL doesn't belong to the host")
            print(f"   Response: {response.text}")
            return False
        else:
            print(f"⚠️  Unexpected response: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: Failed to submit to IndexNow")
        print(f"   Error: {str(e)}")
        return False

def main():
    print("=" * 70)
    print("IndexNow Submission Tool")
    print(f"Website: {SITE_URL}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Get or create API key
    api_key = get_or_create_api_key()
    
    # Create the API key verification file
    key_filename = create_api_key_file(api_key)
    
    # Get URLs to submit
    urls = get_site_urls()
    
    # Submit to IndexNow
    success = submit_to_indexnow(api_key, urls)
    
    if success:
        print("\n" + "=" * 70)
        print("✅ IndexNow submission completed successfully!")
        print("=" * 70)
        print("\n📝 Next Steps:")
        print(f"1. Copy '{key_filename}' to your GitHub Pages repository")
        print(f"2. Commit and push the file to make it accessible at:")
        print(f"   {SITE_URL}/{key_filename}")
        print("3. Search engines will verify the key and start indexing your URLs")
        print("\n💡 Tip: Run this script whenever you add new content to notify search engines!")
    else:
        print("\n" + "=" * 70)
        print("❌ IndexNow submission failed")
        print("=" * 70)
        print("\n📝 Troubleshooting:")
        print(f"1. Make sure '{key_filename}' is accessible at your site root")
        print("2. Verify your website is accessible")
        print("3. Check that URLs are correctly formatted")
        print("4. Try again in a few minutes")

if __name__ == "__main__":
    main()
