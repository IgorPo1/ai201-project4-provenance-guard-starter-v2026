"""
Settings for Provenance Guard.

Everything you're likely to change lives here, at the top, on purpose.

You'll edit the thresholds in Milestone 5 and the rate limits in unit 8.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# `127.0.0.1` is loopback — only your own machine can reach it, which is what
# you want all through units 7 and 8. A host somewhere else has to accept
# traffic from outside the box, and that means `0.0.0.0`. Setting the env var
# is how you get it; the default keeps your local `curl` commands unchanged.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5001"))

# Flask's debug mode gives anyone who can reach the service an interactive
# Python prompt inside your process. Fine on loopback, a gift to strangers
# anywhere else — so it turns itself off the moment HOST isn't loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# Your first signal runs a language model ON YOUR OWN MACHINE. No account, no
# key, no card. It downloads about 550 MB the first time — do that before
# class, not during it.
#
# What it measures: how *predictable* your text is to a language model. Text a
# model finds easy to predict tends to be text a model wrote.
#
# The first call is the slow one — ten to twenty seconds while the model loads,
# longer on an older laptop. After that it stays in memory and a submission
# takes a second or two. That cost is part of what you're learning: this is
# what running a model inline in a request actually looks like.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words, which is enough for the signal to mean something.
DETECTOR_MAX_TOKENS = 400


# ─── Scoring (Milestone 4) ───────────────────────────────────────────────────
# How much each signal counts toward the combined score.
#
# ⚠️ These are placeholders. Milestone 4 asks you to write your combining rule
# down BEFORE you code it, and to put the numbers in your README. Whatever you
# decide, it goes here.

# Model signal weighted at 0.6, style signal at 0.4.
# Rationale: the perplexity-based model signal is harder to fool with cosmetic
# changes (typos, sentence breaks). The style signal is cheaper to game, so it
# gets a lower weight to reduce false positives from evasion tricks.
WEIGHT_MODEL_SIGNAL = 0.6
WEIGHT_STYLE_SIGNAL = 0.4


# ─── Thresholds (Milestone 5) ────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# ⚠️ This is where your false-positive decision from Milestone 1 actually gets
# made. Widening the unsure band means fewer wrong accusations and more AI text
# getting through. There is no setting that avoids the trade — only settings
# that decide who pays for it.

# Improvement (Unit 8, Milestone 5): lowered HUMAN_THRESHOLD from 0.35 to 0.30.
#
# Diagnosis: attack EV01 (AI text with deliberate typos) scored combined=0.346
# and was labelled "human" before this change. Typos corrupt the model signal
# (GPT-2 cannot predict misspelled tokens → high perplexity → low AI score)
# while simultaneously inflating the style signal's type-token ratio (each
# unique typo counts as a new word). The combined score of 0.346 fell just
# inside the original HUMAN_THRESHOLD of 0.35 — a narrow band that a targeted
# typo pass was able to exploit.
#
# The fix: require combined score < 0.30 to earn the "human" label.
# EV01 at 0.346 now lands in "unsure" — the honest answer, because the system
# genuinely cannot tell whether the unusual token distribution is caused by
# human quirks or deliberate corruption.
#
# The cost: texts scoring 0.30–0.35 now see "unsure" instead of "human".
# Checked against criterion 1 personal-writing samples: their combined scores
# range 0.40–0.68, so none are affected by this threshold move.
# Improvement (Unit 8, Milestone 5, second move): raised AI_THRESHOLD from 0.65 to 0.75.
#
# Diagnosis: real human writing landed in the high-confidence AI band. In the
# current attack run, FP03–FP07 (non-native, student essay, technical docs,
# formal template, repeated phrase) scored 0.68–0.73 and were labelled "ai".
# A personal sample from the criterion-1 eval ("Just finished reading that
# book…") scored 0.657 and was labelled "ai" too.
#
# The fix: 0.75 sits above the highest of those scores (0.729) with 0.02 of
# margin, because identical input can score a little differently between runs.
# Those texts now land in "unsure" instead of being accused.
#
# The cost: any text scoring 0.65–0.75 that really is AI-written now gets
# "unsure" instead of "ai". The only known AI-written sample in the attack set
# that scores above the old line is EV10 (0.787), which still gets "ai". No
# labelled AI samples in the 0.65–0.75 band were tested, so that cost is
# unmeasured. Also, with the style signal still stubbed at 0.5, the combined
# score is 0.6 × model + 0.2, so the "ai" label now needs a model score of
# about 0.92 or higher. It is reachable, but rare.
HUMAN_THRESHOLD = 0.30
AI_THRESHOLD = 0.75

# ⚠️ One thing that catches people out in Milestone 5. A weighted average can
# only land between its two inputs — so while `style_signal` is still the stub
# returning 0.5, the combined score can never leave 0.25–0.75 no matter what
# the model signal says, and the human label needs a model score below 0.20 to
# be reachable at all.
#
# If a label you can't reach is the problem, the fix is upstream of the
# thresholds: a style signal that actually varies. `scoring.label_ranges()`
# prints the bands; the reachable range is a different question.


# ─── Rate limiting (UNIT 8) ──────────────────────────────────────────────────
# Off in unit 7. You turn it on and choose the numbers in unit 8, Milestone 1.
#
# Think about two people: a real writer submitting their own work a few times
# an hour, and a script sending a thousand variations to map your thresholds.
# Your README has to say why your numbers and not others.

# Set to True to turn rate limiting on.
# Numbers chosen for two users in mind:
#   - A real writer submitting their own work: typically a handful of pieces per
#     session, maybe 5–10 in an hour. 10/minute is generous for that.
#   - A script mapping thresholds by sending variations: needs hundreds or
#     thousands of requests. 10/minute = 600/hour makes threshold-mapping
#     impractical without waiting a very long time.
#   - 200/day: a prolific writer could submit 20 pieces across 10 sessions.
#     200/day leaves them room while making a scanning script infeasible.
RATE_LIMITING_ENABLED = True

RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 100

# Flask-Limiter warns loudly without this. In-memory is right for one laptop
# and wrong for anything real — a restart forgets every count, and two copies
# of the service wouldn't share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"