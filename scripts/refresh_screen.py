# Re-pulls TTM ratios + price/market cap for the watchlist into data/screen.json. Check numbers before presenting.
import json,re,html,urllib.request,datetime
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/124"}
NOW=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M (Bangkok, UTC+7)")
S=json.load(open("data/screen.json"))
def num(x):
  try: return float(x.replace('%','').replace(',','').replace('+',''))
  except: return None
for it in S["items"]:
  t=urllib.request.urlopen(urllib.request.Request(it["url"],headers=UA),timeout=30).read().decode()
  t=re.sub(r'(?s)<(script|style).*?</\1>','',t);t=html.unescape(re.sub(r'<[^>]+>','|',t));t=re.sub(r'\|[\s|]*','|',t)
  g=lambda k:(lambda m:num(m.group(1)) if m else None)(re.search(re.escape(k)+r'\|([^|]+)\|',t))
  m=re.search(r'Market Cap\|([0-9.,]+[BTM])\|',t);it["mcap_thb"]=m.group(1) if m else None
  dm=re.search(r'\|([0-9.,]+)\|[-+0-9.]+ \([^)]*\)\|(\w{3} \d{1,2}, \d{4})',t);it["price"],it["price_date"]=(dm.group(1),dm.group(2)) if dm else (None,None)
  it.update(chg1y=g('52-Week Price Change'),de=g('Debt / Equity'),debt_ebitda=g('Debt / EBITDA'),icov=g('Interest Coverage'),current=g('Current Ratio'),ebitda_m=g('EBITDA Margin'),net_m=g('Profit Margin'))
S["updated"]=NOW;json.dump(S,open("data/screen.json","w"),ensure_ascii=False,indent=1);print("updated",NOW)
