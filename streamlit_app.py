import streamlit as st

st.set_page_config(page_title="Advice Game: Hold Onto €250 Million in Cork", layout="centered")

st.title("🎲 Advice Game: Can You Hold Onto €250 Million in Cork?")
st.markdown(
    """
Imagine it's day one after winning €250 million in the lotto. Every decision you make will affect your wealth and happiness. Will you end up richer, happier—or broke? Play to find out!
    """
)

# Initialize session state variables
if 'score' not in st.session_state:
    st.session_state.score = 100  # metaphorical fortune meter (out of 100)
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

    # Options displayed as radio buttons
    choice = st.radio("Choose your action:", [opt[0] for opt in q["options"]])

    if st.button("Submit"):
        # Find selected option index
        selected_idx = [opt[0] for opt in q["options"]].index(choice)
        ans, effect, feedback = q["options"][selected_idx]

        st.session_state.score += effect
        st.session_state.answers.append((q["question"], ans, feedback, effect))
        st.session_state.question += 1

        st.rerun()  # Updated here

else:
    st.success("Game Over!")
    final_score = max(0, st.session_state.score)
    st.subheader(f"Your 'fortune' meter: {final_score}% of €250 million left")

    if final_score >= 80:
        st.write("🏅 You're a wealth management pro! Cork's newest wise millionaire.")
    elif final_score >= 50:
        st.write("👏 Not bad! You avoided disaster but have some room to tighten up your planning.")
    else:
        st.write("😱 Uh oh...You've fallen for some classic pitfalls. Your fortune needs rescuing!")

    st.markdown("---")
    st.header("Your choices and lessons:")
    for i, (q_txt, ans_txt, fb_txt, eff_val) in enumerate(st.session_state.answers, 1):
        st.markdown(f"**{i}. {q_txt}**\n\n- Your choice: *{ans_txt}*\n- Impact: {'+' if eff_val>0 else ''}{eff_val}%\n- Lesson: {fb_txt}")

    if st.button("Play again"):
        for key in ['score', 'question', 'answers']:
            del st.session_state[key]
        st.rerun()  # Updated here

st.markdown(
    """
---
*This game is inspired by research into real-life lottery winners. Play again, try new choices, and learn how to stay Cork's happiest millionaire!*
"""
)
