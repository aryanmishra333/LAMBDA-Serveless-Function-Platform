from utils import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lambda Platform", layout="wide")

st.title("⚡ Serverless Function Platform (Lambda Clone)")

tabs = st.tabs(["🚀 Upload Function", "📂 Manage Functions", "📊 Monitoring Dashboard"])

# ---- Upload Function ----
with tabs[0]:
    st.subheader("Upload a New Function")
    name = st.text_input("Function Name")
    language = st.selectbox("Language", ["python", "javascript"])
    timeout = st.number_input("Timeout (seconds)", value=5, min_value=1)
    code = st.text_area("Function Code", height=300, placeholder="Write your code here...")

    if st.button("Upload"):
        if name and code:
            result = upload_function(name, language, timeout, code)
            st.success(f"Function Uploaded! ID: {result.get('function_id')}")
        else:
            st.warning("Please provide both name and code.")

# ---- Manage Functions ----
with tabs[1]:
    st.subheader("Function Manager")
    functions = get_functions()
    
    # Add language filter
    selected_language = st.selectbox(
        "Filter by Language",
        ["All", "python", "javascript"],
        key="language_filter"
    )
    
    filtered_functions = functions
    if selected_language != "All":
        filtered_functions = [f for f in functions if f[2] == selected_language]
    
    if not filtered_functions:
        st.info(f"No {selected_language} functions found. Try uploading one!")
    
    for func in filtered_functions:
        with st.expander(f"📌 {func[1]} ({func[2]})"):
            st.code(func[3], language=func[2])

            cols = st.columns(4)
            
            runtime = cols[0].radio(
                "Runtime",
                ["Docker", "gVisor"],
                horizontal=True,
                key=f"runtime_{func[0]}"
            )
            
            if cols[0].button("▶ Run", key=f"run_{func[0]}"):
                use_gvisor = runtime == "gVisor"
                res = run_function(func[0], use_gvisor=use_gvisor)
                st.write(res)

            if cols[1].button("📝 Edit Code", key=f"edit_{func[0]}"):
                st.session_state[f"editing_{func[0]}"] = True

            if st.session_state.get(f"editing_{func[0]}", False):
                current_code = get_code(func[0])["code"]
                edited_code = st.text_area("Edit Code", value=current_code, height=200, key=f"code_{func[0]}")
                
                if st.button("Save Changes", key=f"save_{func[0]}"):
                    response = update_code(func[0], edited_code)
                    if "message" in response:
                        st.success(response["message"])
                        st.session_state[f"editing_{func[0]}"] = False
                        st.rerun()
                    else:
                        st.error("Failed to update code")


            if cols[2].button("🗑 Delete", key=f"delete_{func[0]}"):
                response = delete_function(func[0])
                st.warning(response)
                st.rerun()

            if cols[3].button("📄 Logs", key=f"logs_{func[0]}"):
                logs = get_logs(func[0])
                st.json(logs)

# ---- Monitoring ----
with tabs[2]:
    st.subheader("Function Performance Dashboard")
    functions = get_functions()
    
    if not functions:
        st.info("No functions available. Please upload a function first.")
    else:
        func_names = {f[0]: f[1] for f in functions}
        selected = st.selectbox("Choose a function", list(func_names.keys()), format_func=lambda x: func_names[x])
        
        metrics = get_metrics(selected)
        if metrics:
            st.metric("Total Runs", metrics["total_runs"])
            st.metric("Avg Execution Time", f'{metrics["avg_exec_time"]} s')
            st.metric("Avg Memory Usage", f'{metrics["avg_memory_usage"]} bytes')
            st.metric("Avg CPU %", f'{metrics["avg_cpu_percent"]}%')

            logs = get_logs(selected)
            if logs:
                df = pd.DataFrame(logs, columns=["id", "function_id", "exec_time", "mem", "cpu", "status", "timestamp"])
                df["timestamp"] = pd.to_datetime(df["timestamp"])

                st.line_chart(df.set_index("timestamp")[["exec_time"]], use_container_width=True)
                st.bar_chart(df.set_index("timestamp")[["cpu"]], use_container_width=True)
            else:
                st.info("No execution logs available for this function yet.")
        else:
            st.info("No metrics available for this function yet.")
