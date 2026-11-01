# Thai Credit Brief · สรุปเครดิตไทย
Live: https://piyaster11.github.io/thaicreditbrief/ · Companion: https://piyaster11.github.io/thaicreditradar/

This is training material for the Krungsri CA AI workshop (4 Nov 2026). It shows what 4 Grok Bot routines found, plus a public credit screen, for 12 well-known SET-listed companies. It uses **public information only, with no bank or client data. It is an illustrative screen, not a lending decision or a client/prospect list.**

## Data files (`data/`)
| file | panel | refresh |
|---|---|---|
| briefing.json | 1 Morning briefing | Grok Bot routine (weekdays 07:30). Each item needs `url` |
| ratings.json | 2 Rating watch | Grok Bot routine (daily). Change `flag` to up/down/none/na |
| stress.json | 3 Stress pulse | `python3 scripts/refresh_stress.py` |
| sentiment.json | 4 Sentiment check | Grok Bot on demand |
| screen.json | 5 Credit screen | `python3 scripts/refresh_screen.py` (thresholds are in the file) |
| watchlist.json | names | manual |

After editing: `git commit -am refresh && git push`. Pages republishes in about 1 minute. Set `updated` in Bangkok time.
