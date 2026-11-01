import json,datetime
NOW=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M (Bangkok, UTC+7)")
import urllib.request
tr=json.load(urllib.request.urlopen("https://piyaster11.github.io/thaicreditradar/data/trends.json"))
rows=[]
for k,v in tr["items"].items():
  if v["theme"] not in ("stress","credit","consumer"): continue
  s=[x[1] for x in v["series"]]
  a=sum(s[-4:])/4;b=sum(s[-16:-4])/12
  if b<3: continue
  rows.append(dict(key=k,word=v["word"],label=v["label"],theme=v["theme"],last4=round(a,1),prev12=round(b,1),chg=round((a-b)/b*100),last_week=v["series"][-1][0]))
rows.sort(key=lambda r:-r["chg"])
hint={"layoff_th":("Labour-intensive manufacturing, exporters, retail staff costs","อุตสาหกรรมใช้แรงงานมาก ผู้ส่งออก ค้าปลีก"),"factory_close_th":("Manufacturing / industrial estates, auto parts, SME suppliers","ภาคการผลิต นิคมฯ ชิ้นส่วนยานยนต์ SME"),"rating_th":("Corporate bond issuers, interest in credit ratings","ผู้ออกหุ้นกู้ ความสนใจอันดับเครดิต"),"bankrupt_th":("Broad corporate / SME distress","ความเครียดธุรกิจ/SME ทั่วไป")}
top=[dict(r,hint=hint.get(r["key"],("General","ทั่วไป"))[0],hint_th=hint.get(r["key"],("General","ทั่วไป"))[1]) for r in rows[:3]]
json.dump(dict(updated=NOW,method="Avg of last 4 weeks vs previous 12 weeks, Google Trends TH weekly (0-100), stress/credit/consumer words with base ≥3. Data pulled "+tr["retrieved"] if isinstance(tr.get("retrieved"),str) else "",top=top,all=rows[:10],source="https://piyaster11.github.io/thaicreditradar/"),open("data/stress.json","w"),ensure_ascii=False,indent=1)

