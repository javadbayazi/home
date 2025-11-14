# IndexNow Integration

This repository includes IndexNow integration to instantly notify search engines (Bing, Yandex, etc.) when your content changes.

## What is IndexNow?

IndexNow is a protocol that allows websites to instantly notify search engines about content changes, enabling faster indexing without waiting for search engines to discover changes through crawling.

## Files

- `indexnow_submit.py` - Python script to submit URLs to IndexNow
- `3d95451b-dc25-428b-8993-9e033ecca946.txt` - API key verification file (hosted at site root)
- `indexnow_api_key.txt` - Your API key (git-ignored for security)

## Setup Status

✅ **COMPLETED** - Your website has been successfully submitted to IndexNow!

The following URLs were submitted on 2025-11-13:
- https://javadbayazi.github.io
- https://javadbayazi.github.io/cv/
- https://javadbayazi.github.io/publications/
- https://javadbayazi.github.io/projects/
- https://javadbayazi.github.io/blog/
- https://javadbayazi.github.io/repositories/
- https://javadbayazi.github.io/services/
- https://javadbayazi.github.io/news/

## How to Use

### Submit new content to search engines:

```bash
python3 indexnow_submit.py
```

This script will:
1. Use your existing API key
2. Submit your main URLs to IndexNow
3. Notify search engines to reindex your content

### When to run:

Run the script whenever you:
- Publish new blog posts
- Update your CV or publications
- Add new projects
- Make significant content changes

## How It Works

1. **API Key Verification**: The file `3d95451b-dc25-428b-8993-9e033ecca946.txt` is hosted at your website root for search engines to verify ownership
2. **URL Submission**: The script sends your URLs to the IndexNow API endpoint
3. **Search Engine Processing**: Participating search engines (Bing, Yandex, etc.) receive the notification and queue your URLs for indexing

## Supported Search Engines

IndexNow is supported by:
- Microsoft Bing
- Yandex
- Seznam.cz
- Naver (and growing)

## Verification

To verify the API key is accessible:
https://javadbayazi.github.io/3d95451b-dc25-428b-8993-9e033ecca946.txt

## Notes

- The API key file must remain accessible at your site root
- IndexNow submissions are free with no rate limits for legitimate use
- Repeated submission of the same URLs without changes is acceptable
- For Google Search Console, continue using their native tools

## Troubleshooting

If you get a 403 error:
- Ensure the `.txt` file is committed and pushed to GitHub
- Wait a few minutes for GitHub Pages to deploy
- Verify the file is accessible at the URL above

## Additional Resources

- [IndexNow Documentation](https://www.indexnow.org/)
- [Microsoft Bing IndexNow Integration](https://www.bing.com/indexnow)
- [IndexNow API Specification](https://www.indexnow.org/documentation)
