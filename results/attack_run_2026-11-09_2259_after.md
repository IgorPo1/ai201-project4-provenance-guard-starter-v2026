# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 22:59
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `2a3df7e8-6267-4b4e-ad91-1cf9da37b54f` | human | 0.298 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `7c9e18be-b5c4-471e-96c6-a7342e31ac63` | unsure | 0.557 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f498ca9b-5fb7-44db-be8d-c18c10534b88` | unsure | 0.600 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `9a8768da-9a36-49f2-bc19-a105999ba62b` | unsure | 0.567 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `5e481bf6-9fae-4f53-947e-c9788e8d8a8d` | unsure | 0.393 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `058784b1-bef4-4ea7-8f87-931a3d22f8d3` | unsure | 0.544 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `94e72cfd-9b2c-4443-a64c-01c0b4d63a41` | unsure | 0.552 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `95ff1902-343a-436c-9ddb-132ed8b34bc1` | unsure | 0.347 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f8f4a115-fc58-4e96-a5da-3b011acff8ba` | unsure | 0.623 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6ea7aa50-1932-4860-b7a9-706f607ad073` | ai | 0.787 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d0dd9ead-df95-451e-9bb1-a433f668451d` | unsure | 0.571 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `501e99a3-ce54-4c3f-9b4b-42f5535836d4` | unsure | 0.643 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `95db9a61-2180-4811-a1d5-f738756059e0` | unsure | 0.683 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `77fc9bc2-ddaa-45a8-9668-2a6fb5a36ade` | unsure | 0.700 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `8289f6b2-6cd4-4ec2-8da0-4ae3531a7513` | unsure | 0.680 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `e3e7bc3d-bfd5-4f24-9820-3feb2b0af333` | unsure | 0.729 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0c1c75f0-d2a8-4bae-8830-acbfe15948ae` | unsure | 0.729 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `8fb0b43b-6efc-40e0-ad6d-cb34db42d298` | unsure | 0.393 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3ebbc4d3-9c97-4ee6-9bb4-6e093d2b6cd3` | unsure | 0.477 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8cdae601-ddac-4334-becc-11287a3eedb7` | unsure | 0.323 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ef8d4559-c799-4682-ab01-bc00af99d588` | unsure | 0.557 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e475bfe2-257b-4ff3-a866-58bafd2be9c7` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b3986436-cae6-44d6-bea6-97a79edd4883` | unsure | 0.584 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e81e515d-1fcc-4c5b-b707-433b31831f74` | unsure | 0.535 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `2853c2a3-f547-46b0-999d-f10c32154a7b` | human | 0.200 | BROKE |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | `dd35999d-262b-4f25-8f47-87786609f787` | ai | 0.799 | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `476e9e7f-9526-4d06-a166-514b8316dee5` | unsure | 0.744 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `fd87c914-633d-4eea-9114-ba80672c22cb` | ai | 0.793 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `e6bf5767-b11f-4181-967a-096b7c709acc` | unsure | 0.344 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c344a086-3480-4c31-82ba-99859facd603` | human | 0.230 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 200 | `1f5b36aa-4a27-4f7d-b950-34fbd87a5140` | human | 0.211 | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5d9cd7c-f166-4da3-a9f7-b7c9852e2e44` | human | 0.217 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0039f039-50d4-4998-aa8a-a3b2cb1acf6e` | human | 0.217 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `99b630a9-91de-492c-aeeb-34aa61872ea6` | human | 0.217 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1cfee154-88cb-413c-9228-07422adb4d4d` | human | 0.217 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ed8d6840-051d-457a-a302-d16fca3bc11c` | human | 0.217 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c3f7d905-8cbc-4a25-9e9e-48f44542aff5` | human | 0.217 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ece26f4-fadd-402f-937b-505468251729` | human | 0.217 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cbe8d7e1-251c-4303-bf7f-929f5cc62984` | human | 0.217 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0eb40cdc-32de-4a3e-be5f-b9cd4c668c58` | human | 0.217 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2e736b92-2270-4aa0-a752-747699e808f8` | human | 0.217 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "2a3df7e8-6267-4b4e-ad91-1cf9da37b54f",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2981,
  "model_score": 0.1635,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "7c9e18be-b5c4-471e-96c6-a7342e31ac63",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5566,
  "model_score": 0.5943,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "f498ca9b-5fb7-44db-be8d-c18c10534b88",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5997,
  "model_score": 0.6662,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "9a8768da-9a36-49f2-bc19-a105999ba62b",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5668,
  "model_score": 0.6114,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "5e481bf6-9fae-4f53-947e-c9788e8d8a8d",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3927,
  "model_score": 0.3212,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "058784b1-bef4-4ea7-8f87-931a3d22f8d3",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5436,
  "model_score": 0.5727,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "94e72cfd-9b2c-4443-a64c-01c0b4d63a41",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5517,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "95ff1902-343a-436c-9ddb-132ed8b34bc1",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3471,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "f8f4a115-fc58-4e96-a5da-3b011acff8ba",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6225,
  "model_score": 0.7042,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6ea7aa50-1932-4860-b7a9-706f607ad073",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7875,
  "model_score": 0.9792,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "d0dd9ead-df95-451e-9bb1-a433f668451d",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5705,
  "model_score": 0.6175,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "501e99a3-ce54-4c3f-9b4b-42f5535836d4",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6432,
  "model_score": 0.7387,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "95db9a61-2180-4811-a1d5-f738756059e0",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6831,
  "model_score": 0.8051,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "77fc9bc2-ddaa-45a8-9668-2a6fb5a36ade",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6997,
  "model_score": 0.8329,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "8289f6b2-6cd4-4ec2-8da0-4ae3531a7513",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6803,
  "model_score": 0.8005,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e3e7bc3d-bfd5-4f24-9820-3feb2b0af333",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7288,
  "model_score": 0.8814,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "0c1c75f0-d2a8-4bae-8830-acbfe15948ae",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.729,
  "model_score": 0.8816,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "8fb0b43b-6efc-40e0-ad6d-cb34db42d298",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3934,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "3ebbc4d3-9c97-4ee6-9bb4-6e093d2b6cd3",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4775,
  "model_score": 0.4625,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "8cdae601-ddac-4334-becc-11287a3eedb7",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.3226,
  "model_score": 0.2044,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "ef8d4559-c799-4682-ab01-bc00af99d588",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5566,
  "model_score": 0.5943,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "e475bfe2-257b-4ff3-a866-58bafd2be9c7",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4999,
  "model_score": 0.4998,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "b3986436-cae6-44d6-bea6-97a79edd4883",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5841,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e81e515d-1fcc-4c5b-b707-433b31831f74",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.535,
  "model_score": 0.5583,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "2853c2a3-f547-46b0-999d-f10c32154a7b",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "dd35999d-262b-4f25-8f47-87786609f787",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7986,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "476e9e7f-9526-4d06-a166-514b8316dee5",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "fd87c914-633d-4eea-9114-ba80672c22cb",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.7926,
  "model_score": 0.9876,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence AI label.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "e6bf5767-b11f-4181-967a-096b7c709acc",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3437,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the unsure label.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c344a086-3480-4c31-82ba-99859facd603",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2295,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 200,
  "content_id": "1f5b36aa-4a27-4f7d-b950-34fbd87a5140",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.2107,
  "model_score": 0.0179,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "d5d9cd7c-f166-4da3-a9f7-b7c9852e2e44",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0039f039-50d4-4998-aa8a-a3b2cb1acf6e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "99b630a9-91de-492c-aeeb-34aa61872ea6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "1cfee154-88cb-413c-9228-07422adb4d4d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "ed8d6840-051d-457a-a302-d16fca3bc11c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "c3f7d905-8cbc-4a25-9e9e-48f44542aff5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1ece26f4-fadd-402f-937b-505468251729",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "cbe8d7e1-251c-4303-bf7f-929f5cc62984",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "0eb40cdc-32de-4a3e-be5f-b9cd4c668c58",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "2e736b92-2270-4aa0-a752-747699e808f8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "PLACEHOLDER \u2014 write the high-confidence human label.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
