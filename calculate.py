#!/usr/bin/env python3
"""Reproduce qualitative consistency checks; no ranks, scores or weights."""
import csv,json,pathlib
P=pathlib.Path(__file__).resolve().parent

def table(name):
 with (P/name).open(encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f))
def check():
 selection=table("FINAL_SELECTION.csv")
 matrix=table("SCORE_MATRIX.csv")
 sources=table("SOURCE_REGISTER.csv")
 claims=table("FACT_CLAIM_MAP.csv")
 audit=table("CANDIDATE_AUDIT.csv")
 data=json.loads((P/"RESULTS.json").read_text(encoding="utf-8"))
 assert len(selection)==len(matrix)==15
 assert len(sources)==34 and len(claims)==101 and len(audit)==28
 assert len({x["participant_id"] for x in matrix})==15
 assert len({x["source_id"] for x in sources})==len(sources)
 assert all(set(x["source_ids"].split(";")).issubset({s["source_id"] for s in sources}) for x in selection)
 assert all(x["source_ids"] for x in claims)
 assert data["ranked"] is False and data["shortlist_count"]==15
 assert sorted(len(g["participants"]) for g in data["groups"])==[3,5,7]
 assert not any(key in matrix[0] for key in ("rank","score","weight","position","place"))
 print("PASS: 15 companies, 3 groups (5/3/7), 28 screened, 34 sources, 101 claims, unranked")
if __name__=="__main__": check()
