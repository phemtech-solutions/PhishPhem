import streamlit as st

st.set_page_config(page_title="PhishPhem", page_icon="🛡️", layout="centered")

from backend.analysis.rule_checks import run_rule_checks
from backend.analysis.gpt_analysis import analyze_email_with_ai

from backend.analysis.report_generator import generate_report


if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

from email import message_from_string

st.title("PhishPhem — AI Phishing Email Analyzer")

uploaded_file = st.file_uploader("Or upload .eml file", type=["eml"], key="eml_upload_1")

raw_email = ""

if uploaded_file is not None:
    st.success(f"✅ Uploaded: {uploaded_file.name}")
    try:
        raw_bytes = uploaded_file.read()
        st.write(f"🔍 Read {len(raw_bytes)} bytes")  # Debug length
        raw_email = raw_bytes.decode("utf-8", errors="ignore")
        st.code(raw_email[:1000], language="text")
    except Exception as e:
        st.error(f"Failed to read file: {e}")
else:
    raw_email = st.text_area("Paste raw email content here:")

# Always show the Analyze button
if st.button("Analyze"):
  with st.spinner("🧠 Processing email... please wait."):
    if not raw_email.strip():
        st.warning("⚠️ Please upload a valid .eml file or paste raw content.")
        st.stop()

    # Continue analysis
    # st.success("📩 Email loaded successfully. Processing...")
    # (your message_from_string, parsing, AI, etc.)


    msg = message_from_string(raw_email)
    from_ = msg.get("From") or "unknown@example.com"
    subject = msg.get("Subject") or "(No Subject)"

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    body += payload.decode(errors="ignore")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors="ignore")

    st.write("**From:**", from_)
    st.write("**Subject:**", subject)

    # Followed by AI + rule-based logic
    with st.spinner("Analyzing with AI..."):
        ai_result = analyze_email_with_ai(body)
        st.subheader("AI Phishing Risk Assessment")
        st.markdown(ai_result)

    # Run rule-based detection
    rule_results = run_rule_checks(body, from_)
    st.subheader("Rule-Based Detection")
    st.markdown(f"**Suspicious Links:** {rule_results['suspicious_links']}")
    st.markdown(f"**Urgency Phrases:** {rule_results['urgency_phrases']}")
    st.markdown(f"**Domain Mismatches:** {rule_results['domain_mismatches']}")
    st.markdown(f"**Rule-Based Risk Score:** {rule_results['total_flags']} red flags")

    # Interpret the rule-based risk
    risk_score = rule_results["total_flags"]

    if risk_score == 0:
        advice = "✅ No suspicious indicators found. The email appears safe — but still verify the sender manually."
    elif 1 <= risk_score <= 2:
        advice = "⚠️ Some suspicious traits detected. Proceed with caution and verify links, attachments, and sender identity."
    elif 3 <= risk_score <= 4:
        advice = "🚨 Multiple red flags identified. This email is likely suspicious. Avoid clicking links or downloading attachments."
    else:
        advice = "❌ High phishing risk detected! Do not interact with this email. Report it immediately."

    st.session_state.advice = advice

    st.markdown(f"**🧠 Summary:** {advice}")

    st.session_state.analysis_done = True
    st.session_state.ai_result = ai_result
    st.session_state.rule_results = rule_results
    st.session_state.meta = {"from": from_, "subject": subject}
  st.success("✅ Analysis complete!")

if st.session_state.get("analysis_done"):
    if st.button("Export Report as PDF"):
        success = generate_report(
            st.session_state.meta,
            st.session_state.ai_result,
            st.session_state.rule_results,
            st.session_state.advice
        )
        if success:
            st.success("📄 Report generated!")
            with open("report.pdf", "rb") as f:
                st.download_button("📥 Download PDF Report", f, file_name="phishing_report.pdf")
        else:
            st.error("❌ Failed to generate the PDF report.")




st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px; color: gray;'>"
    "Designed by <strong>Ajijola Oluwafemi Blessing</strong>"
    "</div>",
    unsafe_allow_html=True
)
