import streamlit as st
import json

# Load your quizzes JSON (replace with your path)
with open("quiz_output.json", "r", encoding="utf-8") as f:
    curriculum = json.load(f)

# Sidebar: Section selection
section_titles = [s["title"] for s in curriculum]
section_idx = st.sidebar.selectbox("Choose Section", range(len(section_titles)), format_func=lambda x: section_titles[x])
section = curriculum[section_idx]

# Optional: Subsection selection
subsections = section.get("subsections", [])
if subsections:
    subsection_titles = [s["title"] for s in subsections]
    subsection_idx = st.sidebar.selectbox("Choose Subsection", range(len(subsection_titles)), format_func=lambda x: subsection_titles[x])
    node = subsections[subsection_idx]
else:
    node = section

st.title("Quiz: " + section["title"])
if node.get("title") != section["title"]:
    st.header(node["title"])

# MCQs
quizzes = node.get("quizzes", [])
if not quizzes:
    st.warning("No quizzes available for this section/subsection.")
else:
    score = 0
    for i, q in enumerate(quizzes[:20]):
        st.write(f"**Q{i+1}. {q['question']}**")
        # Unique key for each question so Streamlit can track state
        selected = st.radio(
            f"Choose your answer:",
            q["options"],
            key=f"{section['section_id']}-{node.get('subsection_id','main')}-{i}"
        )
        if "show_answers" not in st.session_state:
            st.session_state["show_answers"] = False
        if st.session_state["show_answers"]:
            if selected == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. Answer: {q['answer']}")
        st.markdown("---")

    # Show answers & score button at the end
    if st.button("Check Answers"):
        st.session_state["show_answers"] = True
        st.experimental_rerun()

    if st.session_state["show_answers"]:
        st.info(f"Your Score: {score}/{min(20, len(quizzes))}")
