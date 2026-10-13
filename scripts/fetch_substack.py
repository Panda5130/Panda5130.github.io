"""Fetch the latest Substack posts into _data/substack.json.

Reads substack_feed from _config.yml. Run by the deploy workflow before
each build; leaves the file untouched if the feed can't be reached.
"""
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

config = open("_config.yml", encoding="utf-8").read()
match = re.search(r'^substack_feed:\s*"?([^"#\s]*)"?', config, re.M)
base = match.group(1).rstrip("/") if match else ""
if not base:
    print("No substack_feed set; skipping.")
    sys.exit(0)

try:
    req = urllib.request.Request(base + "/feed", headers={"User-Agent": "Mozilla/5.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=20).read())
except Exception as e:
    print(f"Could not fetch feed: {e}; keeping existing data.")
    sys.exit(0)

posts = []
for item in root.iter("item"):
    date = item.findtext("pubDate")
    posts.append({
        "title": (item.findtext("title") or "").strip(),
        "url": (item.findtext("link") or "").strip(),
        "date": parsedate_to_datetime(date).date().isoformat() if date else "",
    })

with open("_data/substack.json", "w", encoding="utf-8") as f:
    json.dump(posts[:20], f, indent=2, ensure_ascii=False)
print(f"Saved {len(posts[:20])} posts.")
