import streamlit as st

st.set_page_config(page_title="Advice Game: Hold Onto €250 Million in Cork", layout="centered")

st.title("🎲 Advice Game: Can You Hold Onto €250 Million in Cork?")
st.markdown(
    """
Imagine it's day one after winning €250 million in the lotto. Every decision you make will affect your wealth and happiness. Will you end up richer, happier—or broke? Play to find out!
    """
)

# Initialize the session state
if 'score' not in st.session_state:
    st.session_state.score = 100  # starts at €250 million (metaphorically, 100%)
if 'question' not in st.session_state:
    st.session_state.question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

questions = [
    {
        "question": "Your old school friend calls to ask for a 'small' €2 million loan. What do you do?",
        "options": [
            ("Politely say no and explain you'll be getting advice soon.", 10, "Good boundaries protect your relationships and your fortune."),
            ("Send the money—they've been a good friend.", -15, "Generosity is nice, but big giveaways add up fast. Most winners regret impulsive gifts."),
            ("Ignore the call—avoid conflict.", -5, "Dodging can create more drama and might not discourage future requests."),
        ]
    },
    {
        "question": "You see an online investment promising 50% returns in a month. Do you:",
        "options": [
            ("Run it past a financial advisor first.", 10, "Savvy! Experts help spot scams and vet deals."),
            ("Invest €5 million—after all, you can afford to lose a little.", -20, "Even small-risk gambles add up. This is a classic scam."),
            ("Invest nothing—you're not interested in investments at all.", -5, "Keeping all your money in cash can erode wealth through inflation."),
        ]
    },
    {
        "question": "You're feeling overwhelmed and anxious. What is your next step?",
        "options": [
            ("Book an appointment with a mental health professional.", 10, "Emotional support is crucial after a big win."),
            ("Buy a new mansion to distract yourself.", -10, "Luxuries can’t solve emotional issues—they often make them worse if unmanaged."),
            ("Start spending uncontrollably to feel better.", -25, "Impulsive spending is one of the top reasons winners go broke."),
        ]
    },
    {
        "question": "A distant cousin threatens to sue you for a share. You:",
        "options": [
            ("Consult a reputable lawyer immediately.", 10, "Good legal advice helps you stay protected and calm."),
            ("Offer cash to avoid the hassle.", -10, "Paying out can set a precedent. Legal help is better."),
            ("Post about the issue on social media to get public support.", -15, "Publicity can escalate issues and make you a bigger target."),
        ]
    },
    {
        "question": "Tax season! What’s your approach?",
        "options": [
            ("Hire a tax expert familiar with Irish law.", 10, "Professional guidance prevents nasty surprises."),
            ("Do your own internet research and guess.", -10, "DIY is risky—mistakes can cost millions."),
            ("Ignore it. Winnings are tax-free in Ireland!", -5, "Some winnings are tax-free, but investments and interest are not. Always double-check."),
        ]
    }
]

if st.session_state.question < len(questions):
    q = questions[st.session_state.question]
    st.header(f"Scenario {st.session_state.question + 1}")
    st.write(q["question"])
    for idx, (ans, effect, feedback) in enumerate(q["options"]):
        if st.button(ans, key=f"q{st.session_state.question}_opt{idx}"):
            st.session_state.score += effect
            st.session_state.answers.append((q["question"], ans, feedback, effect))
            st.session_state.question += 1
            st.experimental_rerun()
else:
    # Game Over summary
    st.success("Game Over!")
    st.subheader(f"Your 'fortune' meter: {max(0, st.session_state.score)}% of €250 million left")
    if st.session_state.score >= 80:
        st.write("🏅 You're a wealth management pro! Cork's newest wise millionaire.")
    elif st.session_state.score >= 50:
        st.write("👏 Not bad! You avoided disaster but have some room to tighten up your planning.")
    else:
        st.write("😱 Uh oh...You've fallen for some classic pitfalls. Your fortune needs rescuing!")
    st.markdown("---")
    st.header("Your choices and lessons:")
    for i, (q, a, fb, eff) in enumerate(st.session_state.answers, 1):
        st.markdown(f"**{i}. {q}**\n\n- Your choice: *{a}*\n- Impact: {'+' if eff>0 else ''}{eff}%\n- Lesson: {fb}")

    if st.button("Play again"):
        for key in ['score', 'question', 'answers']:
