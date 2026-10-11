import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="E-Commerce AI Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PREMIUM CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 10% 5%, rgba(99,102,241,.18), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(168,85,247,.14), transparent 25%),
        linear-gradient(135deg, #081120 0%, #0b132b 48%, #111827 100%);
    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding: 2rem 2.2rem 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1224 0%, #111a31 100%);
    border-right: 1px solid rgba(148,163,184,.15);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

.sidebar-logo {
    background: linear-gradient(135deg, #6366f1, #a855f7);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    font-size: 34px;
    box-shadow: 0 12px 35px rgba(99,102,241,.25);
    margin-bottom: 12px;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 38px;
    border-radius: 26px;
    background: linear-gradient(115deg, rgba(99,102,241,.92), rgba(124,58,237,.88) 55%, rgba(6,182,212,.72));
    border: 1px solid rgba(255,255,255,.18);
    box-shadow: 0 18px 55px rgba(0,0,0,.28);
    margin-bottom: 26px;
}

.hero:after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    right: -80px;
    top: -110px;
    background: rgba(255,255,255,.12);
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,.16);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 999px;
    padding: 7px 13px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .5px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0;
}

.hero-subtitle {
    font-size: 16px;
    opacity: .9;
    margin-top: 10px;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    margin: 24px 0 14px;
    color: #f8fafc;
}

.section-subtitle {
    color: #94a3b8;
    margin-top: -8px;
    margin-bottom: 16px;
}

.metric-card, .glass-card {
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(148,163,184,.16);
    box-shadow: 0 12px 35px rgba(0,0,0,.18);
    backdrop-filter: blur(14px);
    border-radius: 22px;
}

.metric-card {
    padding: 20px;
    min-height: 145px;
    transition: transform .2s ease, border-color .2s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(129,140,248,.55);
}

.metric-icon {
    width: 44px;
    height: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: rgba(99,102,241,.16);
    font-size: 22px;
}

.metric-label {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .7px;
    margin-top: 14px;
}

.metric-value {
    font-size: 29px;
    font-weight: 800;
    margin-top: 5px;
    color: #f8fafc;
    word-break: break-word;
}

.glass-card {
    padding: 24px;
    height: 100%;
}

.glass-card h3 {
    margin-top: 0;
    color: #f8fafc;
}

.glass-card p, .glass-card li {
    color: #cbd5e1;
}

.result-good {
    padding: 30px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(16,185,129,.18), rgba(6,78,59,.34));
    border: 1px solid rgba(52,211,153,.35);
    text-align: center;
}

.result-risk {
    padding: 30px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(244,63,94,.16), rgba(127,29,29,.28));
    border: 1px solid rgba(251,113,133,.35);
    text-align: center;
}

.result-label {
    font-size: 12px;
    font-weight: 800;
    color: #94a3b8;
    letter-spacing: 1px;
}

.result-main {
    font-size: 31px;
    font-weight: 800;
    margin: 10px 0;
}

.result-text {
    color: #cbd5e1;
    margin: 0;
}

.recommendation {
    padding: 20px;
    border-radius: 18px;
    background: rgba(30,41,59,.62);
    border-left: 4px solid #818cf8;
}

.footer {
    margin-top: 32px;
    padding: 20px;
    text-align: center;
    color: #64748b;
    border-top: 1px solid rgba(148,163,184,.12);
}

.stButton > button {
    width: 100%;
    height: 52px;
    border: none;
    border-radius: 14px;
    font-weight: 800;
    font-size: 14px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    box-shadow: 0 10px 25px rgba(99,102,241,.28);
}

.stButton > button:hover {
    border: none;
    transform: translateY(-1px);
}

[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
}

[data-testid="stMetricValue"] {
    color: #f8fafc;
}

div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
}

