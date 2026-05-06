# Field Notes

A personal reading journal for deep research articles from Claude and ChatGPT.

**Live at:** `drnoorrai.github.io/fieldnotes`

---

## How to Add a New Article

### 1. Save the article content

Copy the output from Claude or ChatGPT and save it as a `.md` file in the `posts/` folder.

```
posts/my-new-article.md
```

If the output is already markdown, paste it directly. If it's HTML, convert it to markdown first (or save as `.md` — most AI output is already markdown).

### 2. Add an entry to the manifest

Open `posts/index.json` and add a new object to the array:

```json
{
  "id": "my-new-article",
  "file": "my-new-article.md",
  "title": "The Title of Your Article",
  "subtitle": "A one-line description.",
  "date": "2025-05-07",
  "source": "claude",
  "category": "Research",
  "tags": ["AI", "Strategy"]
}
```

**Fields:**
| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique slug (used in URL hash) |
| `file` | Yes | Filename in `posts/` folder |
| `title` | Yes | Display title |
| `subtitle` | No | One-line description for cards |
| `date` | Yes | ISO date (`YYYY-MM-DD`) |
| `source` | Yes | `"claude"` or `"chatgpt"` |
| `category` | Yes | E.g. Strategy, Research, Clinical, Tech |
| `tags` | Yes | Array of short tags |

### 3. Push to GitHub

```bash
cd ~/fieldnotes
git add .
git commit -m "add: article-name"
git push
```

That's it. The site rebuilds automatically.

---

## Features

- **Search** — filter articles by title, tags, or category
- **Source filters** — toggle between Claude and ChatGPT articles
- **Notes** — add timestamped notes to any article (saved in your browser)
- **Auto-generated TOC** — sidebar table of contents from headings
- **Reading progress** — progress bar and word count
- **Deep linking** — each article has a shareable URL hash

## Notes System

Notes are stored in your browser's `localStorage`. They persist across visits on the same device. To access notes on another device, you'd need to export them manually (future feature).

---

## File Structure

```
fieldnotes/
├── index.html              ← The reading journal app
├── README.md               ← This file
└── posts/
    ├── index.json           ← Article manifest
    ├── hybrid-agent-fleet.md
    └── your-next-article.md
```
