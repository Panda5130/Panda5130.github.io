# panda5130.github.io

Personal site, built by GitHub Pages from plain Markdown and HTML. No local setup needed: edit a file on github.com, commit, and the site redeploys in about a minute.

## Common edits

| To change | Edit |
| --- | --- |
| Bio | `index.html` (the paragraph under the heading) |
| Substack, LinkedIn, GitHub links, email | `links:` and `email:` in `_config.yml` |
| Add a project | Copy `_projects/_template.md` to `_projects/<name>.md` and fill it in |
| Show a project on the home page | Set `featured: true` in that project's front matter |
| Show your latest Substack posts | `substack_feed` in `_config.yml` (your publication URL) |
| Colors and fonts | `assets/css/style.css` |

Project images go in `assets/img/` and are referenced as `/assets/img/<file>`.

## How it deploys

`.github/workflows/deploy.yml` runs on every push to `master`, every Monday, and on demand from the Actions tab. It pulls your latest Substack posts (`scripts/fetch_substack.py`), builds the site with GitHub's own Jekyll action, and publishes it. In **Settings → Pages**, "Source" must be set to **GitHub Actions**.

## Search engines

Paste the Google Search Console verification code into `webmaster_verifications.google` in `_config.yml`, then submit `https://panda5130.github.io/sitemap.xml` in Search Console.
