import streamlit as st

st.set_page_config(page_title="Cork Adventure: 250M Text Quest", layout="centered")

retro_css = """
<style>
body, .stApp, .stMarkdown, .stTextInput, .stButton, .stRadio, .stHeader, .stSubheader {
    font-family: 'Fira Mono', 'Consolas', 'Courier New', monospace !important;
    background: #181818 !important;
    color: #00FF00 !important;
}
.stApp { background: #181818 !important; }
.stMarkdown, .stHeader, .stSubheader, .stTextInput, .stButton, .stRadio {
    color: #00FF00 !important;
}
.retro-box {
    border: 2px solid #00FF00;
    border-radius: 6px;
    background: #101010;
    padding: 18px 18px 10px 18px;
    margin-bottom: 18px;
    font-size: 1.13em;
    box-shadow: 0 0 18px #00FF0033;
}
.retro-prompt {
    color: #00FF00;
    font-weight: bold;
    font-family: inherit;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}
.retro-score {
    color: #FFD700;
    font-weight: bold;
    font-family: inherit;
    margin-bottom: 8px;
}
.retro-end {
    color: #FFD700;
    font-weight: bold;
    font-family: inherit;
    margin-top: 18px;
    font-size: 1.2em;
}
</style>
"""
st.markdown(retro_css, unsafe_allow_html=True)

st.markdown('<div class="retro-box"><span class="retro-prompt">CORK ADVENTURE: 250M TEXT QUEST</span><br>Type your way through a fortune!<br><br>It is a dark and stormy night in Cork. You have just won €250 million. Every decision could change your fate.<br><br><span class="retro-score">Choose carefully. Fortune: 100%</span></div>', unsafe_allow_html=True)

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
    st.markdown(f'<div class="retro-box"><span class="retro-prompt">Scenario {st.session_state.question + 1}:</span><br>{q["question"]}</div>', unsafe_allow_html=True)

    # Options as radio buttons, styled as retro
    choice = st.radio("\n> What will you do?", [opt[0] for opt in q["options"]], key=f"q{st.session_state.question}")

    if st.button("Submit", key=f"submit{st.session_state.question}"):
        selected_idx = [opt[0] for opt in q["options"]].index(choice)
        ans, effect, feedback = q["options"][selected_idx]

        st.session_state.score += effect
        st.session_state.answers.append((q["question"], ans, feedback, effect))
        st.session_state.question += 1

        st.rerun()

else:

    st.markdown('<div class="retro-box retro-end">GAME OVER</div>', unsafe_allow_html=True)
    final_score = max(0, st.session_state.score)
    st.markdown(f'<div class="retro-box"><span class="retro-score">Fortune: {final_score}% of €250 million left</span></div>', unsafe_allow_html=True)

    if final_score >= 80:
        st.markdown('<div class="retro-box">🏅 <b>You are a wealth management pro! Cork\'s newest wise millionaire.</b></div>', unsafe_allow_html=True)
    elif final_score >= 50:
        st.markdown('<div class="retro-box">👏 <b>Not bad! You avoided disaster but have some room to tighten up your planning.</b></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="retro-box">😱 <b>Uh oh...You\'ve fallen for some classic pitfalls. Your fortune needs rescuing!</b></div>', unsafe_allow_html=True)

    st.markdown('<div class="retro-box"><b>Your choices and lessons:</b></div>', unsafe_allow_html=True)
    for i, (q_txt, ans_txt, fb_txt, eff_val) in enumerate(st.session_state.answers, 1):
        st.markdown(f'<div class="retro-box">{i}. <b>{q_txt}</b><br>&gt; Your choice: <i>{ans_txt}</i><br>&gt; Impact: {"+" if eff_val>0 else ""}{eff_val}%<br>&gt; Lesson: {fb_txt}</div>', unsafe_allow_html=True)

    if st.button("Play again"):
        for key in ['score', 'question', 'answers']:
            del st.session_state[key]
        st.rerun()

st.markdown('<hr style="border:1px solid #00FF00;">', unsafe_allow_html=True)
st.markdown('<span style="color:#00FF00;font-family:\'Fira Mono\',\'Consolas\',\'Courier New\',monospace;">*This game is inspired by research into real-life lottery winners. Play again, try new choices, and learn how to stay Cork\'s happiest millionaire!*</span>', unsafe_allow_html=True)
