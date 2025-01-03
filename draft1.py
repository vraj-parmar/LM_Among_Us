import streamlit as st

# Initialize Session State

if 'puzzle_code' not in st.session_state:
    st.session_state.puzzle_code = {
        "Decrypt Data (Crossword)": ["AKSHAR", "SHASTRIJI", "NEASDEN", "YOGIJI", "KESHAV", "SHREEJI", "BHAGATJI", "GUNATIT", "PRAMUKH", "MANDIR"],
        "Log Retrieval (Library Book)": ["A7R2", "P4Q1", "XCG7", "F8O3", "B9R3", "UI8J", "KQH1", "8Z46", "AQEW", "07CR"],
        "Pattern Patch (Celebrity Puzzle)": ["Z8H6X2P5", "S3K9R7W1", "Q2F4Y6J8", "L1N7G5U3", "V4I6M9O2", "A7C5T1D8", "B9R3X2Z6", "H8Q1J4Y7", "BWI3KD8J", "DB37DKI9"],
        "Book of Riddles": ["7265", "8913", "3452", "6098", "1847", "5321", "9776", "4203", "6834", "1579"],
        "Crewmate Camouflage (Where's Wally)": ["3752", "8772", "3451", "0499", "6148", "1733", "3046", "2318", "2759", "1142"]
    }

if 'total_progress_bar' not in st.session_state:
    st.session_state.total_progress_bar = {
        "total": 0
    }

def display_banner():
    col1, col2, col3 = st.columns(3)
    st.image("banner.png", )
    st.title('Among Us 2024/5')

def display_form_and_process_submission():
    c = st.container()
    c.subheader("Total Progress Bar")
    col1, col2 = st.columns(2)

    col1.subheader("Form")
    with col1.form("response_form", clear_on_submit=True):
        inp_player = st.selectbox("Player", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        inp_task = st.selectbox("Task", ("Decrypt Data (Crossword)", "Log Retrieval (Library Book)", "Pattern Patch (Celebrity Puzzle)", "Book of Riddles", "Crewmate Camouflage (Where's Wally)"))
        inp_code = st.text_input("Code", "")
        submitted = st.form_submit_button("Submit")

        if submitted:
            col2.empty()
            if is_valid_submission(inp_task, inp_code):
                st.success("Correct")

                update_total_progress_bar()
            else:
                st.warning("Incorrect")
            display_total_progress_bars(c)

def is_valid_submission(task, code):
    if code in st.session_state.puzzle_code.get(task, []):
        st.session_state.puzzle_code[task].remove(code)
        valid = True
    else:
        valid = False
    return valid

def update_total_progress_bar():
    st.session_state.total_progress_bar["total"] = min(1.0, max(0.0, st.session_state.total_progress_bar["total"] + (1/48)))

def display_total_progress_bars(c):
    c.progress(st.session_state.total_progress_bar["total"])
    c.markdown(f"Completed: {round(st.session_state.total_progress_bar['total'] * 100)}%")

if __name__ == "__main__":
    st.set_page_config(layout='wide')
    display_banner()
    display_form_and_process_submission()