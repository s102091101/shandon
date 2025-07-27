
import streamlit as st

st.set_page_config(page_title="Advice if you won €250 million in Cork", layout="centered")

st.title("Advice if you won €250 million in Cork")
st.subheader("How to keep your windfall—and your peace of mind")

st.markdown(
    """
Congratulations! Imagine you've just won €250 million living in County Cork. You've joined a very exclusive club— but staying wealthy is a lot harder than it looks. Here’s what you need to know to avoid the mistakes so many winners make:
"""
)

advice = [
    ("Lack of Financial Literacy", "Seek advice from certified financial planners and educate yourself about investing, taxes, and wealth management."),
    ("Pressure from Friends and Family", "Set clear boundaries early. Consider working with a lawyer to help manage requests and privacy."),
    ("Overspending & Lifestyle Inflation", "Create a yearly budget. Enjoy some luxuries but focus on sustainability rather than impulse."),
    ("Bad Investments and Scams", "Be cautious with investment pitches. Never commit to opportunities you don’t fully understand, and always get a second opinion from a trusted advisor."),
    ("Emotional and Psychological Struggles", "Take your time adjusting. Speaking to a mental health professional can help manage newfound stress and keep you grounded."),
    ("Legal and Safety Issues", "Consider remaining anonymous if possible. Work with professionals to secure your assets and your privacy."),
    ("Quitting Employment Prematurely", "Don’t rush into leaving your job—routine and purpose are important. Plan a gradual transition."),
    ("Failure to Seek Professional Help", "Assemble a team: at minimum, a financial advisor, a qualified tax specialist, and a reputable lawyer."),
    ("Large Tax Burdens", "Get accurate, location-specific tax advice—Irish tax laws are unique, especially for lotto wins and investments."),
    ("Ingrained Money Attitudes", "Reflect on your own financial habits and what money means to you. Old patterns have a way of resurfacing, even after a big win.")
]

st.header("💡 Top Tips for Winners:")
for i, (title, tip) in enumerate(advice, 1):
    st.markdown(f"**{i}. {title}**")
    st.write(tip)

st.markdown("""
---
*This advice is based on research into the experiences of lottery winners worldwide. If you've won big, take time to plan, protect yourself, and invest in your future!*
""")
