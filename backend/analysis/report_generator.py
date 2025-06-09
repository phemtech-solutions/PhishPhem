from fpdf import FPDF

def generate_report(meta, ai_result, rule_results, advice):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="PhishPhem AI Phishing Analysis Report", ln=True, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"From: {meta['from']}", ln=True)
        pdf.cell(200, 10, txt=f"Subject: {meta['subject']}", ln=True)
        pdf.ln(10)

        pdf.multi_cell(0, 10, txt="AI Assessment:\n" + ai_result)
        pdf.ln(5)

        pdf.multi_cell(0, 10, txt="Rule-Based Detection Results:\n")
        for k, v in rule_results.items():
            pdf.multi_cell(0, 10, txt=f"{k}: {v}")

        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 10, txt="Summary Advice", ln=True)
        pdf.set_font("Arial", size=12)

        # Clean advice of any invalid characters
        safe_advice = advice.encode("latin-1", "ignore").decode("latin-1")
        pdf.multi_cell(0, 10, txt=safe_advice)

        pdf.ln(10)
        pdf.set_font("Arial", style="I", size=10)
        pdf.cell(0, 10, txt="Designed by Ajijola Oluwafemi Blessing", ln=True, align="C")

        # ✅ Save to disk
        pdf.output("report.pdf")
        print("✅ PDF successfully written to report.pdf")
        return True
    except Exception as e:
        print(f"❌ PDF generation failed: {e}")
        return False
