import streamlit as st
import pandas as pd
from io import BytesIO
import random

# KHWEZI minetech: HEALTH, SAFETY AND EQUIPMENT MONITORING SYSTEM

st.set_page_config(page_title="Khwezi MineTech", page_icon="⛏️", layout="wide")

# Application Design: lavender background and purple sidebar

st.markdown("""
<style>
/* Bold, readable field labels on every form */
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label,
div[data-testid="stWidgetLabel"] span,
.stTextInput label p,
.stNumberInput label p,
.stSelectbox label p,
.stTextArea label p {
    color: #23103E !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}

/* Purple border around text, number, dropdown and comment fields */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-testid="stNumberInput"] div[data-baseweb="input"],
div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    border: 2px solid #8A42C5 !important;
    border-radius: 10px !important;
    background-color: #FFFFFF !important;
}

/* Give form labels their own light bordered heading-style appearance */
div[data-testid="stWidgetLabel"] {
    display: inline-flex !important;
    align-items: center;
    border-left: 4px solid #8A42C5;
    border-bottom: 1px solid #CBB2E6;
    border-radius: 4px;
    padding: 4px 9px !important;
    margin-bottom: 7px !important;
    background: #EDE2FA;
}

/* Keep form field text dark and easy to read */
div[data-baseweb="input"] input,
div[data-baseweb="select"] *,
div[data-testid="stTextArea"] textarea {
    color: #161020 !important;
    font-weight: 650 !important;
}
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border: 2px solid #B99BDD !important;
    border-radius: 10px !important;
    background-color: #FFFFFF !important;
}
div[data-baseweb="input"] input {
    color: #111111 !important;
    font-weight: 600 !important;
}
div[data-baseweb="select"] {
    color: #111111 !important;
    font-weight: 600 !important;
}
.stApp { background: #F3EEFC; color: #301060; }
.block-container { padding-top: 1.7rem; max-width: 1400px; }

section[data-testid="stSidebar"] {
    background: linear-gradient(175deg, #35135F 0%, #512080 65%, #2C1055 100%);
}
section[data-testid="stSidebar"] * { color: #FFFFFF !important; }
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    border-radius: 12px;
    padding: 0.45rem 0.7rem;
    margin-bottom: 0.25rem;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: rgba(255,255,255,0.19);
    border-left: 4px solid #FF9D52;
}

h1, h2, h3 { color: #301060 !important; }

.minetech-title {
    color: #35135F;
    font-size: clamp(2.2rem, 4vw, 3.35rem);
    font-weight: 850;
    letter-spacing: -1.4px;
    margin-bottom: 0.1rem;
}
.minetech-tagline {
    color: #713F9E;
    font-size: 1.08rem;
    font-style: italic;
    margin-bottom: 0.35rem;
}
.minetech-description { color: #6A5484; font-size: 0.95rem; }
.minetech-divider {
    height: 5px;
    border-radius: 99px;
    background: linear-gradient(90deg, #8E26E5, #EF3D92, #FF963E);
    margin: 1.1rem 0 1.7rem;
}

.minetech-card {
    min-height: 168px;
    border-radius: 20px;
    padding: 23px 25px;
    box-shadow: 0 7px 20px rgba(60, 24, 100, 0.08);
    border-left: 6px solid;
    margin-bottom: 12px;
}
.minetech-card.purple { background: #E9D9FF; border-color: #A020F0; }
.minetech-card.pink { background: #FFE0ED; border-color: #FF3366; }
.minetech-card.orange { background: #FFE9D5; border-color: #FF8C00; }
.minetech-card.teal { background: #E0F7FA; border-color: #0000FE; }
.minetech-card-head { display: flex; justify-content: space-between; align-items: center; }
.minetech-card-label { color: #563778; font-size: 0.96rem; font-weight: 650; }
.minetech-card-number { color: #301060; font-size: 2.8rem; font-weight: 850; margin-top: 10px; }
.minetech-card-icon {
    width: 52px; height: 52px; border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 1.65rem; background: rgba(255,255,255,0.65);
}
.minetech-welcome {
    background: #E4F6E8; color: #21613A;
    padding: 18px 22px; border-radius: 14px;
    border-left: 5px solid #42B36A; margin-top: 20px;
    font-weight: 600;
}
.minetech-side-brand { text-align: center; padding: 12px 0 16px; }
.minetech-side-logo { font-size: 2.7rem; }
.minetech-side-name { color: white; font-size: 1.45rem; font-weight: 800; }
.minetech-side-line {
    height: 3px; border-radius: 50px;
    background: linear-gradient(90deg, #9C37FF, #EE448F, #FF953A);
    margin: 12px 0 10px;
}
.minetech-side-caption { color: #EADCF7; font-size: 0.83rem; text-align: center; }

.stButton > button {
    border-radius: 12px;
    border: 0;
    background: linear-gradient(90deg, #833AB4, #C13584, #F77737);
    color: white;
    font-weight: 650;
}
</style>
""", unsafe_allow_html=True)

