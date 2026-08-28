# Level 3 Task 2 — Interactive Dashboard (Tableau Public)

Windows/Mac was the assumption, but **Tableau Public runs in a browser on Ubuntu** — no install, no Wine, free. This is the fastest path to a real, publishable "data visualization tool" dashboard.

## Why Tableau Public (not Power BI)
- Power BI Service needs a work/school email; Power BI Desktop is Windows-only.
- Tableau Public is free, browser-based, works on Ubuntu, and is *explicitly allowed* by the task ("Power BI **or Tableau**").
- Publishing gives you a **public URL** to drop into GitHub + LinkedIn.

## Step-by-step (≈20 min)

1. Go to https://public.tableau.com and **sign up** (free, any email).
2. Click **"Create" → "Web Authoring"** (or "Upload workbook/CSV").
3. Upload this file (already prepared, in your project):
   `level1_basic/cleaned_sentiment_dataset.csv`
4. Tableau opens a blank sheet with your columns listed on the left.

### Build 3 visuals + 1 dashboard

**Chart 1 — Bar: sentiment counts**
- Drag `Sentiment` to Columns, drag `Sentiment` to Rows → right-click → Measure → Count.
- You get a bar chart of Positive / Negative / Neutral.

**Chart 2 — Line: likes over time**
- Drag `Timestamp` to Columns (Tableau auto-detects date, choose YEAR).
- Drag `Likes` to Rows → right-click → Measure → Sum.
- A line showing total likes per year.

**Chart 3 — Map or bar: platform breakdown**
- Drag `Platform` to Columns, `Retweets` (SUM) to Rows → bar per platform.
- (Optional) if Tableau reads a country field, drag `Country` to a map.

### Combine into a dashboard
1. Click **"New Dashboard"** (bottom tabs).
2. Drag your 3 sheets onto the canvas.
3. Add a title: "Sentiment & Engagement Dashboard".
4. (Interactive) click a bar and check "Use as Filter" so clicking filters the others.

### Publish
1. Click **"File → Save to Tableau Public"** (or the Publish button).
2. Name it, publish → you get a public link.
3. Copy that link into this README, your GitHub Level-3 repo, and your LinkedIn post.

## Dataset to upload (already in this project)
- Path: `level1_basic/cleaned_sentiment_dataset.csv`
- 710 rows, columns: Text, Sentiment, Timestamp, User, Platform, Hashtags, Retweets, Likes, Country, Year, Month, Day, Hour

## The 3 charts mapped to the task objectives
| Task objective | What you build |
|---|---|
| Import & clean | upload cleaned CSV (cleaning already done in L1-T1) |
| Interactive visualizations | bar (sentiment), line (likes/year), bar/map (platform) |
| Filters & slicers | "Use as Filter" on the sentiment bar |
| Publish & share | Save to Tableau Public → copy public URL |

## Output to record
- [ ] Public dashboard URL: ______________
- [ ] Add URL to `README.md` Level 3 section
- [ ] Add URL to LinkedIn post