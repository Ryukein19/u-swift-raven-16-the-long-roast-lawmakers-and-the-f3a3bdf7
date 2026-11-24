import os
# One-liner entry (320 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "They will draft a 400-page bill to regulate your model before breakfast, then call IT because their printer is 'hacked' — the printer is out of paper — and declare the hearing postponed until someone fixes the Wi-Fi."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
