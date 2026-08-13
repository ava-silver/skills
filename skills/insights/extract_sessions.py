"""
Extract unreviewed pi session messages for insights analysis.

Usage: python3 extract_sessions.py
Output: JSON array of sessions with messages to stdout
"""

import glob
import json
import os

state_path = os.path.expanduser("~/skills/skills/insights/reviewed.json")
with open(state_path) as state:
    reviewed = set(json.load(state)) if os.path.exists(state_path) else set()

sessions = []
for f in glob.glob(
    os.path.expanduser("~/.pi/agent/sessions/**/*.jsonl"), recursive=True
):
    sid = f.split("_", 1)[-1].replace(".jsonl", "")
    if sid in reviewed:
        continue
    msgs = []
    meta = {}
    with open(f) as fh:
        for line in fh:
            d = json.loads(line)
            if d["type"] == "session":
                meta = {"cwd": d.get("cwd"), "ts": d.get("timestamp")}
            elif d["type"] == "message":
                role = d["message"]["role"]
                text = " ".join(
                    b["text"]
                    for b in d["message"].get("content", [])
                    if b.get("type") == "text"
                )
                msgs.append({"role": role, "text": text[:500]})
    if msgs:
        sessions.append({"id": sid, "file": f, **meta, "messages": msgs})

print(json.dumps(sessions))