@media (max-width: 800px) {
    .block-container { padding: 1rem; }
    .hero { padding: 24px; }
    .hero-title { font-size: 30px; }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODELS
# =========================================================
@st.cache_resource
def load_models():
    models = joblib.load("models.pkl")
    scaler = joblib.load("scaler.pkl")
    cluster_scaler = joblib.load("cluster_scaler.pkl")
    kmeans = joblib.load("kmeans.pkl")
    best_model_name = joblib.load("best_model_name.pkl")
    return models, scaler, cluster_scaler, kmeans, best_model_name


try:
    models, scaler, cluster_scaler, kmeans, best_model_name = load_models()
    model_error = None
except Exception as e:
    models = scaler = cluster_scaler = kmeans = best_model_name = None
    model_error = str(e)


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown('<div class="sidebar-logo">🛒</div>', unsafe_allow_html=True)
st.sidebar.markdown("## E-Commerce AI")
st.sidebar.caption("Customer intelligence powered by machine learning")

st.sidebar.markdown("---")
st.sidebar.markdown("### 👤 Customer Profile")
st.sidebar.caption("Enter historical customer behaviour")

recency = st.sidebar.number_input("📅 Recency (Days)", min_value=0.0, value=30.0, step=1.0)
frequency = st.sidebar.number_input("🔄 Frequency (Orders)", min_value=0.0, value=5.0, step=1.0)
monetary = st.sidebar.number_input("💰 Monetary Value", min_value=0.0, value=1000.0, step=100.0)
total_products = st.sidebar.number_input("📦 Total Products", min_value=0.0, value=20.0, step=1.0)
average_order_value = st.sidebar.number_input("🧾 Average Order Value", min_value=0.0, value=200.0, step=10.0)

st.sidebar.markdown("---")
predict_button = st.sidebar.button("🚀 ANALYZE CUSTOMER", type="primary", use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Project Stack")
st.sidebar.caption("5 Classification Models")
st.sidebar.caption("K-Means Customer Segmentation")
st.sidebar.caption("Scikit-learn • Streamlit")


# =========================================================
# HERO HEADER
# =========================================================
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ AI-POWERED CUSTOMER INTELLIGENCE</div>
    <div class="hero-title">Smart E-Commerce<br>Analytics Dashboard</div>
    <div class="hero-subtitle">
        Predict customer purchases, measure probability and discover behavioural segments.
    </div>
</div>
""", unsafe_allow_html=True)

if model_error:
    st.error(f"Unable to load model files: {model_error}")
    st.stop()


# =========================================================
# HELPER FUNCTIONS
# =========================================================
def metric_card(icon, label, value):
    return f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """

def get_segment_name(cluster):
    names = {
        0: "Emerging Customer",
        1: "Loyal Customer",
        2: "High-Value Customer"
    }
    return names.get(int(cluster), f"Customer Segment {cluster}")


# =========================================================
# HOME DASHBOARD
# =========================================================
if not predict_button:
    st.markdown('<div class="section-title">📊 Intelligence Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">A modern overview of the machine learning system behind the dashboard.</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    values = [
        ("🤖", "ML Models", "5"),
        ("🧩", "Segmentation", "K-Means"),
        ("🎯", "Prediction", "YES / NO"),
        ("🏆", "Best Model", str(best_model_name))
    ]
    for col, item in zip(cols, values):
        with col:
            st.markdown(metric_card(*item), unsafe_allow_html=True)

    st.markdown('<div class="section-title">✨ What can this dashboard do?</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="glass-card">
            <h3>🎯 Purchase Prediction</h3>
            <p>Predict whether a customer is likely to make another purchase using historical behaviour.</p>
            <p><b>Key signals:</b></p>
            <ul>
                <li>Recency</li>
                <li>Frequency</li>
                <li>Monetary value</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-card">
            <h3>👥 Customer Segmentation</h3>
            <p>Use K-Means clustering to group customers with similar purchasing patterns.</p>
            <p><b>Behaviour analysed:</b></p>
            <ul>
                <li>Purchase frequency</li>
                <li>Spending behaviour</li>
                <li>Product activity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-card">
            <h3>💡 Smart Actions</h3>
            <p>Turn predictions into practical business recommendations and targeted campaigns.</p>
            <p><b>Possible actions:</b></p>
            <ul>
                <li>Loyalty rewards</li>
                <li>Personalized offers</li>
                <li>Re-engagement campaigns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Enter customer information in the sidebar and click **ANALYZE CUSTOMER** to generate an AI-powered result.")


# =========================================================
# CUSTOMER ANALYSIS
# =========================================================
else:
    new_customer = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary],
        "TotalProducts": [total_products],
        "AverageOrderValue": [average_order_value]
    })

    model = models[best_model_name]

    if best_model_name in ["Logistic Regression", "KNN", "SVM"]:
        scaled_customer = scaler.transform(new_customer)
        prediction = model.predict(scaled_customer)[0]
        probability = model.predict_proba(scaled_customer)[0][1]
    else:
        prediction = model.predict(new_customer)[0]
        probability = model.predict_proba(new_customer)[0][1]

    cluster_input = cluster_scaler.transform(new_customer)
    cluster = kmeans.predict(cluster_input)[0]
    prediction_text = "YES" if prediction == 1 else "NO"
    segment_name = get_segment_name(cluster)

    st.markdown('<div class="section-title">🎯 Customer Analysis Result</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Machine learning insights generated from the customer profile.</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    values = [
        ("📈", "Purchase Probability", f"{probability * 100:.1f}%"),
        ("🎯", "Purchase Again", prediction_text),
        ("👥", "Customer Segment", segment_name),
        ("🏆", "Best ML Model", str(best_model_name))
    ]
    for col, item in zip(cols, values):
        with col:
            st.markdown(metric_card(*item), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == 1:
        st.markdown(f"""
        <div class="result-good">
            <div class="result-label">PURCHASE PREDICTION</div>
            <div class="result-main">🟢 LIKELY TO PURCHASE</div>
            <p class="result-text">
                This customer has a <b>{probability * 100:.2f}%</b> predicted probability of purchasing again.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-risk">
            <div class="result-label">PURCHASE PREDICTION</div>
            <div class="result-main">🔴 UNLIKELY TO PURCHASE</div>
            <p class="result-text">
                This customer has a <b>{probability * 100:.2f}%</b> predicted probability of purchasing again.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">📈 Purchase Confidence</div>', unsafe_allow_html=True)

    gauge_color = "#22c55e" if probability >= 0.75 else "#f59e0b" if probability >= 0.50 else "#ef4444"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        number={"suffix": "%", "font": {"size": 45}},
        title={"text": "AI Purchase Probability", "font": {"size": 18}},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": gauge_color},
            "bgcolor": "rgba(255,255,255,0.08)",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 50], "color": "rgba(239,68,68,0.12)"},
                {"range": [50, 75], "color": "rgba(245,158,11,0.12)"},
                {"range": [75, 100], "color": "rgba(34,197,94,0.12)"}
            ]
        }
    ))
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=55, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#f8fafc"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">👤 Customer Behaviour & Recommendation</div>', unsafe_allow_html=True)
    left, right = st.columns([1, 1.15])

    with left:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Customer Profile Summary")

        details = pd.DataFrame({
            "Feature": ["📅 Recency", "🔄 Frequency", "💰 Monetary", "📦 Total Products", "🧾 Average Order Value"],
            "Value": [f"{recency:.0f} days", f"{frequency:.0f} orders", f"₹ {monetary:,.2f}",
                      f"{total_products:.0f}", f"₹ {average_order_value:,.2f}"]
        })
        st.dataframe(details, hide_index=True, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        if probability >= 0.75:
            level = "⭐ High Purchase Potential"
            text = "This customer shows strong buying potential. Focus on retention and value expansion."
            actions = ["Offer loyalty rewards", "Recommend premium products", "Use cross-selling campaigns", "Provide personalized recommendations"]
        elif probability >= 0.50:
            level = "🟡 Moderate Purchase Potential"
            text = "This customer may purchase again with the right motivation and personalized communication."
            actions = ["Send personalized offers", "Recommend relevant products", "Create limited-time discounts", "Use reminder campaigns"]
        else:
            level = "🔴 Low Purchase Potential"
            text = "This customer needs re-engagement. Use targeted incentives to rebuild purchase interest."
            actions = ["Launch a re-engagement campaign", "Provide discount incentives", "Send reminder emails", "Promote special offers"]

        st.markdown(f"""
        <div class="glass-card">
            <h3>💡 Business Recommendation</h3>
            <div class="recommendation">
                <h4 style="margin-top:0;">{level}</h4>
                <p>{text}</p>
                <b>Recommended actions:</b>
                <ul>{''.join(f'<li>{a}</li>' for a in actions)}</ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">👥 Customer Segment</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        <h3>🔵 {segment_name}</h3>
        <p>This customer was assigned to <b>Cluster {cluster}</b> by the K-Means model based on similar purchasing behaviour.</p>
        <p style="color:#94a3b8;">The segment can help the business create more targeted marketing and retention strategies.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🧠 AI Analysis Summary</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(metric_card("🤖", "Model Used", str(best_model_name)), unsafe_allow_html=True)
    with s2:
        st.markdown(metric_card("📊", "Final Prediction",
                                "Likely to Purchase" if prediction == 1 else "Needs Re-engagement"), unsafe_allow_html=True)
    with s3:
        st.markdown(metric_card("🧩", "Cluster", f"{segment_name} · {cluster}"), unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    🛒 <b>E-Commerce AI Intelligence</b> &nbsp; • &nbsp;
    Machine Learning CA2 Project &nbsp; • &nbsp;
    5 Classification Models + K-Means Segmentation
</div>
""", unsafe_allow_html=True)