# Access Control and Session State Initialization

USERS = {"Lubanzi": {"password": "L@Hlongwane", "role": "Administrator"},"Wandile": {"password": "W@Gumede", "role": "Safety Officer"},
    "Aphiwe": {"password": "A@Hlatshwayo", "role": "Mining Engineer"},"Cristiano": {"password": "C@Ronaldo", "role": "Maintenance Engineer"},
    "Tshepiso": {"password": "T@Takalo", "role": "Manager"},}

def init_state():
    defaults = {"logged_in": False,"username": "","role": "","equipment_records": [],"worker_records": [],"incident_df": pd.DataFrame(),"risk_records": [],
        "card_style": "purple",}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_state()

def read_uploaded_file(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".csv"):
        raw = uploaded_file.getvalue()
        try:
            df = pd.read_csv(BytesIO(raw))
            if len(df.columns) == 1 and ";" in str(df.columns[0]):
                df = pd.read_csv(BytesIO(raw), sep=";")
            return df
        except Exception:
            return pd.read_csv(BytesIO(raw), sep=";")
    if name.endswith((".xlsx", ".xls")):
        return pd.read_excel(uploaded_file)
    raise ValueError("Please upload a CSV or Excel file.")

def login_page():
    st.markdown("""<div class="minetech-title">⛏️ Khwezi MineTech</div>
    <div class="minetech-tagline">Protect Every Miner. Prevent Every Failure. Power Safer Mining.</div>
    <div class="minetech-description">Sign in to open the monitoring dashboard and access RBAC permissions.</div>
    <div class="minetech-divider"></div>""", unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", type="primary")
    if submitted:
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = USERS[username]["role"]
            st.rerun()
        else:
            st.error("Invalid username or password.")

if not st.session_state.logged_in:
    login_page()
    st.stop()

# RBAC Permissions Mapping (PROJECT TABLE 1)

role = st.session_state.role

allowed_pages = ["🏠 Dashboard"]

if role in ["Administrator", "Safety Officer", "Mining Engineer", "Maintenance Engineer", "Manager"]:
    allowed_pages.append("📊 Analytics and Reports")

if role in ["Administrator", "Safety Officer", "Mining Engineer", "Manager"]:
    allowed_pages.append("👷 Worker Safety")

if role in ["Administrator", "Safety Officer", "Mining Engineer", "Manager"]:
    allowed_pages.append("⚠️ Safety Incidents")

if role in ["Administrator", "Mining Engineer", "Maintenance Engineer", "Manager"]:
    allowed_pages.extend(["⚙️ Equipment Monitoring", "🔧 Maintenance", "🚨 Alerts & Notifications"])

if role in ["Administrator", "Safety Officer", "Mining Engineer", "Manager"]:
    allowed_pages.append("🛡️ Risk Assessment")

if role == "Administrator":
    allowed_pages.append("👥 Manage Users")

# Sidebar Navigation and User Information

with st.sidebar:
    st.markdown("""<div class="minetech-side-brand"><div class="minetech-side-logo">⛏️</div><div class="minetech-side-name">Khwezi MineTech</div>
        <div class="minetech-side-line"></div><div class="minetech-side-caption">Mining Safety & Intelligence</div></div>""", unsafe_allow_html=True)

    selected_page = st.radio("Navigation", allowed_pages)

    st.markdown(f"""<div style="margin-top: 20px; padding: 10px; background: rgba(255,255,255,0.1); border-radius: 8px;">
        <div style="font-size: 0.9rem;">User: <b>{st.session_state.username}</b></div><div style="font-size: 0.9rem;">Role: <b>{role}</b></div>
    </div>""", unsafe_allow_html=True)

    if st.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.rerun()

    st.markdown("""<div class="minetech-side-line" style="margin-top:32px"></div><div class="minetech-side-caption">
        Protect Every Miner.<br>Prevent Every Failure.<br>Power Safer Mining.</div>""", unsafe_allow_html=True)

page = selected_page.split(" ", 1)[1]

# Main Title Banner

st.markdown("""<div class="minetech-title">⛏️ Khwezi MineTech</div>
<div class="minetech-tagline">Protect Every Miner. Prevent Every Failure. Power Safer Mining.</div>
<div class="minetech-description">Mining Health, Safety and Equipment Intelligence System</div><div class="minetech-divider"></div>""", unsafe_allow_html=True)

# Helper function for live alerts generation

def get_all_active_alerts():
    alerts = []

    def number(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    def add_alert(item_id, category, parameter, value, severity, message, action):
        alerts.append({"ID": item_id,"Category": category,"Parameter": parameter,"Value": value,"Severity": severity,"Status": f"[{severity}] {message}",
            "Recommended Action": action,})

    for r in st.session_state.equipment_records:
        eq_id = str(r.get("Equipment_ID") or r.get("Equipment ID") or "EQ-UNKNOWN")
        temp = number(r.get("Temperature"))
        vib = number(r.get("Vibration"))
        maint = str(r.get("Maintenance_status") or r.get("Maintenance Status") or "")

        if temp > 100:
            add_alert(eq_id, "Equipment", "Temperature", f"{temp:g} °C", "CRITICAL",
                      "Temperature above 100 °C", "Stop equipment safely and inspect the cooling system.")
        elif temp >= 80:
            add_alert(eq_id, "Equipment", "Temperature", f"{temp:g} °C", "WARNING",
                      "Temperature between 80 and 100 °C", "Monitor the temperature and arrange inspection.")

        if vib > 8:
            add_alert(eq_id, "Equipment", "Vibration", f"{vib:g} mm/s", "CRITICAL",
                      "Vibration above 8 mm/s", "Inspect bearings, alignment and moving parts.")
        elif vib >= 5:
            add_alert(eq_id, "Equipment", "Vibration", f"{vib:g} mm/s", "WARNING",
                      "Vibration between 5 and 8 mm/s", "Check alignment and mounting bolts.")

        if maint.lower() == "overdue":
            add_alert(eq_id, "Maintenance", "Maintenance Status", maint, "CRITICAL",
                      "Maintenance overdue", "Arrange maintenance and follow site procedures.")
        elif maint.lower() == "due":
            add_alert(eq_id, "Maintenance", "Maintenance Status", maint, "WARNING",
                      "Maintenance due", "Schedule maintenance.")

    for w in st.session_state.worker_records:
        w_id = str(w.get("Worker ID") or w.get("Worker_ID") or "W-UNKNOWN")
        risk = str(w.get("Risk Level") or "").strip().capitalize()
        methane = number(w.get("Methane (ppm)"))
        dust = number(w.get("Dust (mg/m³)"))

        if methane > 500:
            add_alert(w_id, "Worker Safety", "Methane", f"{methane:g} ppm", "CRITICAL",
                      "Methane exceeds the project threshold", "Follow the site's gas response and ventilation procedures.")
        elif methane > 300:
            add_alert(w_id, "Worker Safety", "Methane", f"{methane:g} ppm", "WARNING",
                      "Methane exceeds the project warning threshold", "Investigate and verify ventilation conditions.")

        if dust > 5:
            add_alert(w_id, "Worker Safety", "Dust", f"{dust:g} mg/m³", "CRITICAL",
                      "Dust exceeds the project threshold", "Follow the site's dust-control procedures.")
        elif dust > 3:
            add_alert(w_id, "Worker Safety", "Dust", f"{dust:g} mg/m³", "WARNING",
                      "Dust exceeds the project warning threshold", "Check dust controls and exposure conditions.")

# Risk may also be Critical because of PPE and fatigue, not just methane.
        if risk in ("Critical", "High"):
            add_alert(w_id, "Worker Safety", "Overall Worker Risk", risk,
                      "CRITICAL" if risk == "Critical" else "WARNING",
                      f"Worker classified as {risk} risk", "Review the worker safety assessment and its warnings.")

    return alerts

# Dashboard Page

if page == "Dashboard":
    name = st.session_state.get("username", "Miner").capitalize()
    quotes = ["Your safety matters more than any production target.","Work safely today so you can return home tomorrow.",
        "A safe miner is a successful miner.","Every safe decision protects a life.","Great mining starts with safety."]
    quote = quotes[sum(ord(c) for c in name) % len(quotes)]

    st.success(f"👋 Welcome back, {name}!")
    st.info(f"💜 {quote}")
    st.header("Mining Operations Dashboard")
    st.write("Centralized overview of operational key performance indicators, safety incidents, and equipment condition.")

    with st.expander("⚙️ Dashboard Customization"):
        card_theme = st.selectbox("Primary Card Color Theme", ["purple", "pink", "orange", "teal"],
            index=["purple", "pink", "orange", "teal"].index(st.session_state.card_style))
        st.session_state.card_style = card_theme

    eq_records = st.session_state.equipment_records
    worker_records = st.session_state.worker_records
    incident_df = st.session_state.incident_df

    eq_count = len(eq_records)
    worker_count = len(worker_records)
    incident_count = len(incident_df) if isinstance(incident_df, pd.DataFrame) and not incident_df.empty else 0

    all_alerts = get_all_active_alerts()
    total_critical = sum(1 for a in all_alerts if a["Severity"] == "CRITICAL")

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        st.markdown(f"""<div class="minetech-card {st.session_state.card_style}"><div class="minetech-card-head">
                <span class="minetech-card-label">Equipment Monitored</span><span class="minetech-card-icon">⚙️</span></div>
            <div class="minetech-card-number">{eq_count}</div></div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<div class="minetech-card pink"><div class="minetech-card-head"><span class="minetech-card-label">Critical Alerts</span>
                <span class="minetech-card-icon">🚨</span></div><div class="minetech-card-number">{total_critical}</div></div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""<div class="minetech-card orange"><div class="minetech-card-head"><span class="minetech-card-label">Open Incidents</span>
                <span class="minetech-card-icon">📋</span></div><div class="minetech-card-number">{incident_count}</div></div>""", unsafe_allow_html=True)

    with col4:
        st.markdown(f"""<div class="minetech-card teal"><div class="minetech-card-head"><span class="minetech-card-label">Workers Monitored</span>
                <span class="minetech-card-icon">👷</span></div><div class="minetech-card-number">{worker_count}</div></div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="minetech-welcome">✅ Welcome, {role}! Your mining health, safety and equipment intelligence dashboard is active.</div>
    """, unsafe_allow_html=True)

# Worker Safety Page

elif page == "Worker Safety":
    st.header("👷 Worker Health and Safety Monitoring")
    st.write("Record and monitor worker safety compliance, fatigue levels, near misses, and environmental exposure.")

    with st.expander("📥 Import Worker Safety Records (CSV / Excel)"):
        uploaded_w = st.file_uploader("Upload file", type=["csv", "xlsx", "xls"], key="w_up")
        if uploaded_w is not None:
            try:
                df_imp = read_uploaded_file(uploaded_w)
                st.session_state.worker_records.extend(df_imp.to_dict(orient="records"))
                st.success(f"Imported {len(df_imp)} worker records.")
                st.rerun()
            except Exception as e:
                st.error(f"Import error: {e}")

    with st.form("worker_safety_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            worker_id = st.text_input("Worker ID")
            department = st.selectbox("Department", ["Mining", "Processing", "Engineering", "Maintenance", "Safety"])
            job_role = st.text_input("Job Role")
            shift = st.selectbox("Shift", ["Day", "Night"])
            ppe = st.selectbox("PPE Compliance", ["Yes", "No"])
            methane = st.number_input("Methane Concentration (ppm)", min_value=0.0, value=150.0)
        with c2:
            training = st.selectbox("Safety Training Status", ["Complete", "Incomplete"])
            fatigue = st.selectbox("Fatigue Level", ["Low", "Medium", "High"])
            near_misses = st.number_input("Number of Near Misses", min_value=0, step=1)
            previous_incidents = st.number_input("Number of Previous Incidents", min_value=0, step=1)
            dust = st.number_input("Dust Concentration (mg/m³)", min_value=0.0, value=1.0)
            temperature = st.number_input("Workplace Temperature (°C)", min_value=0.0, value=25.0)
        observations = st.text_area("Safety Observations")
        submitted = st.form_submit_button("Analyse & Save Worker Safety", type="primary")

    if submitted:
        if not worker_id.strip():
            st.error("Please enter a Worker ID.")
        else:
            warnings = []
            if ppe == "No": warnings.append("PPE non-compliance")
            if training == "Incomplete": warnings.append("Training incomplete")
            if fatigue == "High": warnings.append("High fatigue")
            if near_misses > 0: warnings.append("Near misses recorded")
            if methane > 500: warnings.append("High methane")
            if dust > 5: warnings.append("High dust")
            if temperature > 40: warnings.append("High temp")

            if (ppe == "No" and fatigue == "High") or methane > 500 or dust > 5 or temperature > 40:
                risk = "Critical"
            elif len(warnings) >= 2 or methane > 300 or dust > 3 or temperature > 35:
                risk = "High"
            elif len(warnings) == 1:
                risk = "Medium"
            else:
                risk = "Low"

            record = {"Worker ID": worker_id.strip(), "Department": department, "Job Role": job_role, "Shift": shift, "PPE Compliance": ppe,
                "Training": training, "Fatigue": fatigue, "Methane (ppm)": methane, "Dust (mg/m³)": dust, "Temperature (°C)": temperature,
                "Safety Observations": observations, "Near Misses": int(near_misses), "Previous Incidents": int(previous_incidents), "Risk Level": risk,
                "Warnings": "; ".join(warnings) if warnings else "None"}
            st.session_state.worker_records.append(record)
            st.success(f"Worker record saved. Risk Level: {risk}")
            st.rerun()

    if st.session_state.worker_records:
        st.subheader("Worker Records Database")
        df_w = pd.DataFrame(st.session_state.worker_records)
        st.dataframe(df_w, use_container_width=True, hide_index=True)
        st.download_button("Download Worker Records (CSV)", df_w.to_csv(index=False).encode("utf-8"), "worker_records.csv", "text/csv")

# Safety Incidents Page

elif page == "Safety Incidents":
    st.header("⚠️ Safety Incident Management Database")
    st.write("Upload, search, filter, categorize, and analyse safety incident datasets.")

    uploaded_inc = st.file_uploader("Upload Incident Dataset (CSV / Excel)", type=["csv", "xlsx", "xls"], key="inc_up")
    if uploaded_inc is not None:
        try:
            st.session_state.incident_df = read_uploaded_file(uploaded_inc)
            st.success(f"Loaded {len(st.session_state.incident_df)} incident records.")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    df_inc = st.session_state.incident_df
    if not isinstance(df_inc, pd.DataFrame):
        df_inc = pd.DataFrame()

    if df_inc.empty:
        st.info("No incident records available. Upload a dataset or add a record below.")
        with st.form("first_incident"):
            iid = st.text_input("Incident ID")
            itype = st.text_input("Incident Type")
            sev = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
            desc = st.text_area("Description")
            if st.form_submit_button("Add Incident"):
                st.session_state.incident_df = pd.DataFrame([{
                    "Incident_ID": iid, "Incident_Type": itype, "Severity": sev, "Description": desc}])
                st.rerun()
    else:
        search = st.text_input("Search incident records")
        view_df = df_inc.copy()
        if search.strip():
            mask = view_df.astype(str).apply(lambda col: col.str.contains(search.strip(), case=False, na=False)).any(axis=1)
            view_df = view_df[mask]
        st.dataframe(view_df, use_container_width=True, hide_index=True)
        st.caption(f"Showing {len(view_df)} of {len(df_inc)} record(s).")

        with st.expander("Analyse Incident Trends"):
            cat_cols = [c for c in df_inc.columns if df_inc[c].nunique() < 30]
            if cat_cols:
                chosen_col = st.selectbox("Group analysis by", cat_cols)
                st.bar_chart(df_inc[chosen_col].astype(str).value_counts())

        st.download_button("Download Incident Records (CSV)", df_inc.to_csv(index=False).encode("utf-8"), "incident_records.csv", "text/csv")

# Equipment Monitoring Page

elif page == "Equipment Monitoring":
    st.header("⚙️ Equipment Database & Condition Monitoring")
    st.write("Monitor equipment temperature, vibration, operating parameters, and automated status limits.")

    with st.expander("📥 Import Equipment Records (CSV / Excel)"):
        uploaded_eq = st.file_uploader("Upload equipment file", type=["csv", "xlsx", "xls"], key="eq_up")
        if uploaded_eq is not None:
            try:
                df_e = read_uploaded_file(uploaded_eq)
                if "Condition" not in df_e.columns and "Temperature" in df_e.columns and "Vibration" in df_e.columns:
                    df_e["Condition"] = df_e.apply(
                        lambda r: "CRITICAL" if float(r["Temperature"]) > 100 or float(r["Vibration"]) > 8 else ("WARNING" if float(r["Temperature"]) >= 80 or float(r["Vibration"]) >= 5 else "NORMAL"), axis=1)
                st.session_state.equipment_records.extend(df_e.to_dict(orient="records"))
                st.success(f"Imported {len(df_e)} equipment records.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

    with st.form("eq_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            eq_id = st.text_input("Equipment ID")
            eq_type = st.selectbox("Equipment Type", ["Haul Truck", "Loader", "Excavator", "Drilling Machine", "Bulldozer", "Crusher", "Conveyor"])
            mfr = st.text_input("Manufacturer")
            op_hours = st.number_input("Operating Hours (Operating Time)", min_value=0.0, value=1000.0)
        with c2:
            temp = st.number_input("Temperature (°C)", min_value=0.0, value=65.0)
            vib = st.number_input("Vibration (mm/s)", min_value=0.0, value=3.0)
            fuel = st.number_input("Fuel Consumption", min_value=0.0)
            downtime = st.number_input("Downtime (hours)", min_value=0.0, value=10.0)
        with c3:
            brake = st.selectbox("Brake Status", ["Good", "Needs inspection", "Faulty"])
            tyre = st.selectbox("Tyre Status", ["Good", "Needs inspection", "Not applicable"])
            engine = st.selectbox("Engine Status", ["Good", "Needs inspection", "Faulty"])
            maint_status = st.selectbox("Maintenance Status", ["Due", "Overdue", "Under Maintenance", "Up to date"])

        if st.form_submit_button("Save Equipment Record", type="primary"):
            if not eq_id.strip():
                st.error("Please enter Equipment ID.")
            else:
                condition = "CRITICAL" if temp > 100 or vib > 8 else ("WARNING" if float(temp) >= 80 or float(vib) >= 5 else "NORMAL")
                total_time = downtime + op_hours
                avail = round((op_hours / total_time) * 100, 1) if total_time > 0 else 100.0

                rec = {"Equipment_ID": eq_id, "Equipment_type": eq_type, "Manufacturer": mfr, "Operating_hours": op_hours,
                       "Temperature": temp, "Vibration": vib,"Fuel_consumption": fuel, "Brake_status": brake,
                       "Tyre_status": tyre, "Engine_status": engine, "Maintenance_status": maint_status,
                    "Downtime": downtime, "Availability (%)": avail, "Condition": condition}
                st.session_state.equipment_records.append(rec)
                st.success(f"Equipment saved. Condition: {condition} | Availability: {avail}%")
                st.rerun()

    if st.session_state.equipment_records:
        df_eq = pd.DataFrame(st.session_state.equipment_records)
        if "Availability (%)" not in df_eq.columns and "Operating_hours" in df_eq.columns and "Downtime" in df_eq.columns:
            df_eq["Availability (%)"] = df_eq.apply(
                lambda r: round((r["Operating_hours"] / (r["Downtime"] + r["Operating_hours"])) * 100, 1) if (r["Downtime"] + r["Operating_hours"]) > 0 else 100.0, axis=1)
        st.subheader("Equipment Database Records")
        st.dataframe(df_eq, use_container_width=True, hide_index=True)
        st.download_button("Download Equipment Records (CSV)", df_eq.to_csv(index=False).encode("utf-8"), "equipment_records.csv", "text/csv")

# Maintenance Monitoring and Advanced Graphs

elif page == "Maintenance":
    st.header("🔧 Equipment Maintenance Monitoring & Analytics")
    st.write("Track maintenance classifications (Due, Overdue, Under Maintenance), excessive downtime, low availability, and repeated alerts.")

    eq_recs = st.session_state.equipment_records
    if eq_recs:
        df_m = pd.DataFrame(eq_recs)
        if "Availability (%)" not in df_m.columns and "Operating_hours" in df_m.columns and "Downtime" in df_m.columns:
            df_m["Availability (%)"] = df_m.apply(
                lambda r: round((r["Operating_hours"] / (r["Downtime"] + r["Operating_hours"])) * 100, 1) if (r["Downtime"] + r["Operating_hours"]) > 0 else 100.0, axis=1)

        st.subheader("📊 Maintenance Status & Condition Breakdown")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Maintenance Classification (Due / Overdue / Under Maintenance)**")
            if "Maintenance_status" in df_m.columns:
                st.bar_chart(df_m["Maintenance_status"].value_counts())
            else:
                st.info("Maintenance status column not found.")
        with c2:
            st.markdown("**Equipment Condition / Alert Severity**")
            if "Condition" in df_m.columns:
                st.bar_chart(df_m["Condition"].value_counts())
            else:
                st.info("Condition column not found.")

        st.markdown("---")
        c3, c4 = st.columns(2)
        with c3:
            st.subheader("⚠️ Low Availability Equipment (< 85%)")
            low_avail = df_m[df_m["Availability (%)"] < 85.0]
            if not low_avail.empty:
                st.dataframe(low_avail[["Equipment_ID", "Equipment_type", "Availability (%)", "Downtime"]], use_container_width=True, hide_index=True)
            else:
                st.success("All monitored equipment has high availability (>= 85%).")

        with c4:
            st.subheader("🚨 Excessive Downtime (> 15 hours)")
            high_dt = df_m[df_m["Downtime"] > 15.0]
            if not high_dt.empty:
                st.dataframe(high_dt[["Equipment_ID", "Equipment_type", "Downtime", "Maintenance_status"]], use_container_width=True, hide_index=True)
            else:
                st.success("No equipment with excessive downtime flagged.")

        st.subheader("Complete Maintenance Log")
        st.dataframe(df_m, use_container_width=True, hide_index=True)
    else:
        st.info("No equipment records found. Please enter equipment data in Equipment Monitoring.")

# Risk Assessment Page

elif page == "Risk Assessment":
    st.header("🛡️ Operational Risk Assessment Matrix")
    st.write("Calculate risk scores using Likelihood (1-5) $\\times$ Consequence (1-5) with automated feedback and warnings.")

    with st.form("risk_form"):
        r_item = st.text_input("Activity / Hazard Description")
        c1, c2 = st.columns(2)
        with c1:
            likelihood = st.slider("Likelihood (1 = Rare, 5 = Almost Certain)", 1, 5, 3)
        with c2:
            consequence = st.slider("Consequence (1 = Insignificant, 5 = Catastrophic)", 1, 5, 3)

        if st.form_submit_button("Assess Risk Score", type="primary"):
            score = likelihood * consequence
            if score <= 4:
                classification = "Low"
                feedback = "🟢 LOW RISK (Score 1-4): Standard operating procedures apply. Routine monitoring is sufficient."
            elif score <= 9:
                classification = "Medium"
                feedback = "🟡 MEDIUM RISK (Score 5-9): Caution required. Implement operational controls and supervisory checks."
            elif score <= 16:
                classification = "High"
                feedback = "🟠 HIGH RISK (Score 10-16): Significant safety hazard. Mandatory safety intervention and engineering controls required."
            else:
                classification = "Critical"
                feedback = "🔴 CRITICAL RISK (Score 17-25): Unacceptable risk level! Stop all related operations immediately and notify site management."

            risk_entry = {"Hazard": r_item, "Likelihood": likelihood, "Consequence": consequence,"Risk Score": score,
                          "Classification": classification, "Feedback": feedback}
            st.session_state.risk_records.append(risk_entry)
            
            if classification == "Critical":
                st.error(feedback)
            elif classification == "High":
                st.warning(feedback)
            elif classification == "Medium":
                st.info(feedback)
            else:
                st.success(feedback)

    if st.session_state.risk_records:
        st.subheader("Evaluated Risks Log")
        df_risk = pd.DataFrame(st.session_state.risk_records)
        st.dataframe(df_risk, use_container_width=True, hide_index=True)

# Alerts and Notifications Page 

elif page == "Alerts & Notifications":
    st.header("🚨 Mining Monitoring Alert Console")
    st.write("View active operational alerts with parameter values, status levels, and recommended engineering actions.")
    st.caption("Alerts are calculated from worker and equipment records saved in this session. Add a record to see alerts here.")
    active_alerts = get_all_active_alerts()

    if active_alerts:
        critical_count = sum(a["Severity"] == "CRITICAL" for a in active_alerts)
        warning_count = sum(a["Severity"] == "WARNING" for a in active_alerts)
        st.warning(f"{len(active_alerts)} active alert(s): {critical_count} critical, {warning_count} warning.")
        df_alerts = pd.DataFrame(active_alerts)
        st.dataframe(df_alerts, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.markdown("### 🔍 Specific Alert Inspector")
        selected_id = st.selectbox("Select Record ID to View Specific Alert", df_alerts["ID"].unique())
        selected_alerts = df_alerts[df_alerts["ID"] == selected_id]

        for _, alert in selected_alerts.iterrows():
            with st.container(border=True):
                st.subheader(f"{alert['Severity']}: {alert['Category']}")
                st.write(f"**ID / Asset:** {alert['ID']}")
                st.write(f"**Parameter:** {alert['Parameter']}")
                st.write(f"**Value:** {alert['Value']}")
                st.write(f"**Status:** {alert['Status']}")
                st.write(f"**Recommended Action:** {alert['Recommended Action']}")
    else:
        st.success("✅ No active equipment or safety alerts detected.")
        st.info("Import records in **Equipment Monitoring** or **Worker Safety** to populate live alerts.")

# Analytics And Reports Page

elif page == "Analytics and Reports":
    st.header("📊 Interactive Data Analysis & Engineering Reports")
    st.write("Answering key mining engineering questions using dataset metrics (min, max, average, availability, compliance).")
    tab1, tab2, tab3 = st.tabs(["Equipment Performance Analytics", "Worker Safety & Environmental Scatter", "Meaningful Engineering Questions"])

    with tab1:
        st.subheader("Temperature vs. Vibration (Equipment Condition Clusters)")
        if st.session_state.equipment_records:
            df_eq = pd.DataFrame(st.session_state.equipment_records)
            if "Temperature" in df_eq.columns and "Vibration" in df_eq.columns:
                st.scatter_chart(df_eq, x="Temperature", y="Vibration", color="Condition" if "Condition" in df_eq.columns else None)
        else:
            st.info("No equipment data available.")

    with tab2:
        st.subheader("Worker Methane vs. Workplace Temperature")
        if st.session_state.worker_records:
            df_w = pd.DataFrame(st.session_state.worker_records)
            if "Methane (ppm)" in df_w.columns and "Temperature (°C)" in df_w.columns:
                st.scatter_chart(df_w, x="Methane (ppm)", y="Temperature (°C)", color="Risk Level" if "Risk Level" in df_w.columns else None)
        else:
            st.info("No worker records available.")

    with tab3:
        st.subheader("❓ Key Mining Engineering Questions Answered")
        
        eq_recs = st.session_state.equipment_records
        worker_recs = st.session_state.worker_records
        
        if eq_recs:
            df_e = pd.DataFrame(eq_recs)
            st.markdown("#### Equipment Performance Insights:")
            max_temp = df_e["Temperature"].max()
            min_temp = df_e["Temperature"].min()
            avg_temp = df_e["Temperature"].mean()
            st.markdown(f"- **Equipment Operating Temperatures:** Maximum: **{max_temp:.1f} °C**, Minimum: **{min_temp:.1f} °C**, Average: **{avg_temp:.1f} °C**.")
            
            if "Availability (%)" in df_e.columns:
                avg_avail = df_e["Availability (%)"].mean()
                min_avail = df_e["Availability (%)"].min()
                st.markdown(f"- **Equipment Availability:** Average fleet availability is **{avg_avail:.1f}%** (Lowest unit availability: **{min_avail:.1f}%**).")
            
            avg_downtime = df_e["Downtime"].mean() if "Downtime" in df_e.columns else 0
            st.markdown(f"- **Average Fleet Downtime:** **{avg_downtime:.1f} hours** per unit.")
        else:
            st.info("Import or log equipment records to view engineering analytics.")

        if worker_recs:
            df_w = pd.DataFrame(worker_recs)
            st.markdown("#### Worker Health & Safety Insights:")
            ppe_yes = len(df_w[df_w["PPE Compliance"] == "Yes"])
            ppe_pct = (ppe_yes / len(df_w)) * 100 if len(df_w) > 0 else 0
            st.markdown(f"- **PPE Compliance Rate:** **{ppe_pct:.1f}%** across all recorded workers.")
            
            avg_methane = df_w["Methane (ppm)"].mean() if "Methane (ppm)" in df_w.columns else 0
            max_methane = df_w["Methane (ppm)"].max() if "Methane (ppm)" in df_w.columns else 0
            st.markdown(f"- **Methane Concentration:** Average: **{avg_methane:.1f} ppm**, Maximum recorded: **{max_methane:.1f} ppm**.")
        else:
            st.info("Import worker safety records to view safety analytics.")

# Manage User Page

elif page == "Manage Users":
    if role != "Administrator":
        st.error("Access Denied: User management is restricted to Administrators per Table 1.")
    else:
        st.header("👥 System User Management")
        st.write("Overview of registered project team accounts and their assigned RBAC permissions from Table 1.")
        
        user_data = []
        for u, details in USERS.items():
            user_data.append({"Username": u, "Role": details["role"]})
        st.dataframe(pd.DataFrame(user_data), use_container_width=True, hide_index=True)