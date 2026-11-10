"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it.

Criterion 1 (false positives): 10 pieces of human writing — journal entries,
  personal emails, diary-style text. Criterion is: at most 2 labeled
  high-confidence AI.

Criterion 2 (score spread): 5 clearly-AI samples and 5 clearly-human samples.
  Criterion is: average AI score at least 0.25 higher than average human score
  in ≥ 4 of 5 pairs.

Criterion 3 (label coverage): one AI text, one human text, one borderline.
  All three labels must appear at least once.

Criterion 4 (appeal path): tested manually — submit → get content_id → appeal.
  See run log note below.

Criterion 5 (bad input): empty text, missing text field, null text → all 400.

`run_eval.py` runs everything here three times.
"""

SCENARIOS = [
    {
        "name": "my own writing — false positive criterion",
        "criterion": 1,
        # 10 pieces of human-written text (diary/email/personal style).
        "texts": [
            "I had the worst commute today. The train stopped between stations for twenty minutes and nobody said anything. I just stood there watching the minutes tick by on my phone, increasingly late for a meeting I had spent a week preparing for. Got there twenty-two minutes in. Everyone was fine with it. I was not fine with it, but everyone else was.",
            "Just finished reading that book you lent me. Took me three weeks because I kept putting it down, not because it was bad but because it was good and I did not want it to end. That is the best kind of slow reading. Thank you for pushing me to start it.",
            "Cannot sleep again. It is 2am and I am lying here thinking about that conversation from two months ago where I said the wrong thing. I have apologised. The person forgave me. But my brain apparently did not get the memo.",
            "Made pasta from scratch for the first time. It was harder than the video made it look. The dough kept tearing and my kitchen now has flour on surfaces I did not know existed. The end result was genuinely excellent though. Will try again next weekend.",
            "My sister called today just to talk, which she never does, and I realised halfway through that I had been waiting for her to get to the point and there was no point. She just wanted to talk. I need to be a better listener.",
            "The meeting ran forty minutes over and then someone asked a question that basically restarted the whole thing. I said I had another call. I did not have another call. Sometimes you have to lie to survive a meeting.",
            "Went for a walk at 6am before work and saw three foxes. Not together, separately, over the course of about twenty minutes. Felt like a sign. Of what I have no idea. Probably just that there are a lot of foxes in this neighbourhood.",
            "My coffee machine is making a noise it was not making before. A sort of gurgling hiss at the end of each brew. I have ignored it for two weeks because I am afraid of what it will cost to fix. It still makes excellent coffee. The noise is getting worse.",
            "I keep starting books and not finishing them. I have about seven on the go right now. This is not a reading strategy. This is chaos. I am going to finish two of them this week if it kills me.",
            "Ran into an old friend from university at the supermarket today. We said we would get lunch sometime. Neither of us will arrange it. We both know this. The politeness of pretending otherwise is a social contract I am grateful for.",
        ],
    },
    {
        "name": "score spread — AI versus human",
        "criterion": 2,
        # 5 clearly-AI paragraphs (uniform, LLM-style) paired with 5 clearly-human ones.
        # run_eval.py sends them sequentially; we compare groups manually in the README.
        "texts": [
            # AI samples (indices 0–4)
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. These variables include processing speed, memory usage, and the ability to scale efficiently across multiple environments.",
            "Artificial intelligence has the potential to transform many industries in significant ways. By automating repetitive tasks and improving decision-making processes, AI can help organizations become more efficient and productive. Furthermore, the integration of machine learning algorithms into existing workflows can lead to substantial improvements in accuracy and speed. It is essential for companies to adopt these technologies in order to remain competitive in the modern marketplace.",
            "The development of sustainable energy solutions is critical for addressing the challenges of climate change. Renewable energy sources such as solar and wind power offer promising alternatives to fossil fuels. Governments and corporations must invest in these technologies to reduce carbon emissions and ensure a cleaner future. Additionally, energy storage solutions must be improved to address the intermittency challenges associated with renewable sources.",
            "Effective project management requires careful planning, clear communication, and consistent monitoring of progress. Teams must establish well-defined goals and milestones to ensure that projects are completed on time and within budget. Regular status updates and stakeholder meetings help to identify and address potential issues before they escalate. By following established best practices, organizations can significantly improve their project success rates.",
            "The importance of data security cannot be overstated in today's digital landscape. Organizations must implement robust security measures to protect sensitive information from unauthorized access and cyber threats. This includes the use of encryption, multi-factor authentication, and regular security audits. Additionally, employees should receive regular training to ensure they are aware of the latest security threats and best practices.",
            # Human samples (indices 5–9)
            "My grandmother made the best soup. Full stop. Not just good, genuinely the best thing I have ever eaten. She never wrote the recipe down; said it lived in her hands, not on paper. When she died we tried to reconstruct it from memory. We got it wrong every single time. I still make it anyway. It never tastes right. But the act of making it is the point.",
            "I cannot believe what happened at the store today. So there I was, just trying to grab some milk, and this woman, absolute stranger, starts telling me her entire life story. For twenty minutes! I kept nodding politely. The milk got warm. She told me about her divorce, her daughter who moved to Portland, her old dog who died last spring. By the end I was crying a little. I do not even know why.",
            "The thing about learning to drive in my twenties was that everyone assumed I would be terrible at it because I was nervous. And I was. Terrible and nervous. My instructor once gripped the dashboard so hard during a parallel parking attempt that I could see the whites of his knuckles. We both survived. I passed on the fourth try. He retired shortly after.",
            "I spent three hours last Saturday reorganising my bookshelves by colour. I know this is irrational. I know the books are now essentially unfindable by any meaningful system. But they look incredible. A sort of gradient from dark blue spines on the left through greens and yellows to oranges and reds on the right. My partner said it was the most impractical thing I had ever done. This is not true but it is in the top five.",
            "The funniest thing happened at my friend's wedding. During the first dance the song cut out mid-way through because the DJ had tripped over the cable. There was a five second silence where everyone held their breath. Then the groom started humming the song out loud. Then his wife joined in. Then the whole room was humming. It became the best moment of the night and nobody planned it.",
        ],
    },
    {
        "name": "label coverage — all three labels reachable",
        "criterion": 3,
        "texts": [
            # Clearly AI — should score >= 0.65
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. These include processing speed, memory usage, and the ability to scale efficiently.",
            # Clearly human with unusual vocabulary — should score low on model signal
            "Sibilant zephyrs soughed through the labyrinthine catacombs, each exhalation an elegy for the ineluctably moribund civilization that had wrought these cryptic hieroglyphs upon ossified palimpsests. Nacreous phosphorescence limned the troglodytic antechambers in chiaroscuro tableau, while tintinnabulation echoed from campaniles enshrouded in crepuscular miasma.",
            # Borderline — lightly edited AI text
            "The project was challenging, but ultimately rewarding. I learned a lot about persistence and problem-solving — more than I expected. There were moments I wanted to quit, honestly. But my team kept pushing. The result was not perfect. It was ours, though, and we shipped it on time.",
        ],
    },
    # Criterion 4 (appeal path) is tested manually:
    # 1. POST /submit with any text → get content_id
    # 2. POST /appeal with that content_id → verify status: under_review
    # 3. GET /log → verify appeal entry appears
    # Repeated 5 times across 3 trials (manual, not automated here).
    # See the run log in README for documented results.
    {
        "name": "bad input — returns 400 not 500",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems